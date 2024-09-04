letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

def encrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                new_index = (index + key) % num_letters
                ciphertext += letters[new_index]
        else:
            ciphertext += ' '
    return ciphertext
 

print()
print('CAESER CIPHER TASK 1')
print()

print('Do you want to encrypt or decrypt ?')
user_input = input('e/d: ').lower()
print() 

if user_input == 'e': 
    print('ENCRYPTION MODE SELECTED')
    print()
    key = int(input('Enter the key: '))
    text = input('Enter the text to encrypt: ')
    ciphertext = encrypt(text, key)
    print(f'CIPHERTEXT: {ciphertext}')

elif user_input == 'd':
    print('DECRYPTION MODE SELECTED')
    print()
    key = int(input('Enter the key: '))
    text = input('Enter the text to decrypt: ')
    plaintext = decrypt(text, key)
    print(f'PLAINTEXT: {plaintext}')