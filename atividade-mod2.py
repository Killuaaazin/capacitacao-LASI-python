def isPalindrome(str):
    if str == str[::-1]:
      return True
    else:
      return False

def main():
  str = input("Enter a WORD to be tested as a palindrome:")

  if (isPalindrome(str)) == True:
    print(str + " is a palindrome!")
  else:
    print(str + " is NOT a palindrome!")

if __name__ == "__main__":
    main()