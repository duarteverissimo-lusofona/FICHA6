from migra_utils import migrar_campo_imagem, setup_django


setup_django()

from artigos.models import Artigo
from escola.models import Curso
from portfolio.models import (
    Docente,
    Formacao,
    MakingOf,
    Projeto,
    Tecnologia,
    UnidadeCurricular,
)


MIGRACOES = [
    (Curso, "imagem"),
    (Artigo, "fotografia"),
    (Docente, "foto"),
    (UnidadeCurricular, "imagem"),
    (Tecnologia, "logo"),
    (Projeto, "imagem"),
    (Formacao, "certificado"),
    (MakingOf, "foto_papel"),
]


for model_class, field_name in MIGRACOES:
    migrar_campo_imagem(model_class, field_name)
