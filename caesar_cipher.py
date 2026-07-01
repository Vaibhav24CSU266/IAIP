def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():

            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)

        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


while True:

    print("\n===== Caesar Cipher Tool =====")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        text = input("Enter text: ")
        shift = int(input("Enter shift value: "))

        encrypted = encrypt(text, shift)
        print("Encrypted Text:", encrypted)

    elif choice == "2":
        text = input("Enter encrypted text: ")
        shift = int(input("Enter shift value: "))

        decrypted = decrypt(text, shift)
        print("Decrypted Text:", decrypted)

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid Choice")
