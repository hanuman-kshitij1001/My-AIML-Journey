
# seek and tell function
with open('sample.txt','r') as f:
  f.seek(15)  # ye Bata Rahi hai 15 charcter pe chale jao
  print(f.read(10))
  print(f.tell())  # kaha Ho usse batao 
  
  print(f.read(10))
  print(f.tell())


# seek during write
with open('sample.txt','w') as f:
  f.write('Hello')
  f.seek(0)
  f.write('Xa')