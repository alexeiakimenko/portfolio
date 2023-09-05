class Student:
    def __init__(self, name):
        self.name = name
        self.comp = self.Computer()

    def student_print(self):
        print(f'{self.name} => {self.comp.model} {self.comp.pr} {self.comp.mem}')

    class Computer:
        def __init__(self):
            self.model = 'HP'
            self.pr = 'i7'
            self.mem = '16'


n1 = Student('Roman')
n2 = Student('Vladimir')
n1.student_print()
n2.student_print()
