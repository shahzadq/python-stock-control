# display an error then end the program
def printError(s: str):
    print(s)
    exit()


# show an input with an empty line above
def inputWithLineBreak(s: str):
    print("")
    return input(s)


# attempt to convert a code to an int otherwise show an error and end program
def convertCodeToInt(code) -> int:
    try:
        return int(code)
    except ValueError:
        printError("Invalid code. Code must only contain digits")


# ensure code is of a specific length, otherwise print error
def requireCodeLength(code: str, requiredLen: int):
    if len(code) != requiredLen:
        printError(
            f"Invalid code length. Make sure your code is {requiredLen} digits exactly")


# check if a number is even
def isEven(num: int):
    return num % 2 == 0


# algorithm for mapping over digits in code and adding based on position
def calculateCodeDigitsAddition(code: str):
    sum = 0

    for idx, i in enumerate(code):
        i = convertCodeToInt(i)
        sum += (i * 3) if isEven(idx) else i

    return sum


def calculateCheckDigit(code: str):
    requireCodeLength(code, 7)

    checkDigit = calculateCodeDigitsAddition(code)
    checkDigit = (((checkDigit + 9) // 10) * 10) - checkDigit

    return checkDigit


def isCodeValid(code: str):
    requireCodeLength(code, 8)

    calculation = calculateCodeDigitsAddition(code)
    calculation = calculation % 10

    return calculation == 0


print("MENU")
print("1 - Calculate check digit")
print("2 - Check code validity")

menuItem = inputWithLineBreak(
    "Choose an option from above (enter the digit): ")

if menuItem == "1":
    code = inputWithLineBreak("Enter a seven digit code: ")
    checkDigit = calculateCheckDigit(code)
    print(f"The check digit for {code} is: {checkDigit}")

elif menuItem == "2":
    code = inputWithLineBreak("Enter your eigth digit code: ")
    isValid = isCodeValid(code)
    print(f"Code {code} is: {'VALID' if isValid else 'INVALID'}")

else:
    print("Invalid choice")
