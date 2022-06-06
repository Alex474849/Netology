from application.people import *
from application.salary import *
from datetime import datetime, date, time


def main():
    # print(f'Your salary on year {quantity * 12}')
    print(f'You tax pay for month {quantity / 100 * 20}')
    year = quantity / 100 * 20 * 12
    print(f'You tax pay for year {year}')
    print(f'Your salary on year with tax {quantity * 12 - year}')
    print(datetime.now())

if __name__ == '__main__':
    main()




