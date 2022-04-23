from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime as dt

if __name__ == '__main__':
    print(dt.now().strftime("%d-%m-%Y %H:%M:%S"))
    calculate_salary()
    get_employees()

