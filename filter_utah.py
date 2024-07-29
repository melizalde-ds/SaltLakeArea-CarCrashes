import pandas as pd


def filter_utah():
    raw = pd.read_csv('Data/Raw.csv')
    utah = raw[raw['State'] == 'UT']
    utah.to_csv('Data/Utah.csv', index=False)


def filter_salt_lake():
    utah = pd.read_csv('Data/Utah.csv')
    salt_lake = utah[utah['County'] == 'Salt Lake']
    salt_lake.to_csv('Data/Salt_Lake.csv', index=False)


def menu():
    loop = True
    while (loop):
        print('1. Filter Utah')
        print('2. Filter Salt Lake')
        print('3. Exit')
        choice = int(input('Enter choice: '))
        if choice == 1:
            filter_utah()
        elif choice == 2:
            filter_salt_lake()
        elif choice == 3:
            loop = False
        else:
            print('Invalid choice')


menu()
