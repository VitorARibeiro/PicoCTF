import string

mensagem = input("Indique a mensagem: ")

alphabetL = string.ascii_lowercase
alphabetU = string.ascii_uppercase

for i in range(26):
	shiftedL = alphabetL[i:] + alphabetL[:i]
	tableL = str.maketrans(alphabetL,shiftedL)

	shiftedU = alphabetU[i:] + alphabetU[:i]
	tableU = str.maketrans(alphabetU,shiftedU)

	decryptedL = mensagem.translate(tableL)
	decryptedF = decryptedL.translate(tableU)

	print("Key: " + str(i) + "/ " + decryptedF)

