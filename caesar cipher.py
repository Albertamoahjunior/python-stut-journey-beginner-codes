
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
'w', 'x', 'y', 'z']
#encryptying message
def encrypt(text,shift):
    cipher_text = ""
    for letter in text:
        if letter not in alphabets:
            cipher_text += letter
        else:
            position = alphabets.index(letter)
            new_position = position + shift % 26
            if new_position > 25:
                new_position -= 26
            new_letter = alphabets[new_position]
            cipher_text += new_letter
    print(cipher_text)

#decrptying messages
def decrypt(text,shift):
    cipher_text = ""
    for letter in text:
        if letter not in alphabets:
            cipher_text += letter
        else:
            position = alphabets.index(letter)
            new_position = position - shift % 26
            new_letter = alphabets[new_position]
            cipher_text += new_letter
    print(cipher_text)


direction = input("Type 'encode' to encrpyt, type 'decode' to decrypt: ").lower()

text = input("Enter your message here: \n").lower()

shift = int(input("Enter the shift number: "))

if direction == "encode":
    encrypt(text = text, shift = shift)
elif direction == "decode":
    decrypt(text = text, shift = shift)
else:
    print("Enter valid input")