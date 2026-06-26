# Bahot Sare Function Hote hia 
# Sabkuch padhna yaad rakhna possible nahi hai 
# sabse  Jada Usse Hone wale function jo hia ML aur DS me Wo haam padhnge theek hai na 
# Ye sare Function Sare Maths ke hai 
# Note : np.round aur np.round.round mein bahut bada difference hai:
# np.round : Yaani decimal places round kar deta hai.
# np.round.round: 
import numpy as np
a = np.random.random((3,3))
b = np.round(a*100)
print(b)


#1: max/min/sum/product

print(np.max(b))
print(np.min(b))
print(np.sum(b))
print(np.prod(b))



#2: abhi tak Maine Kya kiya pure array ke andhar se jo minimum tha usse nikla 
# But ab Haam Ek Particular row me kon Sabse minimum hai usse nikal ne wale hai theek hai na 

# Note : 0 = col , 1 = row
print(np.max(b, axis=1))
print(np.min(b, axis=1))
print(np.sum(b, axis=1))
print(np.prod(b, axis=1))

# yaha haam Col Wise chalne wale hai Theek hai 
print(np.max(b, axis=0))
print(np.min(b, axis=0))
print(np.sum(b, axis=0))
print(np.prod(b, axis=0))


#@ Ab haam Yaha Se Static function Ke Traf Jane wale hai Theek hai Na 

#1; mean / median / std/ var

p = np.random.random((3,3))
q = np.round(a*100)

print(np.mean(q))
print(np.median(q))
print(np.std(q))
print(np.var(q))


#@ Now Move to Some Trignomatric Part 
# Apne Data Sciecnse Ke Entire Course me Trig no Ka Usse kabhi nahi karne wale hai 
print(np.sin(q))
print(np.cos(q))
print(np.tan(q))

# Note ye Do Avlable nahi  hai 
# print(np.cosec(q))
# print(np.cot(q))  use this>>  cot(x) = 1 / tan(x)  )R cot(x) = cos(x) / sin(x)




#@ Dot Product  >> imp

c = np.arange(12).reshape(3,4)
d = np.arange(12,24).reshape(4,3)
print(np.dot(c,d))

#@ # log and exponents
print(np.exp(q))
print(np.log(q))


#@ # round/floor/ceil
print(np.ceil(np.random.random((2,3))*100))
print(np.round(np.random.random((2,3))*100))  # Nearest integer.
print(np.floor(np.random.random((2,3))*100))  # Hamesha neeche wala integer.