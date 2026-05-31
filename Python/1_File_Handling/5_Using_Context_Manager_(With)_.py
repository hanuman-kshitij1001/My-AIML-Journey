# Using Context Manager (With) : ? >
# It's a good idea to close a file after usage as it will free up the resources
# If we dont close it, garbage collector would close it
# with keyword closes the file as soon as the usage is over


# Normal File Handling
# Agar tum file open karte ho bina with ke:
f = open("data.txt", "r")
content = f.read()
f.close()
# Yaha tumhe manually close() karna padta hai. Agar bhool gaye ya error aa gaya to file properly close nahi hogi.

# Context Manager (with)
# Agar tum with use karte ho:
with open("data.txt", "r") as f:
    content = f.read()
# Yaha with ensure karta hai ki file automatically close ho jaaye chahe error aaye ya na aaye.
# Matlab tumhe f.close() likhne ki zarurat hi nahi.

# Benefits:
# Automatic cleanup → file close ho jaati hai.
# Less code → close() likhne ki zarurat nahi.
# Safe → error aane par bhi resource release ho jaata hai.


# with open(...) as f: ka matlab
with open("data.txt", "r") as f:
    content = f.read()

# Yaha open("data.txt", "r") ek file object return karta hai.
# as f ka matlab hai: us file object ko ek nickname/variable de do jiska naam f hai.
# Matlab: ab tum f ke through us file ko access kar sakte ho (read, write, etc.).
# Matlab: with open(...) as f: ek shortcut hai jo file ko safely open karta hai aur usko ek variable (f) ke naam se refer karne deta hai.