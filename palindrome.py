#palindrome
n = input("Enter a Number:")
if n == str(n[::-1]):
  print("It is a palindrome")
else:
  print("It is not a palindrome")
