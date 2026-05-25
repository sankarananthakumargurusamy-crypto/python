{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3d1cf348-5ef4-4c23-b75b-c438ff728f75",
   "metadata": {},
   "outputs": [],
   "source": [
    "class multipleFunctions():\n",
    "    \n",
    "    def oddEven():\n",
    "        num = int(input(\"Enter the number: \"))\n",
    "        if (num % 2) == 0:\n",
    "            print(\"Even number\")\n",
    "            msg = \"even number\"\n",
    "        else:\n",
    "            print(\"Odd number\")\n",
    "            msg = \"odd number\"\n",
    "        return msg\n",
    "\n",
    "    def BMI():\n",
    "        BMI = float(input(\"Enter the BMI: \"))\n",
    "        if BMI < 18.5:\n",
    "            print(\"Underweight\")\n",
    "            message = \"Underweight\"\n",
    "        elif BMI < 24.9:\n",
    "            print(\"Normal\")\n",
    "            message = \"Normal\"\n",
    "        elif BMI < 29.9:\n",
    "            print(\"Overweight\")\n",
    "            message = \"Overweight\"\n",
    "        else:\n",
    "            print(\"Obese\")\n",
    "            message = \"Obese\"\n",
    "        return message"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
