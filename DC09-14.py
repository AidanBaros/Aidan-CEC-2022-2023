def NumberClump(digitList, i):
    if digitList[i] != 0:
        if digitList[i-1] != 1 and digitList[i-1] != 0:
            print(words.get(digitList[i]), "hundred", tens.get(digitList[i-1]), words.get(digitList[i-2]), end = '')

        elif digitList[i-1] == 1 and digitList[i-2] == 0:
            print(words.get(digitList[i]), "hundred and ten", end = '')

        elif digitList[i-1] == 1 and digitList[i-2] == 1:
            print(words.get(digitList[i]), "hundred and eleven", end = '')

        elif digitList[i-1] == 1 and digitList[i-2] == 2:
            print(words.get(digitList[i]), "hundred and twelve", end = '')

        elif digitList[i-1] == 1 and digitList[i-2] == 3:
            print(words.get(digitList[i]), "hundred and thirteen", end = '')

        elif digitList[i-1] == 1 and digitList[i-2] == 5:
            print(words.get(digitList[i]), "hundred and fifteen", end = '')
        
        elif digitList[i-1] == 1:
            print(words.get(digitList[i]), "hundred", words.get(digitList[i-2])+ tens.get(digitList[i-1]), end = '')

    elif digitList[i] == 0:
        if digitList[i-1] == 0:
            print(words.get(digitList[i-2]), end = '')

        elif digitList[i-1] == 1 and digitList[i-2] == 0:
            print("ten", end = '')
        
        elif digitList[i-1] == 1 and digitList[i-2] == 1:
            print("eleven", end = '')

        elif digitList[i-1] == 1 and digitList[i-2] == 2:
            print("twelve", end = '')

        elif digitList[i-1] == 1 and digitList[i-2] == 3:
            print("thirteen", end = '')

        elif digitList[i-1] == 1 and digitList[i-2] == 5:
            print("fifteen", end = '')

        else:
            print(tens.get(digitList[i-1]), words.get(digitList[i-2]), end = '')
    
    if ((digitList[i] == 0) and (digitList[i-1] == 0) and (digitList[i-2] == 0)):
        return True

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

def NumberCrunch(num):
    amount = int(num)
    digitList = []
    i = 1
    while amount>=1:
        digitList.append(amount%10)
        num -= (amount%10)* i 
        amount = amount//10
        i*=10

    num = round(num, 2)
    num = num * 100

    if len(digitList)%3 == 2:
        digitList.append(0)
    elif len(digitList)%3==1:
        digitList.append(0)
        digitList.append(0)
    
    x = 2
    if len(digitList)>=3:
        for j in range(((len(digitList))//3)-1):
            check = NumberClump(digitList, ((len(digitList))-((j+1)*3))+2)
            if check != True:
                print(" "+str(millions.get(((len(digitList))//3)-x))+", " , end = '')
            else:
                pass
            x += 1
    NumberClump(digitList, 2)
    if int(num) == 0:
        print("dollars")
    else:
        print("dollars and", int(num), "/ 100")

doExit = False
print("-------------------------------------------------------------------------")
print("Welcome to the Auto Check Writing Program!")
while doExit == False:
    num = float(input("\n\nPlease enter dollar amount for check, 0 to quit: "))
    if num != 0:
        NumberCrunch(num)
    else:
        print("Thank you for using the Auto Check Writing Program!")
        doExit = True
