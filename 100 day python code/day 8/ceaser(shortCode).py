alphabet  = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction = input("type 'encode' to encrypt, type 'decode' to decrypt : \n ")
text = input("Type your message :\n").lower()
shift  = int(input("Type shift Number :\n"))

def ceaser(start_text,shift_amount,cipher_direction):
    end_text = ""
    for letter in start_text:
        position = alphabet.index(letter)
        # if cipher_direction =='encode':
            # new_position = postiton + shift_amount
        if cipher_direction =='decode':
            shift_amount *= -1
        new_position = position + shift_amount    
        end_text += alphabet[new_position]
    print(f"The {cipher_direction}d text is {end_text} ")



ceaser(shift_amount=shift,start_text=text,cipher_direction=direction)  


