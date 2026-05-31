# reading from files
# -> using read()

f = open('1_sample.txt','r')
s = f.read()
print(s)
f.close()


# reading upto n chars
# Matlb Ye sari ya Puri Files ko Ek Sath Read nahi Karega Kuch Parta Upto n chracter tk hi read karega theek hai 
# code :

f = open("1_sample.txt", "r")
s = f.read(8)
print(s)   #> OutPut: I am Wri   > yah aSpace bhi Count ho jata hai
f.close()

# readline() -> to read line by line
f = open("1_sample.txt", "r")
print(f.readline(),end='')  # end ka matlb hia next line me mmat jao Jaha Ho wahi se start karo theek hai na 
print(f.readline(),end='')  # Line By line Content read karke print kar denga theek hai na bhai 


# reading entire using readline
f = open("1_sample.txt", "r")

while True:
    data = f.readline()
    if data == '':
        break
    else:
        print(data, end='')

f.close()