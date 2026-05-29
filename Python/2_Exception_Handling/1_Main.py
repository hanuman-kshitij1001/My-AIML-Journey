with open('sample.txt', 'w') as f:
    f.write("File Is Created")
f.close()


try:
    with open("sample_1.txt", "r") as f:
        print(f.read())
except:
    print("Sorry File Is Not Found")


try:
    m = 5
    f = open('sample.txt','r')
    print(m)
    print(5/0)
except FileNotFoundError:
    print('file Not found')
except NameError:
    print('Variable not define')
except ZeroDivisionError:
    print("can't divide by 0")
except Exception as e:
    print(e)



# Else

try:
    f = open('sample.txt', 'r')
except FileNotFoundError:
    print('file nhi Mili')
except Exception:
    print('Kuch To Lafda hai ')
else:
    print(f.read())