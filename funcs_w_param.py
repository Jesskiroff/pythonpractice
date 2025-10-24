# def greet():
#     print("Hello")
#     print("My name is Jessica")
#     print("What up what up?!")

# def greet_w_name(name, time_zone):
#     print(f"Hello {name}. Do you know that you're in the {time_zone} time zone now?")

# greet_w_name(time_zone="Eastern",name= "Audrey")

alphabet = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
]

direction = input("Type 'encode' to encrypt or 'decode' to decrypt: \n").lower() #This is the direction of the shift (whether it'll be a shift to the right or left of the chosen letter)
text = input ("Type your message here:\n").lower() #This is the original text that the user types in
shift_number= int(input("Type the shift number: \n")) #This is the number of letters the message will either encrypt or decrypt into

# 1. create a function called encrypt() that takes text and shift_number as 2 inputs

# 2. Inside the 'encrypt' func, shift each letter of the original_text forwards in the alphabet by the shift amount 
#and print the encrypted text


'''def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
       shifted_position = alphabet.index(letter) + shift_amount
       shifted_position %= len(alphabet)
       cipher_text += alphabet[shifted_position]

    print(f"Here is the result: {cipher_text}")'''
# 3. Create a function called decrypt() that takes 'original_text' and 'shift_amount' as 2 seperate inputs

'''def decrypt (original_text, shift_amount):
    output_text = ""
    for letter in original_text:
       shifted_position = alphabet.index(letter) - shift_amount
       shifted_position %= len(alphabet)
       output_text_text += alphabet[shifted_position]
    print(f"Here is the result: {output_text}")'''


# 4. Inside the decrypt function, shift each letter of the original text in the alphabet backwards by the shift_amount and printthe decrypted text
# 5. combine the encrypt func and decrypt func into a c=single function called caesar(), use the vlaue of the userchosen direction variable to determine 
#    which functionality to use, call the caesar function instead of the encrypt function and pass in all 3 variables: direction, text, and shift.
    
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    for letter in original_text:
       if encode_or_decode =="decode":
           shift_amount = -shift_number
       shifted_position = alphabet.index(letter) + shift_amount
       shifted_position %= len(alphabet)
       output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")
# encrypt(original_text= text, shift_amount= shift_number)
#decrypt(original_text= text, shift_amount= shift_number) 

caesar(original_text= text, shift_amount= shift_number, encode_or_decode= direction)