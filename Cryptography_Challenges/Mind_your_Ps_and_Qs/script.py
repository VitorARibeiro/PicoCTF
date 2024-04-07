
#Descobri P e Q utilizando uma ferramenta online de fatorizao de numeros primos https://www.dcode.fr/prime-factors-decomposition
#1593021310640923782355996681284584012117 × 521911930824021492581321351826927897005221


#a parti de P e Q Descobrir theta
P = 1593021310640923782355996681284584012117
Q = 521911930824021492581321351826927897005221
n = 831416828080417866340504968188990032810316193533653516022175784399720141076262857
e = 65537
c = 240986837130071017759137533082982207147971245672412893755780400885108149004760496

theta = (P-1) * (Q-1)
# d * e = 1 mod theta

d = pow(e,-1,theta)
plaintext = pow(c,d,n)

#13016382529449106065927291425342535437996222135352905256639592405461024281868413

# Converting the plaintext from integer to bytes and then to string
plaintext_bytes = plaintext.to_bytes((plaintext.bit_length() + 7) // 8, 'big')
plaintext_string = plaintext_bytes.decode()

print("Decrypted message:", plaintext_string)