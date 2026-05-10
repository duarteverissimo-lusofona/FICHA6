from migra_utils import migrar_campo_imagem, setup_django


setup_django()

from portfolio.models import Formacao


migrar_campo_imagem(Formacao, "certificado")

