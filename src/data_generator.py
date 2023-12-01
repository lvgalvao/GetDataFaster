from faker import Faker
from database import Employee, Session

def generate_data(num_records, batch_size=1000):
    session = Session()
    fake = Faker()

    for i in range(num_records):
        employee = Employee(
            name=fake.name(),
            salary=fake.random_number(digits=5),
            age=fake.random_int(min=18, max=70),
            department=fake.job()
        )
        session.add(employee)

        # Comete os registros em lotes
        if (i + 1) % batch_size == 0:
            session.commit()
            session.close()
            session = Session()

    # Comete quaisquer registros restantes
    session.commit()
    session.close()