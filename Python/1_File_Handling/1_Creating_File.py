f = open("Sample.txt", "w")
f.write("This Is A  Sample File And I Am Writing Some Text To It.")
f.close()

# File me 3 Kaam Hote hia Agr File Nahi Bani Hia TOh Usse Banne Ke Liye 
# f.write se banao 
# f.write se likho 
# f.close()


f = open("Sample.txt", "w")

f.write("""
Hello Bhai
Ye ek bada content hai
Hum multiple lines bhi likh sakte hain
Python file handling easy hai
""")


f.close()





f = open("2_Sample.txt", "w")
#write lines
L = ['hello\n','hi\n','how are you\n','I am fine']
f.writelines(L)
f.close()