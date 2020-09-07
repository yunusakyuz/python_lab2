#!/usr/bin/env python
# coding: utf-8
​
# In[3]:
​
​
# assignment armstrong numbers
# To improve your control flow statement and arithmetic operator algorithm skills.
# while döngüsü kullanilmali. sarti saglandiginda cikmasi icin break kullan
while True:
    number = input("enter a positive number :")
    digits = len(number)
    summ = 0
    if not number.isdigit():   # kullanicilara uyari vermem lazim
        print(number, "It is an invalid entry. Don't use non-numeric, float, or negative values!")
    elif int(number) >= 0:
        for i in range(digits):
            summ += int(number[i]) ** digits
        if summ == int(number):
            print(number, "is an Amstrong number.")
            break
        else:
            print(number, "is not an Amstrong number.")
            break
​
​
# In[5]:
​
​
# Assignment - 4 (Is it a Prime Number?)
# To improve your control flow statement skills and to raise your awareness of some algebraic knowledge.
# Write your Python codes on any IDLE, push it up to your GitHub repository and submit your GitHub Page link address in addition to your code as a plain text.
# Task : Write a program that takes a number from the user and prints the result to check if it is a prime number.
# rule: sadece 1 ve kendisine bölünebilen sayilara prime number denir.
# n 17olsun, 1-17 % = 0 mi degilmi bakarim. 1 2 3 4 5.... 17.
​
n = int(input("Enter a number to check if it is a prime or not: "))
count = 0
for i in range(1, n+1):
    if not (n % i):  # kosulum
        count +=1
if (n ==0) or (n == 1) or (count >=3):
    print(n, "is not a prime number.")
else:
    print(n, "is a prime number")
​
​
# In[17]:
​
​
# Assignment - 5 (Fibonacci Numbers)
# To improve your control flow statement skills and to raise your awareness of some algebraic knowledge.
# Write a Python code on any IDE, push it up to your GitHub repository and submit GitHub page address link in addition to your code (answer) as a plain text.
# Task : Create a list consisting of Fibonacci numbers from 1 to 55 using control flow statements.
# fibonacci →  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# bunun icin yine for döngüsüne ihtiyacim var
​
fibo = []
for i in range (-2, 8) :
    if i < 0:
        fibo.append(1)
    else:
        fibo.append(fibo[i] + fibo[i + 1])
fibo
​
​
# In[14]:
​
​
fibonacci_list = [1,1]
toplam = 0
for i in range(100):
    toplam = fibonacci_list[i] + fibonacci_list[i + 1]
    fibonacci_list.append(toplam)
    if toplam == 55:
        break
print(fibonacci_list)
​
​
# In[11]:
​
​
fibonacci = [1, 1]
while fibonacci[-1] < 55:
    fibo_next = fibonacci[-2] + fibonacci[-1]
    fibonacci.append(fibo_next)
print(fibonacci)
​
​
# In[12]:
​
​
a = 0
b = 1
fibonacci = [b]
for i in range(1,10):
    c = a + b 
    fibonacci.append(c)
    a, b = b, c
print(fibonacci)
​
​
# In[ ]:
​
​
# bu islerin anahtari self study
# artik kalfalik asamasina gelindi
​
​
# In[25]:
​
​
# mesela filter ile ilgili bir calisma yapalim
# filter belirleen fonksiyona gore true lari alip cikti olarak veriyor
​
letters = ["a", "b", "c", "d", "e", "i", "j", "x", "t", "u"]
# sesli harf secen bir fonksiyon yazayim
def fltvowel(let):
    vowel = ["a", "e", "i", "o", "u"]
    if let in vowel:
        return True
    else:
        return False
#filter(fltvowel, letters) # bir obje üretir. o yüzden bir degisken yada listeye atamam lazim
# list(filter(fltvowel, letters))
filitrelenmis = filter(fltvowel, letters)
for vowel in filitrelenmis:
    print(vowel)
​
​
# In[26]:
​
​
fltvowel("b")
​
​
# In[29]:
​
​
# simdi daha zor bir kalfalik sorusu
# hem kontrol hem de loop
# daha az satir yazmak icin. tek satirda if kullanimi
condition = True
if condition:
    a =1
else:
    a = 0
print(a)
    
​
​
# In[31]:
​
​
# turnover if kullanimi
# execute body1 if condition else ececute body2
​
condition = True
# a =1 if condition else 0
1 if condition else 0
print(a)
​
​
# In[68]:
​
​
# list comprehension: tek satir for döngülerini kullanma
# [expresion for item in iterable] bu isin formulu ve kullanimi
my_list = [1, 2, 3, 4, 5, 6]
odd_sqr = []  # [1, 9, 25] tek olanlari alcam karelerini alip yeni bir listede toplayacam
for x in my_list:
    if x % 2 != 0:
        odd_sqr.append(x ** 2)
​
print(odd_sqr)
​
​
# In[35]:
​
​
for item in iterable:
    expression
​
​
# In[42]:
​
​
my_list = [1, 2, 3, 4, 5, 6]
[x ** 2 for x in my_list if x % 2 !=0] # append kullnamadan list comprehension yapmis olduk
[x+1 for x in my_list]
​
​
# In[43]:
​
​
strings = ["ali", "veli", "ayse"]
​
​
# In[44]:
​
​
[len(i) for i in strings] # append kullnamadan sirayla listemize ekledi. buna list comprehension deniyor..
​
​
# In[45]:
​
​
# tuple ile ilgili bisey yapalim
import sys
​
x = [1, 2, 3]
y =(1,2,3)  # tuple llar daha z yer kapliyor memoride
print(sys.getsizeof(x))
print(sys.getsizeof(y))
​
​
# In[46]:
​
​
(x ** 2 for x in my_list) # generator olarak calistigi icin sadece obje doner. nazli. bunun icin baska sey lazim. next kullnamak lazim
​
​
# In[55]:
​
​
a = (x ** 2 for x in my_list) # bunu next ile generate edebiliriz. for gibi kullnabiliyorum. cok ilginc
​
​
# In[56]:
​
​
next(a)
​
​
# In[51]:
​
​
next(a)
​
​
# In[52]:
​
​
next(a)
​
​
# In[58]:
​
​
a = (x ** 2 for x in my_list)
for i in a:  # aslinda for döngüsünün arka planinda next calisiyor denebilir..
    print(i)
​
​
# In[61]:
​
​
bos_liste = []
for i in "clarusway":
    bos_liste.append(i)
bos_liste
# asagida bu kodu tek satirda yazabiliriz. 
​
​
# In[62]:
​
​
[i for i in "clarusway"]  # sahane kullanim sekli!!
​
​
# In[66]:
​
​
[i for i in "beri gel berber" if i == "e"]
