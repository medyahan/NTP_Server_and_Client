def textToDecimal(text):
    liste = []
    yeni = []
    for i in text:
        liste.append(format(ord(i)))

    for j in liste:
        if (len(j) == 2):
            yeni.append("0")
            yeni.append(j)
        else:
            yeni.append(j)
    return ''.join(yeni)

def decimalToText(decimal):
    liste = []
    yeni = []
    i = 0
    while (i != len(decimal)):
        liste.append(''.join(decimal[i: (i + 3)]))
        i = i + 3
    for j in liste:
        yeni.append(chr(int(j)))
    return ''.join(yeni)
