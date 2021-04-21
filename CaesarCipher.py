alphabet = " abcdefghijklmnopqrstuvwxyz"
global end_Phrase

def encrypt_Function(phrase, key):
    phrase = phrase.lower()
    end_Phrase = ""
    for i in range(len(phrase)):
        character = phrase[i]
        position = alphabet.find(character)
        print(position)
        newPosition = (position + key) % 26
        print(newPosition)
        newLetter = alphabet[newPosition]
        end_Phrase += newLetter
    return(end_Phrase)

def decrypt_Function(phrase, key):
    phrase = phrase.lower()
    end_Phrase = ""
    for i in range(len(phrase)):
        character = phrase[i]
        position = alphabet.find(character)
        print(position)
        if key > 25:
            newPosition = 26 - (abs((position - key)) % 26)
        else:
            newPosition = abs((position - key)) % 26
        print(newPosition)
        newLetter = alphabet[newPosition]
        end_Phrase += newLetter
    return(end_Phrase)