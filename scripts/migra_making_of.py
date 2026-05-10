from migra_utils import migrar_campo_imagem, setup_django


setup_django()

from portfolio.models import MakingOf


migrar_campo_imagem(MakingOf, "foto_papel")

