# Syntax : 
with open('file_name', 'mode') as f_ya_KuchBhiName_sakte_ho:
    # f.mode()
    # f.wite()
    # f.read()
    f_ya_KuchBhiName_sakte_ho.read()


# ab Dekho Agr tum Esse Khole bina Likhna Chalu karte ho toh Kuch esa error ayega bhai 

# f_ya_KuchBhiName_sakte_ho.write('hello')
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# /tmp/ipykernel_2240/375632407.py in <cell line: 0>()
# ----> 1 f.write('hello')

# ValueError: I/O operation on closed file.




# moving within a file -> 10 char then 10 char
with open('1_sample.txt','r') as f:
  print(f.read(10))
  print(f.read(10))
  print(f.read(10))
  print(f.read(10))
#           ^
# benefit? -> to load a big file in memory
big_L = ['hello world ' for i in range(1000)]
with open('big.txt','w') as f:
  f.writelines(big_L)


with open('big.txt','r') as f:

  chunk_size = 10

  while len(f.read(chunk_size)) > 0:
    print(f.read(chunk_size),end='***')
    f.read(chunk_size)


    