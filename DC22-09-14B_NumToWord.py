words = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}

tens = {
    0: "",
    1: "teen",
    2: "twenty",
    3: "thirty",
    4: "fourty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "nintey"
}

millions = {
    -1: "",
    0: "thousand",
    1: "million",
    2: "billion",
    3: "trillion",
    4: "quadrillion",
    5: "quintillion",
    6: "sextillion",
    7: "septillion",
    8: "octillion",
    9: "nonillion"
}

def process(num):
    cents = int(round(num - int(num),2)*100)
    digits = list(str(int(num)))

    if len(digits)%3 == 2:
        digits.append("0")
    elif len(digits)%3==1:
        digits.append("0")
        digits.append("0")

    for i in range(len(digits)//3):
        if check != True:
            check = False
        else:
            pass

        print(words.get(int(digits[i])), end = "")

    print(" dollars")

def eval(digits, i):


    if ((digits[i] == 0) and (digits[i-1] == 0) and (digits[i-2] == 0)):
        return True







doExit = False
print("-------------------------------------------------------------------------")
print("Welcome to the Auto Check Writing Program!")
while doExit == False:
    num = float(input("\n\nPlease enter dollar amount for check, 0 to quit: "))
    if num != 0:
        process(num)
    else:
        print("Thank you for using the Auto Check Writing Program!")
        doExit = True