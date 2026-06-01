# LEGB Rule Is Nothing This Is Rule For Variable Scope 


# local and global

# global var : A global variable is one that is defined outside of any function. It can be accessed throughout the entire program, and inside functions as well. If you want to modify it inside a function, you need to use the global keyword. 
x = 10  # global variable

def my_function():
    print(x)  # Accessing global variable
my_function()  # Output: 10


# Ex 2:
a = 20 # Global Varibale

def temp():
    b = 10  #local Var
    print(b)

temp()
print(a)

# Note : Python Always Start Runing From First line Not Main Yes You Idoms To Run Code from Main But you Always Rembaer COde Run From Main Bro 



# Topic 2 :
# local and global -> same name

a = 9   # This Is Called Global Variable 

def my_fun():
    a = 9   # This is Called Local Variable Done pf same name ass Global But Eska Kaam Andhr Hi Andhr Ho Raaa hia Toh Esse frak Nhai Padta ki Name Same Hai Ya Diffrent python Scop Ke hisab Se treat karta hai enhe Done   
    print(a)
my_fun()
print(a)



# Topic 3:
# local and global -> local does not have but global has

a = 2

def my_fun():
    print(a)  
    # sabse Pahele Ye Function a Ko Local me Search karega Agr Ye Local Me nahi ahi toh Global Search karega Yah Globaly Miil gaya Thats Why its Running and we get output 

my_fun()
print(a)

#Topic 4: 
# local and global -> editing global
# Matlb Kya mai Kis Varibale Ko Globle me Define Karke Local Se edit kar sakta hun ye dekhna hai yaha Waise Toh Eska Answer hai Ki Nahi Kar sakte hai
a = 3
def my_fun():
    a += 10
    print(a)

my_fun()
print(a)


# Topic 5:
# Haam Local se Global Variable Ko Edit kar sakte hai Bass Hame "Global(Ye galt hai Hai Bcz Of Capital G) not Capital G use "global""  key word use karna honga 

b = 16
def my_fun():
    global b 
    b += 19
    print(b)
my_fun()
print(b)


# Topic 6:
# local and global -> global created inside local
# Matlb Mai global Key Word Se Local Me ek Variable Bana Raha hun Aur Usse Globly Acess Karunga Done 

def my_fun():
    global p 
    p = 21
    print(p)
my_fun()
print(p)
sum = p+123
print(sum) # dekho mai Es Variable Ko Globly Handle ya Use kar pa raha hun 


# Topic 7:
# local and global -> function parameter is local

def temp(z):  # Kya tum Bata Sakte Ho Yaha fuction Ke Arg me Jo Varible Diya hai Ye Global Hai Ya Local Ans hai Local Ye baat Yad Rakhna hai 
  
  print(z) # local var

a = 5
temp(5)
print(a)
print(z)  # Ayr mai Esse Yaha Globla Me Print Karunga toh Ye Error Denga Hi bhai Kyu Ki maine ese global Nahi banaya hai aur Dursi Baat Ye Local Hia Gloabl me Excess nahi ho sakta hai



# Topic 8  # built-in scope
# Sabse Pahele TOh Ye Samjha Lo Ki Built In Scope Hota kya hai Theek hai na 
# Atually Jitne Bhi Pri define function hai Wo Sare ke sare Built in Scope ke andhar ate hai Samjha kya 
# Mai Ek Code se sare Built in Variable Nikal Sakta Hun 
# Code :  how to see all the built-ins

import builtins
print(dir(builtins))  # Ye Bahut Sare hai Lagfag 157 ke ass pass Aur ++


# Topic 9 
# renaming built-ins
L = [1,3,4,6]
print(max())   # YAHA PE MAINE PYTHON KE MAX BUILT IN FUCTION CALL KIYAH HAI 
def max():
    print('Hello')

print(max())  # YAHA PE MAIJNE aPNE MAX WALE FUNCTION KO CAL KIYA YAHA ERROR AYEGA KYU KIPYTHONE KO LAGEGA NA KIMAI BUILT IN CALLKAR RAHA HUN 
#TypeError: max() takes 0 positional arguments but 1 was given



# Topic 10
# Enclosing scope
# Enclosing scope ka matlab hai nested functions ke case me outer function ke variables ko access karna. Ye Python ke LEGB rule ka “E” part hai.
# Note:
# Local scope → current function ke andar ke variables.
# Enclosing scope → agar ek function ke andar dusra function likha hai, to inner function ke liye outer function ke variables “enclosing” scope me hote hain.
# Matlab: inner function apne outer function ke variables ko dekh sakta hai, use kar sakta hai.

def outer():
    a = 1
    def inner():
        print(a)
    inner()
    print('Out Function')

outer()
print("Main Program")

# out put
# 1
# outer function
# main program


# nonlocal keyword
def outer():
  a = 1
  def inner():
    nonlocal a
    a += 1
    print('inner',a)
  inner()
  print('outer',a)


outer()
print('main program')
# Out-Put Hai 
#inner 2
# outer 2
# main program