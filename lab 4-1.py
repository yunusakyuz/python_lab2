{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def pos_arg(a, b):\n",
    "    print(a)\n",
    "    print(b)\n",
    "    \n",
    "pos_arg(\"first\", \"second\")\n",
    "print()\n",
    "pos_arg(\"second\", \"first\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def texter(t1, t2, t3) :\n",
    "    print(f\"{t2} {t3} {t1}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = \"i\"\n",
    "b = \"love\"\n",
    "c = \"you\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "texter(c,a,b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):\n",
    "    print(\"-- This parrot wouldn't\", action, end=' ')\n",
    "    print(\"if you put\", voltage, \"volts through it.\")\n",
    "    print(\"-- Lovely plumage, the\", type)\n",
    "    print(\"-- It's\", state, \"!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "parrot(1000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "parrot(voltage = 1000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "parrot(voltage = 10000000, action = \"VOOOOM\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):\n",
    "    print(\"-- This parrot wouldn't\", action, end=' ')\n",
    "    print(\"if you put\", voltage, \"volts through it.\")\n",
    "    print(\"-- Lovely plumage, the\", type)\n",
    "    print(\"-- It's\", state, \"!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "parrot(action = \"VOOOOOM\", voltage = 10000000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "parrot(\"a million\", \"bereft of life\", \"jump\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "parrot(\"a thousand\", state = \"pushing up the daisies\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "parrot()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "parrot(voltage = 5, \"dead\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):\n",
    "    print(\"-- This parrot wouldn't\", action, end=' ')\n",
    "    print(\"if you put\", voltage, \"volts through it.\")\n",
    "    print(\"-- Lovely plumage, the\", type)\n",
    "    print(\"-- It's\", state, \"!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "parrot(\"dead\", voltage = 5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "def slicer(*num):\n",
    "    even = [i for i in num if i%2==0]\n",
    "    odd = [j for j in num if j%2!=0]\n",
    "    print(\"even : \" , even)\n",
    "    print(\"odd : \" , odd)"
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
      "even : [2, 4, 6, 8]\n",
      "odd : [1, 3, 5, 7, 9]\n"
     ]
    }
   ],
   "source": [
    "slicer(1,2,3,4,5,6,7,8,9)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "def slicer1(*num):\n",
    "    even = []\n",
    "    odd = []\n",
    "    for i in num :\n",
    "        if i%2 == 0 :\n",
    "            even.append(i)\n",
    "        else:\n",
    "            odd.append(i)\n",
    "    print(\"even :\", even)\n",
    "    print(\"odd :\", odd)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "even : [2, 4, 6, 8]\n",
      "odd : [1, 3, 5, 7, 9]\n"
     ]
    }
   ],
   "source": [
    "slicer1(1,2,3,4,5,6,7,8,9)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "def organizer(**people) :\n",
    "    name = []\n",
    "    age = []\n",
    "    \n",
    "    for key, value in people.items():\n",
    "        name.append(key)\n",
    "        age.append(value)\n",
    "    print(name)\n",
    "    print(age)"
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
      "['ahmet', 'mehmet', 'tulin', 'fatma']\n",
      "[33, 22, 44, 2]\n"
     ]
    }
   ],
   "source": [
    "organizer(ahmet = 33, mehmet = 22, tulin = 44, fatma = 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "def meaner(ahmet, mehmet, burhan) :\n",
    "    avg = (ahmet + mehmet + burhan)/3\n",
    "    print(\"average:\", avg)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "friend = {\"ahmet\": 44, \"mehmet\":22, \"burhan\":40}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "average: 35.333333333333336\n"
     ]
    }
   ],
   "source": [
    "meaner(**friend)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "damat_gelin = {\"f\":[\"marry\", \"bella\", \"susan\"], \\\n",
    "               \"m\":[\"fred\", \"paul\", \"bahadir\"]}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "def muruvvet(f, m):\n",
    "    x_list = []\n",
    "    for x in zip(f, m):\n",
    "        x_list.append(x)\n",
    "    return x_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "[(\"marry\", \"fred\"), (\"bella\", \"paul\"), (\"susan\", \"bahadir\")]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('marry', 'fred'), ('bella', 'paul'), ('susan', 'bahadir')]"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "muruvvet(**damat_gelin)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
