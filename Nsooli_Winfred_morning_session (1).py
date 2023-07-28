class Education:
    def __init__(self, education):
        self._education=education
    def convert(self):
      return (self._education*9/5) +32
        
pen=Education(37)
get=pen.convert()
print("The conversion must be  ",get)

class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary  

    def pay_increment(self, increment_amount):
        self._salary += increment_amount

    def get_salary(self):
        return self._salary

employee = Employee("winfred", 850000)

print("Previous salary: "+ employee._name +" earned" , employee.get_salary())

employee.pay_increment(150000)

print("New salary: "+ employee._name +" earns", employee.get_salary())