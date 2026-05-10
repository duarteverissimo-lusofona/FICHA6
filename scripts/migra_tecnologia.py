from migra_utils import migrar_campo_imagem, setup_django


setup_django()

from portfolio.models import Tecnologia


migrar_campo_imagem(Tecnologia, "logo")

