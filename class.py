class Person:

    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def provide():
        print(self.fname," ",self.lname," is of age ",self.age)
    
p1 = Person("deexith","parandaman",45)
print(p1.provide())
