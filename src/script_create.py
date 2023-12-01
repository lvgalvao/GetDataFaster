from database import create_table
from data_generator import generate_data

def main():
    create_table()
    generate_data(428000)

if __name__ == "__main__":
    main()
