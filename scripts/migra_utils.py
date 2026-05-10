import os
import sys
from io import BytesIO
from pathlib import Path

from django.core.files import File
from django.core.files.base import ContentFile


CLOUDINARY_FREE_MAX_BYTES = 10 * 1024 * 1024
UPLOAD_TARGET_BYTES = 9 * 1024 * 1024


def setup_django():
    base_dir = Path(__file__).resolve().parent.parent

    if str(base_dir) not in sys.path:
        sys.path.insert(0, str(base_dir))

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

    import django

    django.setup()


def preparar_imagem_para_upload(local_path):
    if local_path.stat().st_size <= CLOUDINARY_FREE_MAX_BYTES:
        return local_path.name, None

    try:
        from PIL import Image, ImageOps
    except ImportError:
        print(f"Imagem demasiado grande e Pillow nao esta instalado: {local_path}")
        return None, None

    try:
        with Image.open(local_path) as imagem:
            imagem = ImageOps.exif_transpose(imagem)

            if imagem.mode in ("RGBA", "LA", "P"):
                fundo = Image.new("RGB", imagem.size, (255, 255, 255))
                if imagem.mode == "P":
                    imagem = imagem.convert("RGBA")
                fundo.paste(imagem, mask=imagem.getchannel("A"))
                imagem = fundo
            else:
                imagem = imagem.convert("RGB")

            for max_side in (2400, 2000, 1600, 1200, 1000):
                copia = imagem.copy()
                copia.thumbnail((max_side, max_side))

                for quality in (85, 80, 75, 70, 65, 60):
                    buffer = BytesIO()
                    copia.save(buffer, format="JPEG", quality=quality, optimize=True)
                    conteudo = buffer.getvalue()

                    if len(conteudo) <= UPLOAD_TARGET_BYTES:
                        novo_nome = f"{local_path.stem}.jpg"
                        print(
                            f"Comprimido: {local_path.name} "
                            f"({local_path.stat().st_size} bytes -> {len(conteudo)} bytes)"
                        )
                        return novo_nome, conteudo
    except Exception as exc:
        print(f"Nao foi possivel comprimir {local_path}: {exc}")
        return None, None

    print(f"Imagem continua demasiado grande depois de comprimir: {local_path}")
    return None, None


def migrar_campo_imagem(model_class, field_name):
    from django.conf import settings

    media_root = Path(settings.MEDIA_ROOT)
    migrados = 0
    ignorados = 0
    em_falta = 0
    falhados = 0

    for obj in model_class.objects.all():
        ficheiro = getattr(obj, field_name)

        if not ficheiro or not ficheiro.name:
            ignorados += 1
            continue

        nome_guardado = ficheiro.name.replace("\\", "/")

        if nome_guardado.startswith(("http://", "https://")):
            ignorados += 1
            print(f"Ignorado URL remota: {model_class.__name__} #{obj.pk} -> {nome_guardado}")
            continue

        local_path = media_root / nome_guardado

        if not local_path.exists():
            em_falta += 1
            print(f"Em falta: {model_class.__name__} #{obj.pk} -> {local_path}")
            continue

        nome_upload, conteudo_comprimido = preparar_imagem_para_upload(local_path)

        if not nome_upload:
            falhados += 1
            print(f"Falhou: {model_class.__name__} #{obj.pk} - {obj}")
            continue

        try:
            if conteudo_comprimido is None:
                with local_path.open("rb") as f:
                    ficheiro.save(
                        nome_upload,
                        File(f),
                        save=True,
                    )
            else:
                ficheiro.save(
                    nome_upload,
                    ContentFile(conteudo_comprimido),
                    save=True,
                )
        except Exception as exc:
            falhados += 1
            print(f"Falhou upload: {model_class.__name__} #{obj.pk} - {obj}: {exc}")
            continue

        migrados += 1
        print(f"Migrado: {model_class.__name__} #{obj.pk} - {obj}")

    print(
        f"{model_class.__name__}.{field_name}: "
        f"{migrados} migrados, {ignorados} ignorados, "
        f"{em_falta} em falta, {falhados} falhados"
    )
