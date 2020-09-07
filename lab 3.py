
Armstrong Numbers

while True:
    number = input("enter a positive number :")
    digits = len(number)
    summ = 0
    if not number.isdigit() :
        print(number, "It is an invalid entry. Don't \
        use non-numeric, float, or negative values!")
    elif int(number) >= 0:
        for i in range(digits):
            summ += int(number[i]) ** digits
        if summ == int(number):
            print(number, "is an Armstrong number.")
            break
        else:
            print(number, "is not an Armstrong number.")
            break

Prime Numbers

n = int(input("enter a number to check if it is a prime or not:"))
count = 0
for i in range(1, n+1) :
    if not (n % i) : count += 1
if (n == 0) or (n == 1) or (count >=3) : print(n, "is not a prime number.")
else : print(n, "is a prime number")

fibonacci

fibo = []
for i in range(-2, 8) :
    if i < 0 : fibo.append(1)
    else : fibo.append(fibo[i] + fibo[i+1])



{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<img src=\"https://docs.google.com/uc?id=14xeXxFrVRjvOoUYWn_GuyE-v84wVzrqr\" class=\"img-fluid\" alt=\"CLRWY\">"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h1><p style=\"text-align: center; color:darkblue\">Python In-Class (Hands-on Training), <br>12 July 2020</p><h1>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### [Assignment (Armstrong Numbers)](https://lms.clarusway.com/mod/assign/view.php?id=4905)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter a positive number :4679307774\n",
      "4679307774 is an Armstrong number.\n"
     ]
    }
   ],
   "source": [
    "while True:\n",
    "    number = input(\"enter a positive number :\")\n",
    "    digits = len(number)\n",
    "    summ = 0\n",
    "    if not number.isdigit() :\n",
    "        print(number, \"It is an invalid entry. Don't \\\n",
    "        use non-numeric, float, or negative values!\")\n",
    "    elif int(number) >= 0:\n",
    "        for i in range(digits):\n",
    "            summ += int(number[i]) ** digits\n",
    "        if summ == int(number):\n",
    "            print(number, \"is an Armstrong number.\")\n",
    "            break\n",
    "        else:\n",
    "            print(number, \"is not an Armstrong number.\")\n",
    "            break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(\"442\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### [Assignment (Prime Number)](https://lms.clarusway.com/mod/assign/view.php?id=4943)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter a number to check if it is a prime or not:1\n",
      "1 is not a prime number.\n"
     ]
    }
   ],
   "source": [
    "n = int(input(\"enter a number to check if it is a prime or not:\"))\n",
    "\n",
    "count = 0\n",
    "\n",
    "for i in range(1, n+1) :\n",
    "    if not (n % i) : count += 1\n",
    "\n",
    "if (n == 0) or (n == 1) or (count >=3) : print(n, \"is not a prime number.\")\n",
    "else : print(n, \"is a prime number\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### [Assignment (Fibonacci)](https://lms.clarusway.com/mod/assign/view.php?id=4984)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fibo = []\n",
    "\n",
    "for i in range(-2, 8) :\n",
    "    if i < 0 : fibo.append(1)\n",
    "    else : fibo.append(fibo[i] + fibo[i+1])\n",
    "        \n",
    "fibo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### A sample of ``filter()`` function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "letters = [\"a\", \"b\", \"c\", \"d\", \"e\", \"i\", \"j\", \"x\", \"t\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "def fltVowel(let):\n",
    "    vowel = [\"a\", \"e\", \"i\", \"o\", \"u\"]\n",
    "    \n",
    "    if let in vowel :\n",
    "        return True\n",
    "    else:\n",
    "        return False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fltVowel(\"b\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['a', 'e', 'i', 'u']"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(filter(fltVowel, letters))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "list()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "filitrelenmis = filter(fltVowel, letters)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a\n",
      "e\n",
      "i\n",
      "u\n"
     ]
    }
   ],
   "source": [
    "for vowel in filitrelenmis:\n",
    "    print(vowel)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Ternary Conditionals"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    }
   ],
   "source": [
    "condition = True\n",
    "\n",
    "if condition :\n",
    "    a = 1\n",
    "else :\n",
    "    a = 0\n",
    "\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "condition = False\n",
    "\n",
    "1 if condition else 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "execute body1 if condition else execute body2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## list comprehension"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "my_list = [1, 2, 3, 4, 5, 6]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "odd_sqr = []  # [1, 9, 25]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 9, 25]\n"
     ]
    }
   ],
   "source": [
    "for x in my_list :\n",
    "    if x % 2 != 0 :\n",
    "        odd_sqr.append(x ** 2)\n",
    "\n",
    "print(odd_sqr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "[expression for item in iterable]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "for item in iterable :\n",
    "    expression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['c', 'l', 'a', 'r', 'u', 's', 'w', 'a', 'y']"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bos_liste = []\n",
    "\n",
    "for i in \"clarusway\":\n",
    "    bos_liste.append(i)\n",
    "\n",
    "bos_liste"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['e', 'e', 'e', 'e']"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[i for i in \"beri gel berber\" if i == \"e\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['b', 'r', 'i', ' ', 'g', 'l', ' ', 'b', 'r', 'b', 'r']"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[i for i in \"beri gel berber\" if i != \"e\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "[\"e\", \"e\", \"e\", \"e\"]"
   ]
  },
  {
   "cell_type": "code&q...
