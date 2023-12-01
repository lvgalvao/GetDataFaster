# script principal
from consulta import Consulta
from loguru import logger
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


# Consulta 1 - Funcionários com mais de 30 anos (LIMIT 10)
results = consulta.execute_query("SELECT name, salary FROM employees WHERE age > 20 LIMIT 10", explain=True)
# Consulta 2
results = consulta.execute_query("SELECT name, salary FROM employees WHERE age > 20", explain=True)
# Consulta 3
results = consulta.execute_query("SELECT * FROM employees WHERE age > 20", explain=True)



