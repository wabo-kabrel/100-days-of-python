alphabet = "abcdefghijklmnopqrstuvwxyz"

def encrypt():
    encrypted_message = ""
    message = input("Enter the message you want to encrypt: \n").lower()
    key = int(input("Enter the shift key: \n"))

    for letter in message:
        if letter in alphabet:
            old_index = alphabet.index(letter)
            new_index = (old_index + key) % len(alphabet)
            encrypted_message += alphabet[new_index]

        else:
            encrypted_message += letter

    print(f"The encrypted message is: {encrypted_message}")

def decrypt():
    decrypted_message = ""
    message = input("Enter the message you want to decrypt: \n")
    key = int(input("Enter the shift key: \n"))

    for letter in message:
        if letter in alphabet:
            old_index = alphabet.index(letter)
            new_index = (old_index - key) % len(alphabet)
            decrypted_message += alphabet[new_index]

        else:
            decrypted_message += letter

    print(f"The decrypted message is: {decrypted_message}")

should_continue = True

while should_continue:
    choice = input("Enter \"encode\" if you want to encrypt a message and \"decode\" if you want to decrypt a message: ").lower() 

    if choice == "encode":
        encrypt()

    elif choice == "decode":
        decrypt()

    else: 
        print("Invalid choice.")

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'. \n").lower()

    if restart == 'no':
        should_continue = False
        print("Good bye!")