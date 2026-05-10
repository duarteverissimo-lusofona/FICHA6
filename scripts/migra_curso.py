from migra_utils import migrar_campo_imagem, setup_django


setup_django()

from escola.models import Curso


migrar_campo_imagem(Curso, "imagem")

