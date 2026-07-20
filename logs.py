import logging
import os

from logging import handlers

# BOILERPLATE
# TODO: Usar função
# TODO: Usar lib (loguru)

log_level = os.getenv("LOG_LEVEL", "DEBUG").upper()

# nossa instância
log = logging.Logger("logs.py", log_level)

# level
#ch = logging.StreamHandler() # Console/terminal/stderr
#ch.setLevel(log_level)
fh = handlers.RotatingFileHandler(
    "meulog.log", 
    maxBytes=300, # 10**6 -> 1mb
    backupCount=10
)
fh.setLevel(log_level)

# formatação
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
#ch.setFormatter(fmt)
fh.setFormatter(fmt)

# destino
#log.addHandler(ch)
log.addHandler(fh)

"""
log.debug("Mensagem para dev, qe, sysadmin")
log.info("Mensagem geral para usuários")
log.warning("Aviso que não causa erro")
log.error("Erro que afeta uma única execução")
log.critical("Erro geral ex: banco de dados sumiu")
"""

print("---")

try:
    1/0
except ZeroDivisionError as e:
    log.error("Deu erro %s", str(e))