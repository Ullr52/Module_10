from datetime import datetime
class Employee:

    def __init__(self, last_name, first_name, address, phone_number, salaried, start_date, salary):
        self.last_name = last_name
        self.first_name = first_name
        self.address = address
        self.phone_number = str(phone_number)
        self.salaried = salaried
        self.salary = '%.2f' % float(salary)
        dateObj = datetime.strptime(start_date, '%m/%d/%Y')
        self.__start_date = dateObj.strftime('%m/%d/%Y')


    def display(self):
        str = f'{self.first_name} {self.last_name}\n'
        str+= f'{self.address}\n'
        if self.salaried:
            str+= f'Salaried employee: ${self.salary}/year \n'
            str+= f'Start date: ${self.__start_date}/year \n'
        return str

E = Employee("Patel", "Sasha", "123 Main Street \nUrban, Iowa", "9082098121", True, '06/28/2019', 40000)
print(E.display())
E = Employee("Patel", "Sasha", "123 Main Street \nUrban, Iowa", "9082098121", False,'03/26/2022', 0)
print(E.display())
