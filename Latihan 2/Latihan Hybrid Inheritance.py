# LINDA NOVITA JULIYANTI
# 210510003
# D3

class Seseorang:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    def get_info(self):
        print("Name :", self.name)
        print("Age :", self.age)
        print("Address :", self.address)

class Mahasiswa(Seseorang):
    def __init__(self, name, age, address, nim):
        super().__init__(name, age, address)
        self.nim = nim
    def get_info(self):
        super().get_info()
        print("NIM :", self.nim)

class Employee(Seseorang):
    def __init__(self, name, age, address, employee_id, salary):
        super().__init__(name, age, address)
        self.employee_id = employee_id
        self.salary = salary
    def get_info(self):
        super().get_info()
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)

mahasiswa = Mahasiswa("Hilda", 25, "Cirebon", "8724940")
mahasiswa.get_info()
employee = Employee("Hilda", 25, "Cirebon", "09824585", "$6500")
employee.get_info()
