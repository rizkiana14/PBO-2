class Kalkulator:
    @staticmethod
    def add(x, y):
        return x + y
    @staticmethod
    def subtract(x, y):
        return x - y
    @staticmethod
    def multiply(x, y):
        return x * y
    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ValueError('Tidak dapat membagi dengan nol.')
        return x / y
# Memanggil metode statis add() dan subtract() di dalam class Math
print(Kalkulator.add(2, 5)) # Output: 8
print(Kalkulator.subtract(10, 5)) # Output: 3
# Memanggil metode statis multiply() dan divide() di dalam class Math
print(Kalkulator.multiply(2, 6)) # Output: 24
print(Kalkulator.divide(12,6)) # Output: 3.0