from database import create_table
from data_generator import generate_data

def main():
    create_table()
    generate_data(3_000_000)

if __name__ == "__main__":
    main()
