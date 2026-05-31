# case 2 - if the file is already present

#Step1: sabse Pahele Apko File Open karni hongi Hai TAbhi aap edit kar paoge theek 
f = open("1_sample.txt", "w")

#Step2: Ye Command Ye Write Kar sakte ho Existing File Ke Andhar
f.write("Hello This 1_Sample_txt_file write now I am Editing There Content")

#Step3: likhne Ke Baad Aap Esse Close karn ana Bhule warna Apka Data Loss ho sakta , Ya Koi Ake changes kar sakta hai
f.close()


# write multiline strings
f = open('sample1.txt','w')
f.write('hello world')
f.write('\nhow are you?')
f.close()


#Observation: Mai Ek Kaam Karta hun Ess File Ko Kholta hun aur Write karta hun kuch aur check akrunga kya esme jo data tha wo rahega ya delete ho jayega 
f = open("1_sample.txt", "w")
f.write("I am Writing Second Time To See THe Previous Content are still Is There or not ")
f.close()
# Maine Kya Observe Kiya Ki Dubra Write Karne se File Ka Existing Data Delite  ho gaya hai 
# So Es Problem Se bachne ke liye haame Likhan hai  w Ke jagha a what is a a is called append Maltb ye Last me apped kr denga theek hai na 

# Append Mode 
f = open('sample1.txt','a')
f.write('hello world')
f.write('\nhow are you?')
f.close()

# write lines
L = ['hello\n','hi\n','how are you\n','I am fine']

f = open('/content/temp/sample.txt','w')
f.writelines(L)
f.close()

