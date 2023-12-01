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

        # Aqui você pode adicionar lógica para calcular o tempo de plano e execução, se necessário
        # Por exemplo, você pode analisar os resultados do EXPLAIN ANALYZE para extrair esses tempos

        logger.info(f"Consulta completada em {exec_time} segundos. Resultados: {len(result)} registros.")

        return result
