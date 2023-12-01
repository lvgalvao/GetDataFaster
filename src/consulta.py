# consulta.py
from loguru import logger
from database import Session
from sqlalchemy import text
import time

class Consulta:
    def __init__(self):
        self.session = Session()

    def execute_query(self, query, explain=False):
        start_time = time.time()

        print("Início do processamento pelo servidor")
        logger.info("Início do processamento pelo servidor")
        if explain:
            result = self.session.execute(text(f"EXPLAIN ANALYZE {query}")).fetchall()
            for line in result:
                logger.info(line[0])
            result = self.session.execute(text(query)).fetchall()
            print(result)
        else:
            result = self.session.execute(text(query)).fetchall()
            print(result)

        end_time = time.time()
        exec_time = round(end_time - start_time, 2)  # Tempo total com duas casas decimais

        print(f"Consulta completada em {exec_time} segundos. Resultados: {len(result)} registros.")
        logger.info(f"Consulta completada em {exec_time} segundos. Resultados: {len(result)} registros.")

        return result
