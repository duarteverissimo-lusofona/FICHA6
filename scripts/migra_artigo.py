from migra_utils import migrar_campo_imagem, setup_django


setup_django()

from artigos.models import Artigo


migrar_campo_imagem(Artigo, "fotografia")

