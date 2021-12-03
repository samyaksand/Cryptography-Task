# Decoding QR Code

import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

decocdeQR = decode(Image.open('qrcode.jpg'))
print(decocdeQR[0].data.decode('ascii'))

# Output Text 
# R3JlYXQgam9iLiBKdWxpdXMgQ2Flc2VyIHdhcyBib3JuIGluIHRoZSAxMDAgQkM6ClBEQSBKQVRQIFlFTERBTiBHQVVPTVFXTkEgRU8gUERBIFdITERXWEFQTyBTRVBES1FQIEYKT1BYV09EUFNLUUxPTkNYUU5VSkVPTFhQV0FFSE1PVVpPRVFYWFZLVUpPV0JMTVdYUFFVSU9FTFBNWUtZRUhNT0dPS1lRWEFYS1lLRExZUVpZTFlIQVdXQkxNV1hRWUxXVldPWQ==

# -----------------------------------------------------------------------

# Base 64 Decryption

import base64
encoded = "R3JlYXQgam9iLiBKdWxpdXMgQ2Flc2VyIHdhcyBib3JuIGluIHRoZSAxMDAgQkM6ClBEQSBKQVRQIFlFTERBTiBHQVVPTVFXTkEgRU8gUERBIFdITERXWEFQTyBTRVBES1FQIEYKT1BYV09EUFNLUUxPTkNYUU5VSkVPTFhQV0FFSE1PVVpPRVFYWFZLVUpPV0JMTVdYUFFVSU9FTFBNWUtZRUhNT0dPS1lRWEFYS1lLRExZUVpZTFlIQVdXQkxNV1hRWUxXVldPWQ=="
data = base64.b64decode(encoded)
print(data)

# Encrypted Text - R3JlYXQgam9iLiBKdWxpdXMgQ2Flc2VyIHdhcyBib3JuIGluIHRoZSAxMDAgQkM6ClBEQSBKQVRQIFlFTERBTiBHQVVPTVFXTkEgRU8gUERBIFdITERXWEFQTyBTRVBES1FQIEYKT1BYV09EUFNLUUxPTkNYUU5VSkVPTFhQV0FFSE1PVVpPRVFYWFZLVUpPV0JMTVdYUFFVSU9FTFBNWUtZRUhNT0dPS1lRWEFYS1lLRExZUVpZTFlIQVdXQkxNV1hRWUxXVldPWQ==
# Output Text

# Great job. Julius Caeser was born in the 100 BC:
# PDA JATP YELDAN GAUOMQWNA EO PDA WHLDWXAPO SEPDKQP F
# OPXWODPSKQLONCXQNUJEOLXPWAEHMOUZOEQXXVKUJOWBLMWXPQUIOELPMYKYEHMOGOKYQXAXKYKDLYQZYLYHAWWBLMWXQYLWVWOY

print('\n')

# -----------------------------------------------------------------------

# Caesar Cipher Decryption - Brute Force Way

message = 'PDA JATP YELDAN GAUOMQWNA EO PDA WHLDWXAPO SEPDKQP F' 
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  

for key in range(len(LETTERS)):  
        translated = ''  
   
        for symbol in message: 
                if symbol in LETTERS:  
                        n = LETTERS.find(symbol)  
                        n = n - key  
                        if n < 0:  
                                n = n + len(LETTERS)  
                        translated = translated + LETTERS[n]  
         
        
                else:  
                        translated = translated + symbol  
      
        print('Hacking k #%s: %s' % (key, translated))

# Encrpted Text - PDA JATP YELDAN GAUOMQWNA EO PDA WHLDWXAPO SEPDKQP F
# Output - THE NEXT CIPHER KEYSQUARE IS THE ALPHABETS WITHOUT J

print('\n------------------Decrypted Message found using key 22------------------')
print('THE NEXT CIPHER KEYSQUARE IS THE ALPHABETS WITHOUT J')
print('\n')

# Caesar Cipher Decryption using Key
shift = 22 
encrypted_text = "OPXWODPSKQLONCXQNUJEOLXPWAEHMOUZOEQXXVKUJOWBLMWXPQUIOELPMYKYEHMOGOKYQXAXKYKDLYQZYLYHAWWBLMWXQYLWVWOY"
plain_text = ""

for c in encrypted_text:
    if c.isupper():
        c_unicode = ord(c)
        c_index = ord(c) - ord("A")

        new_index = (c_index - shift) % 26
        new_unicode = new_index + ord("A")

        new_character = chr(new_unicode)

        plain_text = plain_text + new_character

    else:

        plain_text = plain_text + c

print("Encrypted Text:",encrypted_text)

print("Decrypted Text:",plain_text)

print('\n')


from pycipher import Playfair
print(Playfair('ABCDEFGHIKLMNOPQRSTUVWXYZ').decipher('STBASHTWOUPSRGBURYNISPBTAEILQSYDSIUBBZOYNSAFPQABTUYMSIPTQCOCILQSKSOCUBEBOCOHPCUDCPCLEAAFPQABUCPAZASC'))

# Output - RSAENCRYPTNUMBERTWOHUNDREDFOURTYTHREEWITHNVALUEASTWOTHOUSANDFOURHUNDREDANDNINETEENANDEVALUEASELEVENX

print('Formatted Text - RSA ENCRYPT NUMBER TWO HUNDRED FOURTY THREE WITH N VALUE AS TWO THOUSAND FOUR HUNDRED AND NINETEEN AND E VALUE AS ELEVEN X')

print('\n')
import math

c = 243
d = 11
N = 2419

print('Given from the previous message \n')
print("N               : ", N)
print("C (Cipher Text) : ", c)
print("d (Key)         : ", d)
print('\n')
message = pow(c, d, N)
print("Decrypted Message (using the formula m = C^d(mod N)): ", message)

print('\n')


# Caesar Cipher Conversion can be done using libraries
# from pycipher import Caesar

# print(Caesar(key=5).decipher('TM, DTZ KTZSI RJ. HTSLWFYX. YMNX NX YMJ JSILTFQ. TW NX NY?'))
# print('\n')
# Output - OHYOUFOUNDMECONGRATSTHISISTHEENDGOALORISIT

print('--------------In dontsee.txt document-------------------\n')


shift = 5 
encrypted_text = "TM, DTZ KTZSI RJ. HTSLWFYX. YMNX NX YMJ JSILTFQ. TW NX NY?"
plain_text = ""

for c in encrypted_text:
    if c.isupper():
        c_unicode = ord(c)
        c_index = ord(c) - ord("A")

        new_index = (c_index - shift) % 26
        new_unicode = new_index + ord("A")

        new_character = chr(new_unicode)

        plain_text = plain_text + new_character

    else:

        plain_text = plain_text + c

print("Encrypted Text:",encrypted_text)

print("Decrypted Text:",plain_text)


print('\n')

print('Decrypted Formatted Text : OH, YOU FOUND ME. CONGRATS. THIS IS THE ENDGOAL. OR IS IT?')
