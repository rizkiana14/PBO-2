# LINDA NOVITA JULIYANTI
# 210510003
# D3

class Hewan:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} growls")

class Dog(Hewan):
    def __init__(self, name, kind):
        super().__init__(name)
        self.kind = kind
    def run(self):
        print(f"{self.name} is a dog that can run faster than any {self.kind} of them")

class Wolf(Dog):
    def __init__(self, name, kind, color):
        super().__init__(name, kind)
        self.color = color
    def growls(self):
        print(f"{self.name} is a wolf type dog with a {self.color} color")

wolf = Wolf("Jacob", "kind", "Black")
wolf.growls()
wolf.run()
