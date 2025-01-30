import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)

# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter)+shift_amount
#         shifted_position %= len(alphabet) # i.e z index = 25 + shift = 2 so 27 % 25 = 2 
#         cipher_text += alphabet[shifted_position]
#     print(cipher_text)
# encrypt(original_text= text, shift_amount = shift)

# def decrypt(original_text, shift_amount):
#     decoded_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) - shift_amount
#         decoded_text += alphabet[shifted_position]
#     print(decoded_text)

# decrypt(original_text = text, shift_amount = shift)

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if direction == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter)+shift_amount
            shifted_position %= len(alphabet) # i.e z index = 25 + shift = 2 so 27 % 25 = 2 
            output_text += alphabet[shifted_position]
    print(f"Here is your {encode_or_decode}d text: {output_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, and type 'decode' to decrypt. \n")
    text = input("Type your message \n").lower()
    shift = int(input("Type the shift number \n"))
    
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    restart = input("Type 'yes' if you want to continue. Otherwise 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print('Goodbye.')
