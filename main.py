# Write a Python program to check whether a given string is palindrome or not
x=input()

xrevers="".join(reversed(x))
if(x==xrevers):
  print("Palindrome")
