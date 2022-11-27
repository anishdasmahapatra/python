##Write a program to find the length of the string without using inbuilt function (len)**

s="Bangalore is good place"
_count=0

for word in s.split():
    _count+=1
print(_count)

#2. Write a program to reverse a string without using any inbuilt functions.**
d="weather is very cold here"
words=d.split()
for word in words:
    print (word[::-1])

#**3. Write a program to replace one string with another. e.g. "Hello World" replaces "World" with "Universe".**

s="Hello string"
d=s.replace("string","universe")
print(d)

new="universe"
old="string"
res=""
words=s.split()
for word in words:
    if word==old:
        print(word+" "+new)
 
        


# Convert the string "Hello welcome to Python" to a comma separated string.
e="Hello string"
print(",".join(s))


#Write a program to print alternate characters in a string.**
s="bangalore"
print(s[::2])

#Write a Program to print ascii values of the characters present in a string.**

#Write a function to convert upper case to lower case and vice-versa without using inbuilt methods.**

# Write a program to read a random line in a file. (ex. 50, 65, 78th line)**
from itertools import islice

with open(r"C:\Users\ANISH DASMAHAPATRA\Desktop\New folder\self_practice\access-log.txt") as f:
    n=islice(
        
