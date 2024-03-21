import string

mensagem = input("Indique uma mensagem: ")
key = int(input("Indique a key: "))



alphabetl = string.ascii_lowercase
shiftedl = alphabetl[key:] + alphabetl[:key]
tablel = str.maketrans(alphabetl,shiftedl)


alphabetu = string.ascii_uppercase
shiftedu = alphabetu[key:] + alphabetu[:key]
tableu = str.maketrans(alphabetu,shiftedu)

encryptedl = mensagem.translate(tablel)
encryptedFinal = encryptedl.translate(tableu)

print("Resultado: " + encryptedFinal)





