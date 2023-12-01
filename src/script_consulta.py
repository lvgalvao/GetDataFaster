# script principal
from consulta import Consulta
from loguru import logger
import time
import os

env = os.getenv('ENV')

logger.remove()  # Remove as configurações padrão
logger.add(
    "logs-index.log",
    format=f"{env} {{time:HH:mm:ss.SS}} {{level}} {{message}}"
)

consulta = Consulta()

# Consulta sem limit
print("Envio do pacote - Consulta sem limit")
logger.info("Envio do pacote - Consulta sem limit")
results = consulta.execute_query("SELECT name, salary FROM employees WHERE age > 30", explain=False)

time.sleep(5)

# Consulta com limit
print("Envio do pacote - Consulta com limit")
logger.info("Envio do pacote - Consulta com limit")
results = consulta.execute_query("SELECT name, salary FROM employees WHERE age > 30 LIMIT 10", explain=False)
