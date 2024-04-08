letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

def encrypt_decrypt(text, mode, key):
    result = ''
    num_letters = 26
    if mode == 'd':
        key = -key

    for letter in text:
        letter = letter.lower()
        if letter != ' ':
            index = letters.find(letter)
            if index == -1:
                result += letter
            else:
                new_index = index + key
                if new_index >= num_letters:
                    new_index -= num_letters
                elif new_index < 0:
                    new_index += num_letters
                result += letters[new_index]
        else:
            result += ' '  # Preserve spaces in the text
    return result

letters = 'abcdefghijklmnopqrstuvwxyz'

print('\n*** CAESAR CIPHER PROGRAM\n')

print('Do you want to encrypt or decrypt?')
user_input = input('e/d: ').lower()

if user_input == 'e':
    print('\nENCRYPTION MODE SELECTED\n')
    key = int(input('Enter the key (1 through 26): '))
    text = input('Enter the text to encrypt: ')
    ciphertext = encrypt_decrypt(text, user_input, key)
    print(f'CIPHERTEXT: {ciphertext}')

elif user_input == 'd':
    print('\nDECRYPTION MODE SELECTED\n')
    print()
    key = int(input('Enter the key (1 through 26): '))
    text = input('Enter the text to decrypt: ')
    plaintext = encrypt_decrypt(text, user_input, key)
    print(f'PLAINTEXT: {plaintext}')
