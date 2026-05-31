# tell()
# Ye batata hai ki file pointer abhi kis position pe hai.
# Jab tum file open karte ho aur read/write karte ho, ek invisible pointer hota hai jo file ke andar move karta hai.

f = open("data.txt", "r")
print(f.tell())   # 0 (start of file)
f.read(5)
print(f.tell())   # 5 (pointer moved after reading 5 chars)
f.close()
# Matlab: tell() tumhe current position (in bytes) return karta hai.

# seek(offset, whence)
# Ye pointer ko move karne ke liye use hota hai.
# Syntax: seek(offset, whence)
# offset → kitne bytes move karna hai
# whence → reference point (default 0)
# 0 → start of file
# 1 → current position
# 2 → end of file

f = open("data.txt", "r")
f.seek(0)        # start of file
print(f.read(5)) # first 5 chars

f.seek(0, 2)     # move to end of file
print(f.tell())  # position at end
f.close()



# Note: Ye dono tumhe file ke andar navigation control dete hain, jaise tum ek movie ke timeline pe forward/backward karte ho.