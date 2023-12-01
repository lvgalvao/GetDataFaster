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

# # Consulta normal
# result_count = consulta.execute_query("SELECT count(*) FROM employees WHERE age > 31")
# count = result_count[0][0]
# logger.info(f"Total de funcionários: {count}")


# Consulta 1
results = consulta.execute_query("SELECT name, salary FROM employees WHERE age > 30", explain=False)
# Consulta 2
results = consulta.execute_query("SELECT * FROM employees WHERE age > 30", explain=False)

time.sleep(5)

# Consulta 3 - Funcionários com mais de 30 anos (LIMIT 10)
results = consulta.execute_query("SELECT name, salary FROM employees WHERE age > 30 LIMIT 10", explain=False)

