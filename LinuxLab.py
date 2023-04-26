import sys

def ceasarCipher (input, shift):
    upperInput = input.upper()
    newSentence = ""
    count = 0
    for i in range(len(upperInput)):
        if count == 5:
            newSentence = newSentence + " "
            count = 0
        if upperInput[i] == " ":
            continue
        if ord(upperInput[i]) < 65 or ord(upperInput[i]) > 90:
            newSentence = newSentence + upperInput[i]
            count += 1
            continue
        let = ord(upperInput[i]) + shift
        if let < 65:
            let += 26
        elif let > 90:
            let -= 26
        newSentence = newSentence + chr(let)
        count += 1
    return newSentence

for line in sys.stdin:
    ceasarCipher(line)
