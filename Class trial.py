




class Car:
    def printSize(self):
        print("small")

class B(Car):
    def printSize(self):
        super().printSize()
        print("medium")
        


v = B()
v.printSize()
print(v.printSize())

'''This code defines two classes: Car and B. Here's a breakdown of what each part does:

class Car:: This line starts the definition of the Car class.

def printSize(self):: This defines a method named printSize() within the Car class. The self parameter is a reference to the current instance of the class, allowing the method to access variables and other methods of the class.

print("small"): Inside the printSize() method of the Car class, it prints "small" to the console.

class B(Car):: This line defines the B class, which inherits from the Car class. This means that B will have all the methods and properties of Car, and can also define its own.

def printSize(self):: Similarly, this line defines a printSize() method within the B class.

super().printSize(): This line calls the printSize() method of the parent class (Car) using super(). This ensures that the "small" message from the Car class is printed before anything else when printSize() is called on an instance of B.

print("medium"): This line prints "medium" to the console after the "small" message.

v = B(): This line creates an instance of the B class and assigns it to the variable v.

v.printSize(): This line calls the printSize() method of the B class on the instance v. This will print "small" followed by "medium" because of the method overrides in B.

print(v.printSize()): This line calls printSize() on the v object and then prints whatever printSize() returns. Since printSize() doesn't explicitly return anything, it implicitly returns None, so "small" and "medium" are printed, followed by None. '''
