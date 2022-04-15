k = 2
file = open("sifreli.txt","r")
message = file.read().lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
#alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"
mod = len(alphabet)
encrypt_message = ''
for x in message:
    for y in alphabet:
        if(y==x):
            location = alphabet.index(y)
            location -= k
            encrypt_message += " "+alphabet[location % mod]
print("Message : " + message + "\n")
print("Encrypted Message: " + encrypt_message)

file.close()

file2 = open("realmetin.txt","a")
file2.write(encrypt_message)

