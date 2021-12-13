alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
from art import logo
print(logo)
game = False
while not game:
    def caeser(text, shift, direction):
        plain_text = list(text)
        i = -1
        for letter in plain_text:
            i += 1
            if letter not in alphabet:
                plain_text[i] == letter
            else:
                position = alphabet.index(plain_text[i])
                if direction == "encode":
                    position += shift
                elif direction == "decode":
                    position -= shift
                new = position % 26
                cipher_text = alphabet[new]
                plain_text[i] = cipher_text 
        print(f"The encoded text is {''.join(plain_text)}")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(text, shift, direction)
    next_step = input("Type 'Yes' if you want to go again. Otherwise type 'No'. ").lower()
    if next_step ==  "yes":
        game == False
    if next_step == "no":
        print("Goodbye!")
        break
