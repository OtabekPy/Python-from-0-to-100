
"""""
class Student:
    allstudents=[]
    def __init__(self,sub,lastname):
        self.sub=sub
        self.lastname=lastname
        self.subject=[]

    def addsubject(self):
        self.subject.append(self.sub)



    def allstudentscha(self,year):
        Student.allstudents.append(year)

ss1=Student('Python','Otabek')
ss1.addsubject()
ss2=Student('Python','Otabek')
ss2.allstudentscha(year=2020)
print(Student.allstudents)
"""

"""""

class Avto:
    def __init__(self,name,location,curentavto):
        self.name=name
        self.location=location
        self.curentavto=curentavto
        self.adding=[]


    def shows(self):
        print(self.name)
        print(self.location)
        print(self.curentavto)

    def addadd(self):
        self.names=input("enter your name")
        self.locations=input("enter your location")
        self.curentavtos=input("enter your curentavto")
        self.adding.append(self.names)
        self.adding.append(self.locations)
        self.adding.append(self.curentavtos)

        return self.adding

aa=Avto('James','Smith',2020)
aa.shows()
print(aa.addadd())
"""
"""""
class Student:
    students = []

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def show(self):
        print(f"ID: {self.id}, Name: {self.name}, Age: {self.age}")

    def addstudent(self):
        Student.students.append(self.name)

        Student.students.append(self.age)
        return self.students
ss1=Student('Alijon','Samuniyel',2020)
ss2=Student('Otabek','Kuchkinov',2020)
print(ss1.addstudent())
print(ss2.addstudent())
"""
"""""
class Product:
    products = []

    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def shows(self):
        print(
            f"ID: {self.id} | Name: {self.name} | "
            f"Price: {self.price} | Quantity: {self.quantity}"
        )


    def adss(self):
        Product.products.append(self)

    def Shows(self):
        for kes in Product.products:
            print(f"ID: {kes.id} | Name: {kes.name} | Price: {kes.price} | Quantity: {kes.quantity}")


    def deleate(self):
        for keys in Product.products:
            if keys.name=="James":

               Product.products.remove(keys)
               break


    def delateid(self):
        for keyss in Product.products:
            if keyss.id==2:
                Product.products.remove(keyss)

P1=Product(1,"James",20,1)
P2=Product(2,"Smith",20,2)
print(P1.shows())
print(P2.shows())
P1.adss()
P2.adss()
P1.Shows()
P2.Shows()
print(Product.products)
P1.deleate()
P2.deleate()
P2.delateid()

"""
"""""
class Employee:
    employees = []

    def __init__(self, id, name, age, salary):
        self.id = id
        self.name = name
        self.age = age
        self.salary = salary


    def addn(self):
        Employee.employees.append(self)



    def shows(self):
        for kes in Employee.employees:
            newreturn=f"{kes.id} | Name: {kes.name} | Salary: {kes.salary}"
            return newreturn

    def deletestent(self):
        for kes in Employee.employees:
            if kes.id==2:
                Employee.employees.remove(kes)
                break

    def idshowa(self,id):
        self.id=id
        for kes in Employee.employees:
            if kes.id==id:
                return f"ID: {kes.id} | Name: {kes.name}"
            else:
                return "Not found"

    def addsalary(self):
        total=0
        for kes in Employee.employees:
            total+=kes.salary
        return total
E=Employee(2,"James",20,1)
E1=Employee(3,"Smith",20,2)
E2=Employee(4,"Kuchkinov",20,3)
E.addn()
E1.addn()
E2.addn()
print(E1.shows())
print(E2.shows())
print(E.shows())
"""



class Book:
    books = []

    def __init__(self, id, title, author, price):
        self.id = id
        self.title = title
        self.author = author
        self.price = price


    def addbook(self):
        Book.books.append(self)

    def showbook(self):
        for kes in Book.books:
                print(f"{kes.id} | Title: {kes.title} | Author: {kes.author},Price: {kes.price}")


    def finds(self,id):
        found=False
        for ids in Book.books:
            if ids.id==id:
                print("Found Successfully")
                print(f"{ids.id} | Title: {ids.title} | Author: {ids.author}")
                found=True
        if not found:
            print("Not found")


    def deleate(self,id):
        found=False
        for kes in Book.books:
            if kes.id==id:
                Book.books.remove(kes)
                found=True
        if not found:
            print("Not found")


    def update(self,id,newprice):
        found=False
        for kes in Book.books:
            if kes.id==id:
                kes.price=newprice
                found=True
        if not found:
            print("Not found")

b1 = Book(1, "Python Basics", "John", 15)
b2 = Book(2, "OOP Python", "Alex", 30)
b3 = Book(3, "FastAPI", "Mike", 25)
b1.addbook()
b2.addbook()
b3.addbook()
b1.showbook()
b1.finds(1)
b2.finds(2)
b3.finds(4)
b1.deleate(1)
b1.showbook()
b1.update(3,100)
b1.showbook()






