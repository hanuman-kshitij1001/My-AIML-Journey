# So Fist of All What Is Decorator
# In Python Decorator is Function that Recived Another function as an input and add some functionailites(Decoration) to it and return it
# This can happen only because python functions are 1st class citizens.
# There are 2 types of decorators available in python
# 1: Built in decorators like @staticmethod, @classmethod, @abstractmethod and @property etc
# Note Jitne Bhi builtin Hote hai He Is Starts with "@" always 
# 2: User defined decorators that we programmers can create according to our needs

# Python are 1st class function
# First-class function ka matlab hai ki Python me functions ko bhi ek “object” ki tarah treat kiya jaata hai.
# Matlab: function ko variable me assign kar sakte ho, function ko argument ke roop me pass kar sakte ho, aur function ko return bhi kar sakte ho.

def modify(func,num):  
  # Yaha modify() ek function hai jo dusre function ko input ke roop me accept karta hai.
  # func parameter ek function hoga.
  # num parameter ek number hoga.
  
  return func(num)   # return func(num) ka matlab hai: jo function tumne diya hai, usko num ke saath call karo

def square(num):  # square() ek function hai jo number ka square return karta hai.
  return num**2

print(modify(square,2))


# simple example

def my_decorator(func):
  def wrapper():
    print("*************")
    func()
    print("*************")
  return wrapper

def hello():
  print("hello")

def display():
  print("Kshitij-Tiwari")

a = my_decorator(hello)
a()

b = my_decorator(display)
b()


# Ab Tum Yaha Sikhoge ki Mai Kaise @ ka Use karke COde ko Chota bana Sakta hun

def my_decorator(func):
  def wrapper():
    print("*****************")
    hello()
    print("*****************")
    return wrapper

@my_decorator   
def hello():
  print('Hello')

hello()  # yaha Maine Simple Hello Call KArke Pura COde excute kara liya 
# @my_decorator ka matlab
#  Jab tum @my_decorator likhte ho hello() ke upar, iska matlab hai:
#  hello = my_decorator(hello)
#  Matlab: hello function ko my_decorator ke andar pass kar diya gaya, aur jo wrapper return hua usse hello replace kar diya gaya


# @my_decorator ek shortcut hai jo function ko decorator ke andar pass kar deta hai.
# Tumhe manually likhne ki zarurat nahi: ese  hello = my_decorator(hello)  
# Ye automatically ho jaata hai jab tum @ syntax use karte ho.

# Note : Matlab @ lagane se koi “extra bada kaam” nahi hota — bas ek shortcut hai jo function ko decorator ke andar wrap kar deta hai.



# anything meaningful? 
# Yha mai Ek Code likh raha hun Jo Ki Mai code excution ka Time nikane wala hun bhai theek hai na 

import time

def timer(func):
  def wrapper(*args):
    start = time.time() # ye Real Time Fetch Karta hai 
    func(*args)
    print('time take by ', func.__name__,time.time()-start,'secs')
  return wrapper

@timer
def hello():
  print('Hello Kshitij')
  time.sleep(2)

@timer
def square(num):
  time.sleep(1)
  print(num**2)

@timer
def power(a,b):
  print(a**b)

hello()
square(2)
power(2,3)


#  One last example -> decorators with arguments
@checkdt(int)
def square(num):
  print(num**2)