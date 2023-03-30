# Object Oriented Programming 

# What is an Object?

# Class defines a series of function (methods, operations)
# that can be applied to the objects, this sums the interface of the object 


# NOTE : AN OBJECT IS AN INSTANCE OF A CLASS 


# Exemple->
#  Cat:
#      - Attributes: • age 
#                    • name
#                    • hair colour
#                    • weight  
#  
#      - Functionalities • miaw! (makes noises)   
#                        • purss! (makes different noises)
#                        • sleeps
#                        • eats

# Attributes consists in what a class has, and Functionalities in what that class does


# NOTE: Inheritance si used for the DRY principle to be avoid (DO NOT REPEAT YOURSELF)


# Inheritance 

# Inheritance is used to not DRY 

# ANIMAL -------> MAMMAL ------> CAT 

# Parent Class ------> Child Class 


# Exemple -->
# NOTE class Mammal should be abstract, because you cannot point to something defined only as Mammal 


# class Mammal:                             class:Animal:Mammal: (The Animal inherits from Mammal)
#               - Attributes:                                   - Attributes: 
#                          • age                                              •  ̶a̶g̶e̶
#                          • weight                                           •  ̶w̶e̶i̶g̶h̶t̶ ̶                                       
#                                                                             • name (because it's an Animal not a Mammal)                              
#                                                                             • colour (because it's an Animal not a Mammal)
# 
#               - Methods • sleeps                              - Methods     • miaw! (makes noises) 
#                         • birts                                             • purss! (makes more noises)
#                         • eats                                              •  ̶s̶l̶e̶e̶p̶s̶
#                                                                             •  ̶b̶i̶r̶d̶s̶
#                                                                             •  ̶e̶a̶t̶s̶


# Inheritance represents a relation of type "is-a" 
# Exemple: The Cat is a Mammal (Inheritance)

# Inheritance DOES NOT represent a relation of type "has-a"
# The Cat has fur, name etc ( THOSE ARE ATTRIBIUTES)

# Inheritance DOES NOT represent a relation of type "does"
# The Cat does something() (those are methods/functions)



# notation--->


# CLASS(class)
# •template for the creation of objects of a specific type 

# METHODS
# •they are functions that belong to a class

# ATTRIBUTES
# •variabiles that belong to a class

# OBJECT 
# •specific instance of a class

# Inheritance
# •method where a class inherits the behavior of another class 

# Composition 
# •creation of complex objects with the help of other objects 

 


# Exemples 

class Cat:
    def __init__(self,name):    # constructor of class
        self.name = name        # self. is the bounding that needs to be done inside the class 
        print("an object is created ")
    def print_object(self):                            # I can create how many functions I desire 
        print("the name of the cat is =", self.name)




# Object instantiation 

x = Cat("rino") # here I pass my class her attributes 
print(x.name)   # I call the variable with attributes of the class( in this case the function self.name)

y = Cat("tazz")  # I assign the variable with the class
y.print_object() # I call the variable with function print_object() that is embaded in the class 



# Exemples

class Car:
    def __init__(self,brand,year,colour,km = 0, *parameters):
        self.brand = brand
        self.year = year
        self.colour = colour
        self.colour2 = "Maro" # without self. I hard assign it 
        self.km = km 
        print(parameters)

class Driver:
    def __init__(self):
        pass




M1 = Car( "Mercedes",  2007,     "rosu",     10,      4 ,5 ,764) # everything after values not declare enter a Tuple// see args and kargs for reference 
print(     M1.brand,   M1.year,  M1.colour,  M1.km)   #()



M2 = Car(  "BMW",      1997,    "White",     100,     20,30,40,50)
print(     M2.brand,   M2.year,  M2.colour,  M2.km)   #()


print(M2.colour2) # If i need to call the hard assigned 



# Exercise 
# Make a class for a Computer 

class Calculator():
    def __init__(self, nr1, nr2):
        self.nr1 = nr1
        self.nr2 = nr2
    def add(self):
        return self.nr1 + self.nr2
    def sub(self):
        return self.nr1 - self.nr2
    def mul(self):
        return self.nr1 * self.nr2
    def div(self):
        return self.nr1 // self.nr2



test_Calculator = Calculator(100,10)
print(test_Calculator.add())
print(test_Calculator.sub())
print(test_Calculator.mul())
print(test_Calculator.div())




# Exercise 

#The Point class must be created to abstract a point from a plane (x and y coordinates)
#• The class has the following characteristics:
#• Point x and point y
#• The class has the following implementations:

#show - the coordinates of the point are printed;
#move - the coordinates are moved;
#setToOrigin - set the coordinates (0, 0)


from math import sqrt # we need math to calculate the distance between points pythag

class Point():
    def __init__(self, x,y):
        self.x = x 
        self.y = y

    def show(self):               # We see our point(x,y)
        print([self.x, self.y])

    def move(self, new_x, new_y):     # we assign new coordonates
        self.x, self.y = new_x,new_y

    def setToOrigin(self):            # we set to origin
        self.x, self.y = 0, 0 

    def dist(self, another_point):          # we add the same class as operation to our method 
        [self.x , self.y ,another_point.x , another_point.y]  # we import sqrt from math to obtain the distance between them 
        return sqrt((self.x - another_point.x)**2 + (self.y - another_point.y)**2) 
        # I substract the points and apply Pythagorean theorem



point = Point(3,4)
point.show()        # [3, 4]
point.move(7,6)   
point.show()        # [7, 6]
point.setToOrigin()
point.show()        # [0, 0]


point1 = Point(4,5)  # I make 2 new objects to assign 
point2 = Point(1,1)  # I transfer to method dist() the class Point as a parameter 


# Printing them will give me this // Without making operations with them 
print(point2.dist(point1)) # [1, 1, 4, 5]
print(point1.dist(point2)) # [4, 5, 1, 1]



print(point1.dist(point2)) # 5.0 the distance between the 2 points 
print(point2.dist(point1)) # 5.0 the distance between the 2 points 




# Exercise 

# Build the Wallet class that abstracts a bank account
#• The class has the following implementations with the necessary checks:

# widthdraw - money is drawn from the wallet
# addMoney - money is added to the wallet
# showBalance - print balance 



class Account():
    def __init__(self, money = 0):
        self.money = money 

    def showBalance(self):
        print(self.money)

    def addMoney(self, money_in):
        self.money += money_in
   
    def withdraw(self, money_out):
        if money_out < self.money:
            self.money -= money_out
        else:
            print("impossible")



wallet = Account(500)
wallet.showBalance()   # 500


wallet.withdraw(300)  # 200  if money_out < self.money 
wallet.showBalance()  # else: "impossible"


wallet.addMoney(200)   # 400
wallet.showBalance()



# Exercise  


#  Create a Car class() twith the attributes: brand, consumption, tank, km, tank capacity
#  With the moethods Show, Recharge, Km_made  

class Car():
    def __init__(self, brand, consumption, tank, km = 0, tank_capacity = 60):
        self.brand = brand
        self.consumption = consumption 
        self.tank = tank 
        self.km = km 
        self.tank_capacity = tank_capacity
    
    def __str__(self):
        return f"brand={self.brand},consumption={self.consumption},tank={self.tank}, km={self.km},tank capacity= {self.tank_capacity}"

     
    def gas_recharge(self, liters):
        if self.tank <= self.tank_capacity:
            self.tank += liters
        else:
            self.tank = self.tank_capacity 

    def km_made(self,new_km):
        if new_km * self.consumption / 100 < self.tank_capacity:
            self.tank -= new_km * self.consumption / 100 
            self.km += new_km 
        else:
            self.km += self.tank / self.consumption * 100
            self.tank = 0 


# We create our object and call our methods
my_car = Car("Ferrari", 7, 10, 100)
print(my_car)# brand=Ferrari,consumption=7,tank=10, km=100,tank capacity= 60


my_car.gas_recharge(10)
print(my_car) # brand=Ferrari,consumption=7,tank=20, km=100,tank capacity= 60


my_car.km_made(10)
print(my_car) # brand=Ferrari,consumption=7,tank=19.3, km=110,tank capacity= 60



# Interactions between Classes


# Encapsulation 


# Def. Encapsulation is the process where our data and functions are kept separate from the exterior( Private Functions and Atributes)
# They are accessible only in the interior of our class


#    ____________________________________________________________________
#   |                                                                    |
#   |         OBJECT:                                                    |
#   |                -public attributes     <<<--------------------------|-------------- Accessible everywear, in the interior of the class and in the exterior of it                        
#   |                -public functions                                   |
#   |                                                                    |
#   |                                                                    |
#   |                       ___________________________                  |
#   |                      |  -private attributes      |                 |
#   |                      |  -private functions       |                 |
#   |                      |                           |    <<<----------|-------------- Accessible only in the interior of the class 
#   |                      |                           |                 |
#   |                      |___________________________|                 |
#   |                                                                    |
#   |                                                                    |
#   |                                                                    |
#   |                                                                    |
#   |                                                                    |
#   |                                                                    |
#   |____________________________________________________________________|



# Exemple 

class University():
    def __init__(self, name, location):
        #intern attribute _
        self._name = name 
        #private attribute __
        self.__location = location # _NAMECLASS__location (the __location is hidden in the name of the class) 

    def getLocation(self):
        return self.__location
    
    def setLocation(self, new_location):
        if type(new_location) == str and new_location in ["Paris","Budapest","Viena"]:
            self.__location == new_location  


#making my object 
uni = University("ASE", "Bucharest")

# printing my name attribute from my object 
print(uni.name)   # output -> ase


# I acess my location through a method(function) not an attribute 
print(uni.getLocation()) # output ---> Bucharest 


print(uni.setLocation("Paris"))




# Exemple of get() and set() {getter and setter}


class University():
    def __init__(self, name, location):
        #intern attribute _
        self.name = name 
        #private attribute __
        self.__location = location # _NAMECLASS__location (the __location is hidden in the name of the class) 

    def getLocation(self):
        return self.__location
    
    def setLocation(self, new_location):
        if type(new_location) == str and new_location in ["Paris","Budapest","Viena"]:
            self.__location == new_location  
            return new_location
        else:
            print("we do not have the location")
    



#making my object 
uni = University("Harvard", "Bucharest")


# printing my name attribute from my object 
print(uni.name)   # output -> ase



# I acess my location through a method(function) not an attribute 
print(uni.getLocation()) # output ---> Bucharest 


# We access the method to change our location 
print(uni.setLocation("Paris"))
uni.getLocation()  # output ----> Paris 



# Interactions between Classes 


class Student():
    def __init__(self, name, age):
        self.name = name 
        self.age = age 


class Professor():
    def __init__(self, name, age):
        self.name = name 
        self.age = age 

    

ob1 = Student("Silviu", 31)

ob2 = Professor("Silviu", 31)


print(type(ob1)) # <class '__main__.Student'>
print(type(ob2)) # <class '__main__.Professor'>

print(isinstance(ob1, Student)) # True 
print(isinstance(ob2, Student)) # False 

# NOTE isinstance() is a built in function ,that returns True or Flase if the object is instance of a class 
# isinstance() takes 2 parameters the object and the class  
# see the exemple for reference 



# Static variables 

# Methods and static variables belong strictly to the class() not the Object 
# They do not need the creation of an object to exist, they exist at a class level 
# They can be defined as [] 



class Student():
    STUDENT_TYPE = ["Python", "JavaScript", "WebDesign", "MySQL"] # It only lives at a class level 
    def __init__(self, name, age, type):
        self.name = name 
        self.age = age 
        if (not type in Student.STUDENT_TYPE):            # I check if my DATA_TYPE is in my [Student.STUDENT_TYPE]
            raise ValueError(f"{type} is not valid type") # If not WE CATCH THE ERROR and output our ERROR
        else:
            self.type = type 




s1 = Student("Maria", 25, "Python")
s2 = Student("Maria", 25, "Rust") # The ValueError will be raised here 


# print(Student.STUDENT_TYPE) # I call with the name of the class in front
# Exercise 

# Create a deposit class() for the storage of food
# The deposit will contain types of food and the max capacity 


class Deposit():
    TYPES_OF_FOOD = ["MEAT", "CHEESE", "BIO", "PANTRY", "VEGETABLES"]     # static variables 
    def __init__(self, amount, type_of_food):                             # __init__
        self.__amount = amount                                            # __private amount 
        if (not type_of_food  in Deposit.TYPES_OF_FOOD):                  # Check my TYPES_OF_FOOD to be in my []
            raise ValueError(f"{type_of_food} is not in TYPES_OF_FOOD")   # treat ERROR
        else:
            self.type_of_food = type_of_food            





#  Decorators
#  @classmethod and @staticmethod 

# @classmethod	                                                                          @staticmethod
# Declares a class method.	                                                              Declares a static method.
# It can access class attributes, BUT NOT THE INSTANCE ATTRIBUTES 	                      It cannot access either class attributes or instance attributes.
# It can be called using the ClassName.MethodName() or object.MethodName().	              It can be called using the ClassName.MethodName() or object.MethodName().
# It can be used to declare a factory method that returns objects of the class.	          It cannot return an object of the class.



# Decorators, they represent an extension to the behavior of a function in the time of execution 
# They can be used on global functions as well as methods inside a class 
# exemple 

class Scholar():
    STATIC_LIST = ["YEAR_1, YEAR_2, YEAR_3"]
    def __init__(self,name,age):
        self.name = name 
        self.age = age 

    @classmethod                # <-- decorator
    def getstudenttype(cls):
        return cls.STATIC_LIST

print(Scholar.getstudenttype()) # without the decorator I cannot call the function 


# Simple exemple 

def my_decorator(func):                          # making a decorator 
    print("called decorator")                    # the added information     
    return func                                  # returning the func execution + the added information 

@my_decorator                   # applying it 
def myfunction(a,b):
    return a + b


myfunction(5,6) # called decorator

print(myfunction(7,8))     # called decorator
                           # 15

# Decorators take functions as a parameter and bring new behavior



# With decorators I can change the complet functionality of a method(function)
def my_decorator(func):                           # I define my decorator, with a func as a parameter 
    def rewrite(*args):                           # Inside my_decorator I rewrite the function passed
        return ("result is" + str(func(*args)))   # return my result, I need str to convert it
    return rewrite                                # return my function 


@my_decorator                                  # I decorate the function that I want to add functionality 
def my_func(a,b):
    return a + b


print(my_func(3,4))          # result is7    


def my_second_decorator(func):                             # I define my decorator with a function as a parameter 
    def rewrite(*args, **kargs):                           # I define another function inside and I Pass [] and {}
        return ("result is" + str(func(sum(args), 0)))     # I return str(function passed(summed(arguments), and 0 for {}))
    return rewrite                                         # I return my function 

@my_second_decorator                                       # I decorate my function 
def my_func2(a,b):           
    return a + b


print(my_func2(4,5,5,6))  # result is 20 //// everythin is inserted into a [] and summed 



# classmethods @classmethods 

class Student:
    name = 'unknown'        # class attribute
    def __init__(self):
        self.age = 20       # instance attribute

    @classmethod            # the decorator @classmethod makes my method a class method called by cls
    def tostring(cls):
        print('Student Class Attributes: name=',cls.name)


Student.name = "Radu"       # I give my class.name the class attribute "radu" 
Student().tostring()        # I call my CLASS METHOD



class Student:
    
    def __init__(self, name, age):
        self.name = name              # instance attribute
        self.age = age                # instance attribute
 
    @classmethod                      # we make our method a class method 
    def getobject(cls):
        return cls("Radu", 24)        # we return cls(name, age)


std = Student.getobject()            # we make our object directly contacting our classmethod
print(std.name)                      # radu
print(std.age)                       # 24 



# Exercise 

# Make a class Bill() that represents the cost of energy 
# attributes : consumation(kWh), cost of a kWh and fix_cost of maintanance monthly 

# setter and getter 

# use the attributes to calculate the total cost of the bill 

# use __str__



class Bill():
    def __init__(self, kWh, cost, cost_of_1kWh, monthly_cost = 100):
        if type(kWh) == int:
            self.kWh = kWh
        else:
            print("the value will be assigned to 0 if you cannot enter integers, please restart")
            self.kWh = 0 

        cost = kWh * cost_of_1kWh + monthly_cost
        self.cost = cost


        self.cost_of_1kWh = cost_of_1kWh
        self.monthly_cost = monthly_cost
        
     
    def __str__(self):
        return f"kwh={self.kWh}, total cost = {self.cost}, cost of 1 kwh = {self.cost_of_1kWh}, monthly_cost = {self.monthly_cost} "


my_bill = Bill(10, 5, 5)
print(my_bill)



# Exercise 

# Create a class Rent() that represent the renting of a room with a fixed fee. The cost of the rooms is the same 
# for all the rooms but the cost can change in time

# Attributes: cost_of_rent// day , number_of_nights , tax_of_hotel (money / night_stayed)
# create a setter and a getter for the number of nights 
# check the attributes 
# use the attributes to calculate the cost of the trip 



class Rent():
    def __init__(self, nights, hotel_fee ,tax = 100 ):
        self.nights = nights
        self.hotel_fee = hotel_fee
        self.tax = tax

    def getter(self):
        return self.nights 

    def setter(self, new_nights):
        self.nights = new_nights
        return self.nights


    def check_out(self):
        self.hotel_fee *= self.nights + self.tax
        return self.hotel_fee        
        

    def __str__(self):
        return f"you have stayed {self.nights} nights the cost per night is {self.hotel_fee}"
    

    

holiday = Rent(10, 125)
print(holiday)


print(holiday.getter())
holiday.setter(5)


print(holiday.getter())
print(holiday)


print("total", holiday.check_out())



# Exercise 

# Create a class OysterCard() that represents the card of transportation in London
# Atributes are name, available_trips, available_credit 
# In case there is no name, set it to "Unknown"
# One trip costs 3 pounds 
# Create Methods for validation_by_credit, validation_by_trip, recharge_cfredit, recharge_trips 





class OysterCard():
    ONE_TRIP = 3
    def __init__(self, credit = 0, ticket = 0, name= "unknown"):
        self.name = name 
        self.credit = credit 
        self.ticket = ticket  
    
    def __str__(self):
        return f"name = {self.name}, tickets={self.ticket}, credits={self.credit}"
    
    
    def recharge(self, credit, ticket):
        self.credit += credit 
        self.ticket += ticket

    def validation(self):
        if self.ticket ==  0 :
            self.credit -= OysterCard.ONE_TRIP
        elif self.ticket >= 1:
            self.ticket -= 1
        else:
            return "you need to purchase credit or tickets"


card = OysterCard(10, 10)
print(card)   # name = unknown, tickets=10, credits=10

card.recharge(10,10)     
print(card)   # name = unknown, tickets=20, credits=20

card.validation()
print(card) 


# Exercise 

# For the class Child() with attributes: name, allowance, nino, number_of_kids 
# USE the cast operator to insert float and output str 
# USE the cast opeartor to insert str and output int 


class Children():
    def __init__(self, name, allowance, Nino, number_of_children):
        self.name = name
        self.allowance = allowance 
        if Nino == str(Nino):
            Nino = int(Nino)
            self.Nino = Nino 
        elif Nino == float(Nino):
            Nino = int(Nino)
            self.Nino = Nino 
        else:
            self.Nino = Nino 
        
        if number_of_children == str(number_of_children):
            number_of_children = float(number_of_children)
            self.number_of_children = number_of_children
        else:
            self.number_of_children = number_of_children

child = Children("Charles", 100, "100", "100" )

print(child.name, child.allowance, child.Nino, child.number_of_children)     





# Inheritance 

# Exercise 

# Create an program Library
# The program will show at the beginning a meniu with the following items 
# 1: new_book, 2 change_book, 3: delete_book, 4 new_listing, 5 exit_program 

# All books are kept in the memory 


class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author 

    def __str__(self):
        return f"title = {self.title}, author= {self.author}"


    # __eq__ is the overwrite of is equal ==
    # we change the behavior of equal == 
    def __eq__(self, other):                                             # the computer doesnt know how to compare values of the same objects, the only know the address i memory of the object
        if self.title == other.title and self.author == other.author:    # the build in function __eq__ can compare the separate values from the address
            return True
        else:
            return False                                                 # The key here is comparation, the build in method can have 2 objects that for exemple, have different auhthors but the title are the same 




class Library():
    def __init__(self, books = []):
        self.books = books
    
    def __str__(self):
        self.description = f"Library with {len(self.books)} books: "     # I format my string with the number of books, self.descripiton  becomes iterable 
        for book in self.books:
            self.description += f"{book}"                               # I iterate through them and add formated string of the{book}
        return self.description                                         # I rerturn the description with every book 

    def list_all_books(self):                                           # Method to list all my books
        for book in self.books:
            print(book)

    def add_book(self, Book):
        self.books.append(Book)                                          # I .append BECAUSE its a LIST 
        return self.books

    # the more adavnced method                                                      
    def delete_book(self, Book):                                                       
        for index, item in enumerate(self.books):                                     # I iterate through the indexes of the list[books]                   
            if Book == item:                        
                print(f"I have found the book that needs deleted: {Book}")            
                self.books.pop(index)


         # the easy method to remove the book specified, second method 

        '''def delete_book(self, Book, decision):                                             # Decision(true or flase)  
        for item in self.books:                                                               # Iterate through my books 
            if Book == item:                        
                print(f"I have found the book that needs deleted: {Book}")                    # print(the book )
                if decision == True:                                                          # if i Confirm the book is removed from list, else continue 
                    self.books.remove(item)
                else:
                    continue'''

    def change_book(self, Book, new_title):                                                # similar as in delete_book()
        for index, item in enumerate(self.books):                                          # I find the index of the book 
            if Book == item:                                                
                print(f"this si the book that will be changed {Book}")               
                print(f"the book {item.title} was change to {new_title}")                  
                item.title = new_title                                                     # item.title change to new_title
                self.books[index] = item                                                   # i change the title 
  

Book1 = Book("Dracula", "Stocker")  
Book2 = Book("Ion", "Rebreanu")
Book3 = Book("Matreyi","Mircea Eliade")
Book3.author = "Mircea Eliade2"          # directly modifying parameters 


print(Book1) # title = Dracula, author= Stocker
print(Book2) # title = Ion, author= Rebreanu
print(Book3) # title = Matreyi, author= Mircea Eliade 



My_Library= Library([Book1, Book2]) #I pass my class to another class 
My_Library.add_book(Book3) #    I add my BOOK 
print(My_Library) # My number of Books Is Now 3 

My_Library.list_all_books()   # I print all my books

# print for first method of deleting  
print(My_Library)

My_Library.delete_book(Book2)
print(My_Library)


# print from second method of deleting 
# my delete.method second version 
'''print(My_Library)
My_Library.delete_book(Book1, True)
print(My_Library)

My_Library.delete_book(Book2, True)
print(My_Library)

My_Library.add_book(Book3)
print(My_Library)'''


My_Library.change_book(Book1, "Varcolac")   # I chenage the nameof the Book1 
print(My_Library)






#NOTE#####################################################################################
# BEHAVIOR                                                                               #
#                                                                                        #
# The Cat HAS A : name, fur, eyes etc (ATTRIBUTES)                                       #                                      
#                                                                                        #
# The CAT DOES : sleeps, eats, talks etc ( METHODS / FUNCTIONS)                          #                                                    
#                                                                                        #
# The CAT IS A MAMMMAL(Inheritance) She Inherits properties from another class()         #                                                                     
#                                                                                        #
#                                                                                        #
##########################################################################################


    
# Inhertiance Exercise 
# Author, Unknow Author, Book, Roman, 

class Author():
    NATIONALITY = ["GB", "RO", "US", "IT", "DN", "DE"]
    def __init__(self, name, nationality):
        self.name = name 
        if nationality in Author.NATIONALITY: 
            self.nationality = nationality 
        else:
            self.nationality = " Unknown"

    
    def __str__(self):
        return f"author with name{self.name} and nationality{self.nationality}"

    
class UnknownAuthor(Author):
    def __init__(self):
        super().__init__("unknown", "unknown")

class MultipleAuthor(Author):
    def __init__(self, name, nationality):
        super().__init__(name, nationality)


            
class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author 

    def __str__(self):
        return f"title = {self.title}, author= {self.author}"


    # __eq__ is the overwrite of is equal ==
    # we change the behavior of equal == 
    def __eq__(self, other):                                             # the computer doesnt know how to compare values of the same objects, the only know the address i memory of the object
        if self.title == other.title and self.author == other.author:    # the build in function __eq__ can compare the separate values from the address
            return True
        else:
            return False                                                 # The key here is comparation, the build in method can have 2 objects that for exemple, have different auhthors but the title are the same 

class Roman(Book):
    def __init__(self, title, author, volume = 1):
        super().__init__(title, author)
        self.volume = volume 





class Library():
    def __init__(self, books = []):
        self.books = books
    
    def __str__(self):
        self.description = f"Library with {len(self.books)} books: "     # I format my string with the number of books, self.descripiton  becomes iterable 
        for book in self.books:
            self.description += f"{book}"                               # I iterate through them and add formated string of the{book}
        return self.description                                         # I rerturn the description with every book 

    def list_all_books(self):                                           # Method to list all my books
        for book in self.books:
            print(book)

    def add_book(self, Book):
        self.books.append(Book)                                          # I .append BECAUSE its a LIST 
        return self.books

    # the more adavnced method                                                      
    def delete_book(self, Book):                                                       
        for index, item in enumerate(self.books):                                     # I iterate through the indexes of the list[books]                   
            if Book == item:                        
                print(f"I have found the book that needs deleted: {Book}")            
                self.books.pop(index)


         # the easy method to remove the book specified, second method 

        '''def delete_book(self, Book, decision):                                             # Decision(true or flase)  
        for item in self.books:                                                               # Iterate through my books 
            if Book == item:                        
                print(f"I have found the book that needs deleted: {Book}")                    # print(the book )
                if decision == True:                                                          # if i Confirm the book is removed from list, else continue 
                    self.books.remove(item)
                else:
                    continue'''

    def change_book(self, Book, new_title):                                                # similar as in delete_book()
        for index, item in enumerate(self.books):                                          # I find the index of the book 
            if Book == item:                                                
                print(f"this si the book that will be changed {Book}")               
                print(f"the book {item.title} was change to {new_title}")                  
                item.title = new_title                                                     # item.title change to new_title
                self.books[index] = item                                                   # i change the title 
  





unknown_author = UnknownAuthor()
print(unknown_author)
author1 = Author("Stocker", "Kilngon")
print(author1)

Book1 = Book("Dracula", author1)  
Book2 = Book("Ion", "Rebreanu")
Book3 = Book("Matreyi","Mircea Eliade")
Book3.author = "Mircea Eliade2"          # directly modifying parameters 


print(Book1) # title = Dracula, author= Stocker
print(Book2) # title = Ion, author= Rebreanu
print(Book3) # title = Matreyi, author= Mircea Eliade 



My_Library= Library([Book1, Book2]) #I pass my class to another class 
My_Library.add_book(Book3) #    I add my BOOK 
print(My_Library) # My number of Books Is Now 3 

My_Library.list_all_books()   # I print all my books

# print for first method of deleting  
print(My_Library)

My_Library.delete_book(Book2)
print(My_Library)


# print from second method of deleting 
# my delete.method second version 
'''print(My_Library)
My_Library.delete_book(Book1, True)
print(My_Library)

My_Library.delete_book(Book2, True)
print(My_Library)

My_Library.add_book(Book3)
print(My_Library)'''


My_Library.change_book(Book1, "Varcolac")   # I change the name of the Book1 
print(My_Library)



    
# POLYMORPHISM

# I can call the same method from a different Object 

# Exemple of Polymorphism 
# I can have multiple implentations for different objects 


class Test():
    def __init__(self, time, grade):
        self.time = time 
        self.grade = grade 
    
    def __str__(self):
        return f"time = {self.time}, grade = {self.grade}"

    def show(self):                                 # For my specific Object I call my show()method 
        print("Show obj test from Test")


class Test2(Test):
    def __init__(self,time,grade):
        super().__init__(time,grade)
    
    def __str__(self):
        return f" i am from test2 time = {self.time}, grade = {self.grade}"
    
    def show(self):                                 # For my specific Object I call my show()method 
        print("Show obj test2 ")



def call_show(obj):                                # I define a GLOBAL function that takes a s parameter my (obj) 
    obj.show()                                     # the function calls my show method from every class i define it 


test = Test(10,5)
test2 = Test2(4,6)

call_show(test)                                # Show obiectul test from Test
call_show(test2)                               # Show obiectul test2 


# If my second show() method is not defined , The second object (test2) will inherit the show method 

# OUTPUT --->

class Test():
    def __init__(self, time, grade):
        self.time = time 
        self.grade = grade 
    
    def __str__(self):
        return f"time = {self.time}, grade = {self.grade}"

    def show(self):                                
        print("Show obj test from Test")


class Test2(Test):
    def __init__(self,time,grade):
        super().__init__(time,grade)
    
    def __str__(self):
        return f" i am from tes2 time = {self.time}, grade = {self.grade}"
    


def call_show(obj):                    # I make a method at both class levels to call show from Test, and Test2 because it is inherited             
    obj.show()                                    

test = Test(10,5)
test2 = Test2(4,6)

call_show(test)                                                        # Show obiectul test from Test
call_show(test2)      # this is inherited from test              ------> Show obiectul test from Test



# SIMPLE EXEMPLE of DIAMOND INHERITANCE  

# Method resolution order: MRO 
# In Python, every class whether built-in or user-defined is derived from the object class and all the objects are instances of the class object. Hence, the object class is the base class for all the other classes.
# In the case of multiple inheritance, a given attribute is first searched in the current class if it’s not found then it’s searched in the parent classes. The parent classes are searched in a left-right fashion and each class is searched once.
# If we see the above example then the order of search for the attributes will be Derived, Base1, Base2, object. The order that is followed is known as a linearization of the class Derived and this order is found out using a set of rules called Method Resolution Order (MRO).

# To view the MRO of a class: 
 
# Use the mro() method, it returns a list 
# Class4.mro()

# or the _mro_ attribute, it returns a tuple 
# Eg. Class4.__mro__ 


# Python program to demonstrate
# super() and real inheritance of methods 

class Class1:
	def m(self):
		print("In Class1")

class Class2(Class1):
	def m(self):
		print("In Class2")
		super().m()

class Class3(Class1):
	def m(self):
		print("In Class3")
		super().m()

class Class4(Class3,Class2):
	def m(self):
		print("In Class4")
		super().m()
	
obj = Class4()
obj.m()


print(Class4.mro())  

print(Class4.__mro__ )   # __mro__ built in method to see the path of inheritance






# Exercise // abstract method and Diamond inheritance 

# Define classs Engine(), with the attributes: seial_number, power, number_km
# add class ElectricEngine and GasolineEngine with the attributes battery(percentage of drained at 1 km)
# and the consumbtion in liters at 100 km 

import abc # abstract class 
# abstract class create a commun fucntionality between classes but it is not callable as an object , because it is abstract
# abstarct class and methods need to be written for further functionality in the program, you can see them as "hard coded startting points, which are fundamentaly needed"


class Engine(abc.ABC):                                         # passing the default abstract class, Engine becomes abstract class
    def __init__(self, serial_number, power, number_km):
        self.serial_number = serial_number
        self.power = power
        self.number_km = number_km
   
    @abc.abstractmethod                                        # methods become as well abstract, to use them you have to rewrite them 
    def warning():                                             # warning() is a method that needs to be present in all Engines 
        pass

    @abc.abstractmethod
    def my_meth0d_that_need_to_be_present_in_all_objects(self):    # the fucntion does not need to return somthing becuase its abstract, but in inheritance the function has to be present 
        pass



class ElectriEngine(Engine):
    def __init__(self, serial_number, power, number_km, battery):
        super().__init__(serial_number, power, number_km)
        self.battery = battery 
    
    def warning(self):
        if self.battery < 10:
            return f" battery is low {self.battery}"
        else:
            return f"battery value is {self.battery}"

    def my_meth0d_that_need_to_be_present_in_all_objects(self):
        pass


    def power_consumption(self):
        self.number_km = self.power * self.battery 
        return self.number_km

    def __str__(self):
        return f"Electric engine --- > SERIAL NUMBER = {self.serial_number}, POWER = {self.power}, NUMBER OF KM = {self.number_km}, BATTERY = {self.battery}"    


class GasolineEngine(Engine):
    def __init__(self, serial_number, power, number_km, consumption):
        super().__init__(serial_number, power, number_km)
        self.consumption = consumption
    
    def warning(self):
        if self.consumption < 10:
            return f" battery is low {self.battery}, please recharge "
        else:
            return f"battery value is {self.battery}"

    def my_meth0d_that_need_to_be_present_in_all_objects(self):
        pass

    def power_consumption(self):
        self.number_km = self.power * self.consumption
        return f"power consumption is {self.number_km}"


    def __str__(self):
      return f" Gasoline engine -- > SERIAL NUMBER = {self.serial_number}, POWER = {self.power}, NUMBER OF KM = {self.number_km}, CONSUMPTION = {self.consumption}"  
        


# Diamond Inheritance 
class HybridEngine(GasolineEngine, ElectriEngine):
    def __init__(self, serial_number, power, number_km, battery, consumption):
        super(GasolineEngine, self).__init__(serial_number, power, number_km)
        super(ElectriEngine, self).__init__(power, number_km)
        self.consumption = consumption
        self.battery = battery 
        
    def warning(self):
        if self.consumption < 10 or self.battery < 10 :
            return f" battery is low {self.battery} or you do not have gas {self.consumption} please recharge "
        else:
            return f"battery value is {self.battery}good, and consumption is good {self.consumption} "

    def power_consumption(self):
        self.number_km = self.power * self.consumption + self.power * self.consumption
        return self.number_km

    def my_meth0d_that_need_to_be_present_in_all_objects(self):
        pass

    def __str__(self):
        return f" Hybrid engine -- > SERIAL NUMBER = {self.serial_number}, POWER = {self.power}, NUMBER OF KM = {self.number_km}, BATTERY = {self.battery}" 



# gasoline = GasolineEngine("101", 100, 1000, 7)
# print(dir(gasoline))                                     # dir() is for introspection so i can see my classes in the back that are being called WITH DIR YOU CAN SEE THE REFLECTIUON OF THE CLASS 

# print(gasoline)     #  serial number = 101 ,power = 100 ,number of km = 1000,consumption =  7 
# __mro__ built in method to see the path of inheritance


electricEngine = ElectriEngine("1001", 100, 100, 10)
print(electricEngine) # SERIAL NUMBER = 1001, POWER = 100, NUMBER OF KM = 100, BATTERY = 10
print(electricEngine.power_consumption())



gasolineEngine = GasolineEngine("1002", 200, 200, 15)
print(gasolineEngine)
print(gasolineEngine.power_consumption())


hybridEngine = HybridEngine("1003", 225, 230, 20, 5)
print(hybridEngine)
print(hybridEngine.power_consumption())





# Exercise Team 

# create the Team, Score and Match classes. The Team class contains the field: team_name.
# The Match class contains the fields: home (the object of the Team class), away (the object of the Team class), minutes (the current minute of the match) and score (the current result).
# The Score class contains the fields: home and away, in which the result of the match is found
# The match ends when the 90 minutes expire Silviu Ojog
# The Match class contains the start method, which starts the match.
# During the match, the results are changed to a random choice and displayed at the exit.

# Add a list of players []


import time 
import random 

class Team():                                                             # we create our class Team()
    def __init__(self,team_name, squad):
        self.team_name = team_name 
        self._squad = squad 

    def first_squad(self):                                               # we create our method first squad of 11 players 
        return self._squad[:11]
    
    def __str__(self):
        return f" {self.team_name}"


class Score():
    def __init__(self, home_goals= 0, away_goals = 0):                   # we define our class Score(0,0) we make the attributes internal 
        self.__home_goals = home_goals
        self.__away_goals = away_goals
        
    
    def goal_from_hometeam(self):                                       # home team scores 
        self.__home_goals += 1

    def goal_from_awayteam(self):
        self.__away_goals += 1

    def __str__(self):
        return f"  {self.__home_goals} - {self.__away_goals}"   
  

class Match():
    def __init__(self, home_team, away_team):
        self.home_team = home_team 
        self.away_team = away_team 
        self.score = Score()                     # passing a class as an attributes makes the class Score direct callable
        self._is_started = False                 # Flags: The game did not begin 
        self._is_ended = False                   # Flags: The game did not end 
        self.duration = 90                       # the duration of the game is seconds 

 
    def start_game(self):                                             # method to start game 
        self._is_started = True                                       # true 
        self.the_game_has_started = time.time()                       # we attribute current time to a our variable 
        print(self)
        self.game_dynamics()                                          # we call our function for starting the "dynamics of the game"

    def choose_hiter(self,team):                                     
        return team.first_squad()[random.randint(0,10)]               # we choose who we want to make the goal from our list -- we actuall call opur function from team that returns our list where we insert random valuea

        


    def game_dynamics(self):
        if self.the_game_has_started+self.duration > time.time():            # if the time is bigger then the current game
            time.sleep(5)                                                    # every 5 seconds the hometeam scores a goal 
            self.score.goal_from_hometeam()
            print(self)
            print("the goal was from", self.choose_hiter(self.home_team))   # we choose from our list who was the goal from 
            self.game_dynamics()                                            # we call the same function. creating a loop 
        else:
            self.end_game()                                                 # the game is ended , we call our endgame function/method 
        print(self)

    def end_game(self):                     
        self._is_ended = True

  

    def __str__(self):
        return f'''  {self.home_team}   VS {self.away_team}
        {self.score}
                            
        '''



home = Team("Milan", ["P1", "P2", "P3", "P4","P5","P6","P7","P8","P9","P10","P11"])       # we create our teams 
away = Team("Juventus",["P1", "P2", "P3", "P4","P5","P6","P7","P8","P9","P10","P11"])

game = Match(home, away)    # we pass 2 objects to our class Match 

'''print(game)                # we print 

game.score.goal_from_hometeam()  # I need to call the score that is attributed to class Score 
print(game)  # 1-0

game.score.goal_from_awayteam()  # I need to call the score that is attributed to class Score 
print(game) # 1-1'''

game.start_game()




# TRY EXCEPT 

# try 
# except 
# finnaly


#exemple 
x = input("enter a number")

try:                                 # we can try values
    x = int(x)
    x += 4
except:                                 # we can except the error 
    print("a existat o eroare")         # treat it/ show it 
    print(f" {x} <-- is an error")
finally:
    print(x)                                            # we end here in any case 
    print("we are here even there is an error or not ")

 


#exemple2
try:
    x = input("enter x ")
    y = input("enter y ")
    x, y = int(x), int(y)
    z = x/y
except ZeroDivisionError:                    # we except ZeroDivisionError
    print("0 is not posible in division")
    z = 0                                    # we hardcode or answer 
finally:
    print(z)




#exemple3 
try:
    x = input("enter x")
    y = input("enter y")
    x, y = int(x), int(y)
except ValueError as err :
    print(err)
    z = 0 
except ZeroDivisionError:
    print(f"the second number cannot be {y}")
    z = 0
finally:
    print(z)



# Exercise 

# Create a program that adds numbers, asking continuously for input first_number and second_number
# if the user send the wrong value the computer prompts a message saying 'wrong values" and asks for a new entry 
# the computer should not retake the operation from the start but begin a new entry of values





while 1:
    try:
        x = int(input("enter nr 1--->"))
        y = int(input("enter nr 2--->"))
        z = x / y 
    except ZeroDivisionError:
        print("division by 0 not possible")
        z = 0
    except ValueError:
        print("value erorr")
        z = 0 
    finally:
        print(z)

# you can also treat the error 

while 1:
    try:
        x = int(input("enter nr 1--->"))
        y = int(input("enter nr 2--->"))
        z = x / y 
    except ZeroDivisionError as err:
        print(err)
        z = 0
    except ValueError as err2:
        print(err2)
        z = 0 
    finally:
        print(z)



# Same exemple but with indexes 

while 1:
    try:
        x = [1,2,3]
        y = int(input("enter index"))
        x[y]
    except IndexError:
        print("your index is out of range ")
    else:
        print("good job")





# Practical exemple of custom Exception()  with the use of raise()


def divide(a,b):         
    if b==0:
        return 0
    if a>10 or b>10:                            # condition      
        raise ArithmeticError("value is > 10")  # my custom Exception()
    else:
        return a + b 

print(divide(14,1))




# Exemple of use case in a class

class Student:
    def __init__(self, name, age ):
        self.name = name 
        if age < 16:
            raise Exception("YOU HAVE TO BE OVER 16")
        else:
            self.age = age 
    def __str__(self):
        return f"name = {self.name}, age = {self.age}"



my_student_object = Student("Radu", 12)
print(my_student_object)




# The class method is to inherit the exception from a class() and raise my class(exception)
# see exemple below 



class MinimumAgeException(Exception):                       # we create our exception class 
    def __str__(self):
        return "minimum age is 10"


class Student:                                              # we define our class use case 
    def __init__(self, name, age ):
        self.name = name 
        if age < 16:
            raise MinimumAgeException()                     # we call our class 
        else:
            self.age = age 
    def __str__(self):
        return f"name = {self.name}, age = {self.age}"



try:                                                         # we try our values 
    my_student_object = Student("Radu", 12)
except MinimumAgeException as identifier:                    # we except as indentifier 
    print("the exceptiuon is = ",identifier)




# make a program for a simple check of firstname, lastname, id and email 

import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'     # we import regex/ we can search it on the web 

class InvalidIdException(Exception):                               # we create our exceptions 
    def __str__(self):
        return "Id has to be smaller than 100"

class InvalidNameException(Exception):                        
    def __str__(self):
        return "number is to low"

class InvalidEmailException(Exception):
    def __str__(self):
        return "wrong email"

class User:                                                
    def __init__(self, id, firstName, lastName, email):
        if id < 100:                                             # we check if its lower than 100 
            self.id = id
        else:
            raise InvalidIdException()                          # we raise our exceptions 
        if len(lastName) > 1 and len(firstName) > 1:            
            self.firstName = firstName
            self.lastName = lastName
        else:
            raise InvalidNameException()

        if (re.fullmatch(regex, email)):                         # built in function of regex 
            self.email = email
        else:
            raise InvalidEmailException()
    
    def __str__(self):
        return f"firstname = {self.firstName},lastname = {self.lastName}, email = {self.email}, id = {self.id}"


u1 = User(99, "Xi", "Ji", "radu243ivanov@gmail.com")
print(u1)





# @property // @getter and @setter // @abstractmethod 


import abc


class Product:
    CONTOR = 1000
    def __init__(self, name, description, price, discount):
        self._name = name 
        self.description = description 
        self.price = price 
        self.discount = discount 
    
    def __str__(self):
        return f" name ={self.name}, description = {self.description}, price={self.price}, discount={self.discount}"

    @property                                            # property 
    def name(self):
        return self._name

    @name.setter                                         # we can create our own decorator and set it 
    def name(self, new_value):
        if len(new_value) < 3:
            return
        self._name = new_value 


    @abc.abstractmethod
    def discount(self):
        pass


class Jeans(Product):
    def discount(self):
        return 0 


class Tshirt(Product):
    def discount(self):
        return 0 


if __name__ == "__main__":
    p1 = Product("Jeans", "jeans-description", 100, 0)
    print(p1)
    p1.name = "different_jeans"
    print(p1)

    
    


# LAMBDA // REDUCE // FILTER // MAP 

from functools import reduce

# reduce 
listy = [5, 9, 10, 12, 15]

suma = reduce((lambda x,y: x+y), listy) # we use lambda for fast usecases 
print(suma) # it will print 51



# filter 
nums = [5, 10, 23, 64, 42, 53, 93, 2, 0, -14, 6, -22, -13]

odd = filter(lambda p: p%2 != 0, nums)
even = filter(lambda p: p%2 == 0, nums)

print(f"the odd numbers are = {list(odd)}") # the odd numbers are = [5, 23, 53, 93, -13]
print(f"the even numbers are = {list(even)}") # the even numbers are = [10, 64, 42, 2, 0, -14, 6, -22]



# map 
list_1 = [1,2,3,4]
list_2 = [5,6,7,8]

mapping = map((lambda a,b: a+b),list_1, list_2) 
print(f" the sum of numbers in list1 and list2 is = {list(mapping)}") # the sum of numbers is = [6, 8, 10, 12]