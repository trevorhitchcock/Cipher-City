"""
Created on Sun Feb 12 17:59:19 2023

@author: Trevor Hitchcock
"""

def shift_cipher_menu():
    
    def shift_cipher_encrypt():
        plaintext = (input("\nEnter the text to be encrypted using a shift cipher: ")).lower()
        
        try:
            shift = int(input("Enter the shift amount: "))
            ciphertext = ""
            
            for i in range(0, len(plaintext)):
                char_val = ord(plaintext[i]) # grabs ASCII value
                if((char_val >= 97) and (char_val <= 122)): # only checking lowercase because string is made all lowercase
                    char_val = ((char_val - 97 + shift) % 26) + 97 # shifts the letter using mod 26
                    ciphertext = ciphertext + chr(char_val).upper() # adds to final ciphertext
            
            print("\nYour ciphertext for the plaintext \""+plaintext+"\" while using a shift of "+str(shift)+" is...")
            print(ciphertext)
        except TypeError:
            print("\nEnter an integer")
            shift_cipher_encrypt()
        shift_cipher_menu()
        
    def shift_cipher_decrypt():
        ciphertext = input("\nEnter the text to be decrypted: ")
        
        # changes string to all lowercase for printing
        ciphertext = ciphertext.lower()
        
        plaintext = ""
        
        for i in range(25, 0, -1): # 26 for each letter in the alphabet
            shift = i # for readability purposes
            print("\nThe ciphertext with a " + str(26 - shift) + " shift applied:")
            for j in range(len(ciphertext)):
                char_val = ord(ciphertext[j])
                if((char_val >= 97) and (char_val <= 122)): # char_val is a letter and not puncuation
                    char_val = ((char_val - 97 + shift)% 26) + 97
                    
                plaintext = plaintext + chr(char_val)
            print(plaintext)
            plaintext = ""
        
        shift_cipher_menu()
    
    print("\nWelcome to Shift Cipher!")
    print("1: Encrypt a message")
    print("2: Decrypt a message")
    print("3: Go to main menu")
    
    try:
        choice = int(input("Choose your option: "))
        
        if(choice == 1):
            shift_cipher_encrypt()
        elif(choice == 2):
            shift_cipher_decrypt()
        elif(choice == 3):
            print("\nExiting to main menu")
            main()
        else:
            print("")
            print("Invalid input")
            shift_cipher_menu()
    except ValueError:
        print("\nEnter an integer please")
        shift_cipher_menu()

def affine_cipher_menu():
    
    def affine_cipher_encrypt():
        plaintext = (input("\nEnter the text to be encrypted using an affine cipher: ")).lower()
        ciphertext = ""
        
        valid_alpha_inputs=[1,3,5,7,9,11,15,17,19,21,23,25]
        print("Valid inputs for alpha are "+str(valid_alpha_inputs))
        try:
            alpha = int(input("Enter alpha: "))
            
            if alpha in valid_alpha_inputs:
                print("Valid inputs for beta are integers between 0 and 26.")
                beta = int(input("Enter beta: "))
                if beta >= 0 and beta <=26:
                    # alpha and beta are valid
                    for i in range(0, len(plaintext)):
                        char_val = ord(plaintext[i]) # grabs ASCII value
                        if((char_val >= 97) and (char_val <= 122)): # only put letters into ciphertext
                            char_val = ((((char_val-97)*alpha) + beta)%26)+97 # affine cipher
                            ciphertext = ciphertext + chr(char_val).upper()
                    
                    print("\nYour ciphertext for the plaintext \""+plaintext+"\" while using α="+str(alpha)+" and β="+str(beta)+" is...")
                    print(ciphertext)
                else:
                    print("\nBeta input invalid")
                affine_cipher_menu()
            else:
                print("\nAlpha input invalid")
                affine_cipher_menu()
        except ValueError:
            print("\nEnter an integer")
            affine_cipher_menu()
            
    def affine_cipher_decrypt():
        try:
            ciphertext = input("\nEnter the text to decrypt using the affine cipher: ")
            alpha = int(input("Enter known α: "))
            beta = int(input("Enter known β: "))
            plaintext=""
            
            # this code finds alpha inverse
            alpha_inverse = 1
            total = 0
            
            while(total%26 != 1):
                alpha_inverse = alpha_inverse + 1
                total = alpha_inverse * alpha
            
            ciphertext = ciphertext.lower()
            if(ciphertext.isalpha()):
                for i in range(0, len(ciphertext)):
                    # written in 3 lines for readability
                    char_val = ord(ciphertext[i])-97
                    char_val = (char_val-beta)*alpha_inverse # inverse of (y=ax+b) == (y=(a^-1))(x-b)
                    char_val = char_val%26
                    # ensures char_val is between 0 and 25
                    while(char_val<0):
                        char_val = char_val+26
                        
                    char_val = char_val+97
                    plaintext = plaintext +chr(char_val).upper()
                    
                print("\nYour plaintext for the ciphertext \""+ciphertext+"\" while using α="+str(alpha)+" and β="+str(beta)+" is...")
                print(plaintext.lower())
            else:
                print("\nEnter only alphabet characters.")
            affine_cipher_menu()
                
        except ValueError:
            print("Enter an integer")
            affine_cipher_menu()
        
    print("\nWelcome to Affine Cipher!")
    print("1: Encrypt a message")
    print("2: Decrypt a message")
    print("3: Go to main menu")
    
    try:
        choice = int(input("Choose your option: "))
        if(choice == 1):
            affine_cipher_encrypt()
        elif(choice == 2):
            affine_cipher_decrypt()
        elif(choice == 3):
            print("\nExiting to main menu")
            main()
        else:
            print("\nInvalid input")
            shift_cipher_menu()
    except ValueError:
        print("\nEnter an integer please")
        shift_cipher_menu()

def vigenere_cipher_menu():
    
    def vigenere_cipher_encrypt():
        # THIS ISNT COMPLETE
        plaintext = (input("\nEnter the text to be encrypted using a Vigenère cipher: ")).lower()
        key = (input("Enter a key: ")).lower()
        key_ASCII = []
        
        # puts ASCII values -97 of key into the list
        for i in range(0, len(key)):
            key_val = ord(key[i])
            key_ASCII.append(key_val-97)
        print(key_ASCII)
        ciphertext = ""
        # LEAVE ONlY ALPHABET IN PLAINTEXT
        if(key.isalpha()): # key must be only letters
            for i in range(len(plaintext)):
                for j in key_ASCII:
                    print(j)
                    i=i+1
        else:
            print("\n Invalid key. Key must be only letters.")
            vigenere_cipher_menu()
        
        
        
        
        
    def vigenere_cipher_decrypt():
        print("Vigenère cipher decrypt doesn't work yet")
    
    
    print("\nWelcome to Vigenere Cipher!")
    print("1: Encrypt a message")
    print("2: Decrypt a message")
    print("3: Go to main menu")
    
    try:
        choice = int(input("Choose your option: "))
        
        if(choice == 1):
            vigenere_cipher_encrypt()
        elif(choice == 2):
            vigenere_cipher_decrypt()
        elif(choice == 3):
            print("\nExiting to main menu")
            main()
        else:
            print("")
            print("Invalid input")
            vigenere_cipher_menu()
    except ValueError:
        print("\nEnter an integer please")
        vigenere_cipher_menu()
    
def main():
    print("\nWelcome to Cipher City! Which cipher would you like to use?")
    print("1. Shift Cipher")
    print("2. Affine Cipher")
    print("3. Vigenere Chipher")
    print("4: End program")
    
    try:
        menu = int(input("Choose your option: "))
        if(menu == 1):
            shift_cipher_menu()
        elif(menu == 2):
            affine_cipher_menu()
        elif(menu == 3):
            vigenere_cipher_menu()
        elif(menu==4):
            print("\nProgram ending")
        else:
            print("\nInvalid input")
            main()
    except ValueError:
        print("\nEnter an integer")
        main()
    
main()
