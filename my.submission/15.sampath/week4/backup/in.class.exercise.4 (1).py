{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h1> <a href= \"http://interactivepython.org/runestone/static/pythonds/Recursion/toctree.html\"> In Class Exercise: #4 </a>  </h1>\n",
    "<ul>\n",
    "    \n",
    "<li> Recursion vs Iteration </li>\n",
    "<li> Three Laws of Recusion</li>\n",
    "<li>  Example: Tower of Hanoi, Maze, Dynamic Programming</li>\n",
    "</ul>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h1> <a href= \"http://interactivepython.org/runestone/static/pythonds/Recursion/DiscussionQuestions.html\">4.15. Discussion Questions\n",
    " </a> \n",
    "\n",
    "</h1>\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Write both  recursive and iterative function to compute the Fibonacci sequence. \n",
    "        How does the performance of the recursive function compare to that of an iterative version?\n",
    "           F(1)=F(2) = 1\n",
    "   F(n) = F(n-1)+F(n-2), for n >= 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def recursive_factorial (n):\n",
    "  if n == 0:\n",
    "    return 1\n",
    "  else:\n",
    "    return n *recursive_factorial(n-1)\n",
    "def iterative_factorial (n):\n",
    "  product = 1\n",
    "  for i in range(1,n + 1):\n",
    "    product = product * i\n",
    "    return product"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Using the dynamic programming algorithm for making change, find the smallest number of coins that you can use to make 33 cents in change. In addition to the usual coins assume that you have an 8 cent coin."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import math\n",
    "\n",
    "\n",
    "def findMinCoins(denomination, change):\n",
    "    minCoins = change\n",
    "    if(len(denomination) == 0 or change == 0):  # when there are no coins or change is 0\n",
    "        return 0\n",
    "    elif(change in denomination):\n",
    "        return 1\n",
    "    elif(change < min(denomination)):\n",
    "        return float(\"inf\")\n",
    "    else:\n",
    "        for i in denomination:\n",
    "            if(i <= change):\n",
    "                numCoins = 1 + findMinCoins(denomination, change - i)\n",
    "                if(numCoins < minCoins):\n",
    "                    minCoins = numCoins\n",
    "    return minCoins\n",
    "\n",
    "\n",
    "c = [1, 5, 10, 8, 25]\n",
    "d = 33\n",
    "\n",
    "print(findMinCoins(c, d))\n"
   ]
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
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
