## Luhn Algorithm Credit Card Checker.

def checkCard(cardNo):
    nDigits = len(cardNo)
    nSum = 0
    isSecond = False
    for i in range(nDigits - 1, -1, -1):
        d = ord(cardNo[i]) - ord('0')
        if (isSecond == True):
            d = d * 2
        nSum += d // 10
        nSum += d % 10
        isSecond = not isSecond
    if (nSum % 10 == 0):
        return True ## Card Passed Check
    else:
        return False ## Card Failed Check
