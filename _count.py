##Write a program to find the length of the string without using inbuilt function (len)**

s="Bangalore is good place"
_count=0
____________________________________________
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
def convert(any_string):
    l=[]
    
    for word in any_string:
        temp=ord(word)
        if temp in range(97,123):
            l.append(chr(temp-32))
        elif temp in range(65,91):
            l.append(chr(temp+32))
        else:
            l.append(chr(temp))
    return ''.join(l)
print(convert("Hello World"))
    
#9. Write a program to swap two numbers without using the 3rd variable.**

#10. Write a program to merge two different lists.**

#
#14. Write a program to check if the given string is Palindrome or not without using reversed method.**
s="malayalam"
def palin(string):
    if string==string[::-1]:
        return True
    return False
print(palin("malayalam"))


#Write a program to search for a character in a given string and return the corresponding index.
from collections import defaultdict
s="hello world"
d=defaultdict(list)
for index,value in enumerate(s):
    d[value]+=[index]
print(d)

#Write a program to get the below output

#d = {'h': ['hello', 'hi'], 'w': ['world', 'welcome'], 't': ['to', 'there'], 'p': ['python', 'programming'] }
sentence = "hello world welcome to python programming hi there"
from collections import defaultdict
words=sentence.split()
d=defaultdict(list)
for word in words:
    d[word[0]].append(word)
print(d)

# Write a function which takes a list of strings and integers.If the item is a string it should print as is and if the item is integer or float it should reverse it.
s=["Anish",345,567.09]
def func(any):
    for item in any:
        if isinstance(item,str):
            print (item)
        else:
            temp=str(item)
            print (temp[::-1])
print(func(s))


#Write a to replace all the characters with - if the character occurs more than once in a string**
my_string = 'hellohai' # O/P should be '-e--o-ai'
print(''.join(['-' if s.count(my_string)>1 else s for s in my_string]))

#write a decorator that returns only positive values of subtraction**
def pos(func):
    def wrapper(*args,**kwargs):
        result=func(*args,**kwargs)
        return abs(result)
    return wrapper

@pos
def num(a,b):
    return a-b

print(num(20,30))


class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __setattr__(self, name, value):
        super().__setattr__(name, value)

p=Person("Anish","Das")
print(p.__dict__)
print(p.fname)

class Point:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
            
    def __setitem__(self,name,value):
        if name== fname:
            self.fname = value
        elif name == lname:
            self.lname = value
        else:
            raise Exception("Point Object is out of index")
    def __getitem__(self,name):
        if name=='fname':
            return self.fname
        elif name == 'lname':
            return self.lname
        else:
            raise Exception("Point Object is out of index")
p=Point("Anish","Dasm")
print(p['lname'])


#########Write a program to reverse a string without using any inbuilt functions.*************
def reverse(string):
    temp=[]
    for i in range(len(string)-1,-1,-1):
        temp.append(string[i])
    return(''.join(temp))
print(reverse("python"))
print(reverse("Hello world"))

#Write a python program to get the below output**
sentence = "Hi How are you"

def func(string):
    return string[::-1]
print(func(sentence))

#Write a python program to get the below output**
sentence = "Hi How are you"
s=sentence.split()
split=[word[::-1] for word in s]
reverse=" ".join(split)
print(reverse)

####
a = [1, 2, 3] 
b = [1, 2, 3, 4]


##Print all the numbers in the below list**
a = ['abc', '123', 'hello', '23']
for words in a:
    if words.isnumeric():
        print(words)

##Write a function to print the below output.**

# func("TRACXN", 0)  # Should print RCN
# func("TRACXN", 1)  # Should print TAX

def func(string,value):
    if value==0:
        return string[0::2]
    elif value==1:
        return string[1::2]
print (func("TRACXN",1))
              
##Write a function to reverse any iterable without using reverse function.
any=[1,3,7,0,9]
r=[]

for i in range (len(any)-1,-1,-1):
    r.append((any[i]))
print(r)

##Write a to replace all the characters with - if the character occurs more than once in a string**
string = 'hellohai' # O/P should be '-e--o-ai'
for char in string:
    if string.count(char)>1:
        string=string.replace(char,"-")
print(string)

##Write a method that returns the last digit of an integer. For example, the call of get_last_digit(3572) should return 2.
def func(check):
    temp=str(check)
    return temp[-1]
print(func(6578))

##68 Make a function named tail that takes a sequence (like a list, string, or tuple) and a number n and returns the last n elements from the given sequence, as a list.**
def func(args,n):
    if not isinstance(n,int):
        raise TypeError('Value of N should be Integer')
    elif n <=0:
        raise TypeError("negative value not accepcted")
    return list(args)[-n:]
print(func([1,3,5,6,7.04,7],3))
    
print (func("Anish",3))

###
words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes','the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the','eyes', 'look', 'into','my', 'eyes', "you're", 'under']

d=defaultdict(int)
for word in words:
    d[word]+=1
print(d)

from collections import defaultdict
p=defaultdict(int)
for word in words:
    if word[0] in "AEIOUaeiou":
        p[word]+=1
print(p)

##94 Write a program to print prime numbers from 1 to 50**
def is_prime(number):
    for i in range(2,number):
        if number%i==0:
            return False
            break
        return True
print(is_prime(5))

##97 Write a program to count the number of occurrences of non-special characters in a given string**
from re import findall
s = 'hello@world! welcome!!! Python$ hi how are you & where are you?'

print(findall(r"[^\w]+",s))

#*95 Write a program to sort a list which has mix of both odd and even numbers, the sorted list should have odd numbers first and then even numbers in sorted order**
a = [3, 4, 1, 7, 2, 12, 8, 6, 9, 11]
_evens=[num for num in a if num%2==0]
_odd=[num for num in a if num%2!=0]
_even_sort=sorted(_evens)
_odd_sort=sorted(_odd)
print(*_odd_sort,*_even_sort)

#96 Write a program to sort a list which has mix of both odd and even numbers, in the sorted list, odd numbers should be in ascending order and even numbers should be in descending order**
a = [3, 4, 1, 7, 2, 12, 8, 6, 9, 11] # o/p should be [1, 3, 7, 9, 11, 12, 8, 6, 4, 2]

#Grouping Flowers and Animals in the below list**
items = ['lotus-flower', 'lilly-flower', 'cat-animal', 'sunflower-flower', 'dog-animal']
i=defaultdict(list)
for item in items:
    _item,group=item.split("-")
    i[group]+=[_item]
print(i)

#*99 Grouping files with same extensions**
files = ['apple.txt', 'yahoo.pdf', 'gmail.pdf', 'google.txt', 'amazon.pdf', 'facebook.txt', 'flipkart.pdf']
j=defaultdict(list)
for file in files:
    _name,tag =file.split(".")
    j[tag]+=[_name]
print(j)

#Filter only those characters except digits**
s = '@hello12world34welcome!123'
print(findall(r"[^\d]+",s))

#101 Count number of words in a sentence. ignore special characters.**
sentence = "Hi there! How are you:) How are you doing today!"
###

sentence = "hello world welcome to programming"
s=sentence.split()
max_len=0
ma_word=""
for word in s:
    if len(word)>max_len:
        max_len=len(word)
        max_word=word
    print(max_word,max_len)



s="how are u yellow"
long={ word:len(word) for word in s.split()}
print(sorted(long.items(),key=lambda item:item)[::-1][0])

names=["alex","james","steve","john"]
char="j"
for name in names:
    if name[0]==char:
        print(name)


s="hellohai"
res=""
for char in s:
    if s.count(char)>1:
        res+="-"
    else:
        res=char
print(res)

######


#40 Program to print only the repeated characters and count of the same.**

s = 'helloworld'

print({word:s.count(word) for word in s if s.count(word)>1})

##100 Filter only those characters except digits**

s = '@hello12world34welcome!123'
from re import findall
k=(findall(r"[^0-9]+",s))
print("".join(k))


##101 Count number of words in a sentence. ignore special characters.**

sentence = "Hi there! How are you:) How are you doing today!"

from re import findall
m=(findall(r"\b\w+\b",sentence))
from collections import Counter
print(Counter(m))

##104 Find all max length words from the below sentence**
sentence = "hello world hi apple you yahoo to you"

print({(word,len(word)) for word in sentence.split()})


##109 Replace all vowels with "*"**
sentence = "hello world welcome to 012python"
sign="*"
res=""

for char in sentence:
    if char in "aeiouAEIOU":
        res=res+sign
    else:
        res+=char
print(res)

##**111 Maximum sum of 3 numbers and Minimum sum of 3 numbers**
numbers = [10, 15, 20, 25, 30, 35, 40, 15, 15]
number=set(numbers)
number=(sorted(numbers))

print(sum(number[-3::]))
print(sum(number[::3]))


##112 Write a program to get the output as below**
s="python@#$%pool"
# o/p should be ['PYTHON', 'POOL']

k=(findall(r"\w+",s))
print([word.upper() for word in k])

##113 Write a program to print all the number which are ending with 5**
numbers = ['1', '12', '123', '12345', '125', '905', '55', '5', '95655', '55555']
from re import findall
for number in numbers:
    if number.endswith("5"):
        print(number)

##**116 Write a program to print all the words which starts with letter 'h' in the given string**
string = 'hello world hi hello universe how are you happy birthday'
print(findall(r"\bh\w+",string))

##**117 Write a program to sum all even numbers in the given string**
sentence = 'hello 123 world 567 welcome to 9724 python'
numbers=(findall(r"\d",sentence))
type_cast=[int(number) for number in numbers]
print([number for number in type_cast if number%2==0])

##**126 In the list below, find all the number pairs which results in 10 either when added or subtracted**
a = [3, 5, -4, 8, 11, 1, -1, 6]
for item1 in a:
    for item2 in a:
        if item1!=item2:
            if item1+item2==10 or item1-item2==10:
                print((item1,item2))

##**127 Write a decorator to prefix +91 to the original phone numbers**

numbers = [1234567890, 123456790, 1234567890]

def prefix_country(func):
    def wrapper(*args,**kwargs):
        prefix_number=[ "+91-"+str(number) for number in numbers]
        return func(prefix_number)
    return wrapper

@prefix_country
def code(numbers):
    for number in numbers:
        print(number)
code(numbers)


###132 Reverse a list without using any built-in functions and slicing**
a = [1, 2, 3, 4, 5]

print([a[i] for i in range(len(a)-1,-1,-1)])


###do this
s=["anish.mail","number.int"]
dd=defaultdict(list)
for item in s:
    name,ite=item.split(".")
    dd[ite]+=[name]
print(dd)


##grouping anagrams
l = ["listen", "hello", "eat", "desserts", "silent", "peek", "ate", "keep", "tea", "stressed"]
d={}
for item in l:
    length=len(item)
    if length not in d:
        d[length]=[item]
    else:
        d[length]+=[item]
print(d)

##
##52 Write a program to replace value present in nested dictionary.**
d = {'a': 100, 'b': {'m': 'man', 'n': 'nose', 'o': 'ox', 'c': 'cat'}}
# Replace "nose" with "net"

for name,value in d.items():
    if isinstance(value,dict):
        d[name]['n']='net'
print(d)




i=[12,35,9,56,24]
output=[]
a=12
b=24
a,b=b,a
i[0]=a
i[4]=b
print(i)

l=[30,10,60,20,9,10]
largest=0
for item in l:
    if item>largest:
        largest=item
print(largest)

a=[2,4,56,89]
def number(iterable,n):
    if not isinstance(n,int):
        raise Exception 
    return list(iterable)[-n:]

print(number("ANISH",2))


s='AGLOSHACK'
from re import findall
print(findall(r"[AEIOU]",s))


items = ['apple', 1.2, 'google', '12.6', 26, '100']
for item in items:
    if isinstance(item,(int,float)):
        print(item)

for i in range(7,0,-1):
    print(f"{'*'* i:^12}")


pat=''
for i in range(0,6):
    pat+=str(i)
    print(f"{'*'*i:6}")


pat=''
for i in range(1,6):
    pat=pat+' '+str(i)
    print(f"{pat:^12}")


apple_products = {'iPhone', 'Mac', 'iWatch'}
google_products = {'Gmail', 'Maps', 'Google Drive'}
msft_products = {'Windows', 'One Drive'}

d=defaultdict(list)

for prod in apple_products:
    d['apple.inc'].append(prod)
print(d)

names = ["apple", "google", "yahoo", "gmail", "facebook", "flipkart", "amazon"]

def rotate(iterable,n):
    for i in range(0,n):
        item=iterable.pop()
        iterable.insert(0,item)
    return iterable

print(rotate(names,1))


def rotate_string(string,n):
    string=list(string)
    for i in range(0,n):
        letter=string.pop()
        string.insert(0,letter)
    return string

print(rotate_string("ANISH",2))

##################################################################################################################
_count={}

def count(func):
    def wrapper(*args,**kwargs):
        if args in _count:
            return _count[args]
        else:
            result=func(*args,**kwargs)
            _count[args]=result
        return result
    return wrapper

@count
def num(a,b):
    return a+b
print(num(3,4))
print(num(4,5))
print(_count)



def func_call(func):
    func.count=0
    def wrapper(*args,**kwargs):
        func.count+=1
        if func.count>5:
            raise ValueError(f"you have reached {func.__name__} max time")
        return func(*args,**kwargs)
    return wrapper

@func_call
def add(a,b):
    return a+b
print(add(4,5))
print(add(4,5))
print(add(4,5))
print(add(4,5))
print(add(4,5))
print(add(4,5))


    
        
