# encryption.py
# AUTHOR NAME: Aaryan Sharma
#
# A terminal-based encryption application capable of both encoding and decoding text when given a specific cipher.
# Detailed specifications are provided via the Assignment 3 git repository.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.
import re

class Inputs:
    """
    The class is responsible for checking and cleaning the input strings. It has two functions, 'message' which will clean up the message input if the user decides to encode.
    """

    #For encoding
    def message(self,user_input):
        """
        The function is responsible for removing all the spaces, numbers, letters from the string and leaving only letters. It will also make all the letters lowercase
        :param user_input: what the user has entered for the message
        :return inp: will return the string that has been processed
        """

        #removing all spaces and symbols
        inp=re.sub(r'[\W_0-9]+', '',user_input)
        #making all the letters lowercase
        inp=inp.lower()
        print("The message after being processed is: ",inp)
        return inp

    def validate_cipher(self,cipher_input):
        """
        The function is responsible for checking if the string input for cipher has 26 characters, is all lowercase and just consists of numbers and lettersprompts the user to
        :param cipher_input: what the user has entered for the cipher
        :return cipher_input: what the user has entered for the cipher, this one will have met all the conditions
         """
        while True:
            try:
                #checking if the cipher consists just of just a   
                check=cipher_input.isalnum()
                check_2=cipher_input.islower()
                #if the conditions are not met, a value error will be raised and the user will be asked to input a cipher again
                if check==False or len(cipher_input)!=26 or check_2==False:
                    raise ValueError("Please enter cipher again")
            except ValueError as e:
                print(e)
                cipher_input=input("Enter the cipher: ")
            else:
                return cipher_input
                break
            

        
class DecEnc:
    """This class is responsible for encoding and decoding the input depending on what the user selects."""
    

    def encode(self,message_input,final_cipher):

        """The function will be responsible for encoding the input. It will do so by first creating a zipped file of alphabets and cipher input, which will then be converted into a dictionary. 
        A loop is created where 'e_text' will store the encoded message. 
        :param message_input: the message that has been processed
        :param final_cipher: what the user has entered for the cipher, the one that has met all the conditions
         """
        
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        #Zipping the cipher with correct order of the alphabets 
        e_zipped=zip(alphabet,final_cipher)#encode

        #Coverting the zipped file into a dictionary
        e_this_dict=dict(e_zipped)
       
       # Creating a loop that will help in storing  the characters of the encoded message in 'e_text'
        e_text=""
        for i in message_input:
         
            e_text+=e_this_dict[i]

        #If user had chosen to encode, this will be the final printed statement
        print("The encoded text is: ",e_text)
        

    def decode(self,message_input,final_cipher):

        """
        The function will be responsible for decoding the input. It will do so by first creating a zipped file of alphabets and cipher input, which will then be converted into a dictionary. 
        In the dictionary, the cipher_input will be before alphabet, opposite of what happened in encode(). A loop is created where 'd_text' will store the encoded message.
        :param message_input: the message that has been inputted by the user
        :param final_cipher: what the user has entered for the cipher, the one that has met all the conditions
        """

        alphabet = 'abcdefghijklmnopqrstuvwxyz'
         #Zipping the correct order of the alphabets with the cipher
        d_zipped=zip(final_cipher,alphabet)
        #Coverting the zipped file into a dictionary
        d_this_dict=dict(d_zipped)
        # Creating a loop that will help in storing  the characters of the decoded message in 'd_text'
        d_text=""
        for i in message_input:
            d_text+=d_this_dict[i]
        #If user had chosen to decode, this will be the final printed statement
        print("The decoded text is: ",d_text)


def main():
    """This function acts as the point of execution where functions from classes will be called"""
    print("ENSF 592 Encryption Program")

    message_input=input("Input the text to be encoded/decoded: ")

    #Creating an object of the Inputs class
    
    text=Inputs()
    cipher_input=input("Enter the cipher: ")
    final_cipher=text.validate_cipher(cipher_input)
     
    

    while True:
        
        #Ask to encode or decode
        enc_dec=input("Enter 1 to encode or 2 to decode your message: ")
        
         #Initiating Dec_Enc class
        d_e=DecEnc()

        #Encoding
        if enc_dec=="1":
            print("You have selected for the message to de encoded")
            #After the message is processed, it will be assigned to processed_input
            processed_input=text.message(message_input)
            #The processed input and cipher will go to the encode() function
            d_e.encode(processed_input,final_cipher)
            break
        
        #Decoding
        elif enc_dec=="2":
            print("You have selected for the message to de decoded")
            #The processed input and cipher will go to the decode() function
            d_e.decode(message_input,final_cipher)
            break

        else:
            print("Invalid number! Enter 1 to encode or 2 to decode your message ")  
            
if __name__ == '__main__':
    main()

