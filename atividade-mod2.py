
def isPalindrome(str):
    if str == str[::-1]:
      return True
    else:
      return False

def main():
  str = input("Entre uma PALAVRA para testar se é um palindromo:")

  if (isPalindrome(str)) == True:
    print(str + " é um palindromo!")
  else:
    print(str + " não é um palindromo!")

if __name__ == "__main__":
    main()