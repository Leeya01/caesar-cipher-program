
# Name: Leeya01
# A Caesar Cipher Program

import os.path

def welcome():
    # introduction to the user
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher.")
    return

def enter_message():
    #determine the mode of conversion 
    mode = ''
    message = ''
    shift = 0
    mode = input("Would you like to encrypt (e) or decrypt (d):")
    while mode not in ['e', 'd']:
        print("INVALID MODE")
        mode = input("Would you like to encrypt (e) or decrypt (d): ")
    #Prompt users to select a mode 
    if mode == 'e':
        message = input("What message would you like to encrypt:")
    elif mode == 'd':
        message = input("What message would you like to decrypt:")
    message = message.upper()
    shift = int(input("What is the shift number:"))

    return (mode, message, shift)

def encrypt(message,shift):
    #encrypt the message as appropriate and print the output.
    message = message.upper()
    result = ''
    
    for char in message:
        if char.isalpha():
            #deals with underflows/overflows
            new_ascii_index = ord(char) + shift
            if (new_ascii_index > 90):
                new_ascii_index = new_ascii_index -26
            #--------------------------
            result = result + chr(new_ascii_index)
        else:
            result = result + char

            
    return result

def decrypt(message,shift):
    #decrypt the message as appropriate and print the output.
    message = message.upper()
    result = ''
    
    for char in message:
        if char.isalpha():
            #deals with underflows/overflows
            new_ascii_index = ord(char) - shift
            if (new_ascii_index < 65):
                new_ascii_index = new_ascii_index + 26
            #--------------------------
            result = result + chr(new_ascii_index)
        else:
            result = result + char
            
    return result


def process_file(filename, mode,shift):
    list_messages = []
    file = open(filename, 'r')
    for line in file:
        if(mode == 'e'):
            line = encrypt(line, shift)
        else:
            line = decrypt(line, shift)
        list_messages.append(line)
    file.close()
    return list_messages

def write_messages(lines):
    with open('results.txt', 'w') as output_file:
        for line in lines:
            output_file.write(line + '\n')
    output_file.close()

# Example usage:
lines = ['abc', 'def', '123']
write_messages(lines)


def is_file(filename):
    return os.path.exists(filename)


def message_or_file():
    mode = ''
    filename = None
    message = None
    shift = 0

    # Prompt users to select a mode
    mode = input("Would you like to encrypt (e) or decrypt (d): ")
    while mode not in ['e', 'd']:
        print("INVALID MODE")
        mode = input("Would you like to encrypt (e) or decrypt (d): ")

    # Prompt users to select input mechanism
    read_type = input("Would you like to read from a file (f) or the console (c)? ")
    while read_type not in ['f', 'c']:
        print("INVALID MODE")
        read_type = input("Would you like to read from a file (f) or the console (c)? ")

    if read_type == "c":
         # If console input, prompt for message
        if mode == 'e':
            message = input("What message would you like to encrypt: ")
            shift = int(input("What is the shift number"))
            encrypt(message,shift)

        elif mode == 'd':
            message = input("What message would you like to decrypt: ")
            shift = int(input("What is the shift number"))
            decrypt(message,shift)

    else:
        # If file input, prompt for filename and check if the file exists
        while True:
            filename = input("Enter a filename: ")
            if is_file(filename):
                break
            else:
                print("INVALID FILENAME")
                #filename = input("Enter a filename: ")
        while True:
            shift = int(input("What is the shift number"))
            if(shift>0 and shift<26):
                break
            else:
                print("INVALID SHIFT")
        process_file(filename,mode,shift)

       
            #process_file(filename,mode,shift)

    return mode, message, filename, shift



def main():
    # WELCOME USER:
    welcome()
    result=''
    #Prompt users to select a mode
    while True:
        mode, message, shift = enter_message() 
        
        #encrypt (e) or decrypt (d)
        if  (mode == 'e'):
            result = encrypt(message, shift)
            
        elif (mode =='d'):
            result = decrypt(message, shift)
 
        print(result)
        write_messages(lines)

        message = input("Would you like to encrypt or decrypt another message? (y/n):")
        while message not in ['y', 'n']:
            message = input("Would you like to encrypt or decrypt another message? (y/n): ")
            
        if  (message == 'y'):
            mode, message, shift = enter_message() 
            
            #encrypt (e) or decrypt (d)
            if  (mode == 'e'):
                result = encrypt(message, shift)
                
            elif (mode =='d'):
                result = decrypt(message, shift)
    
            print(result)
            write_messages(lines)
            
        elif (message == 'n'):
            print("Thanks for using the program, goodbye!")
            break
    return


# Program execution begins here
if __name__ == '__main__':
    main()

    #a_list = process_file('messages.txt', 'e', 2)
    #print(a_list)
   # write_messages(lines)
   #message_or_file()