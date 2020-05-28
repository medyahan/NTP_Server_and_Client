def textToDecimal(text): # Function that converts a text message to decimal
    list = []
    new = []
    for i in text:
        list.append(format(ord(i)))

    for j in list:
        if (len(j) == 2):
            new.append("0")
            new.append(j)
        else:
            new.append(j)
    return ''.join(new)

def decimalToText(decimal): # Function that converts a decimal message to text
    list = []
    new = []
    i = 0
    while(i != len(decimal)):
        list.append(''.join(decimal[i: (i + 3)]))
        i = i + 3
    for j in list:
        new.append(chr(int(j)))
    return ''.join(new)
