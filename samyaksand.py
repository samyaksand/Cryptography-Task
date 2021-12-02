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

print('\n')

# Caesar Cipher Decryption - Brute Force Way

message = 'OPXWODPSKQLONCXQNUJEOLXPWAEHMOUZOEQXXVKUJOWBLMWXPQUIOELPMYKYEHMOGOKYQXAXKYKDLYQZYLYHAWWBLMWXQYLWVWOY' 
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

# Output Text -STBASHTWOUPSRGBURYNISPBTAEILQSYDSIUBBZOYNSAFPQABTUYMSIPTQCOCILQSKSOCUBEBOCOHPCUDCPCLEAAFPQABUCPAZASC

print('\n')

from pycipher import Playfair
print(Playfair('ABCDEFGHIKLMNOPQRSTUVWXYZ').decipher('STBASHTWOUPSRGBURYNISPBTAEILQSYDSIUBBZOYNSAFPQABTUYMSIPTQCOCILQSKSOCUBEBOCOHPCUDCPCLEAAFPQABUCPAZASC'))

# Output - RSAENCRYPTNUMBERTWOHUNDREDFOURTYTHREEWITHNVALUEASTWOTHOUSANDFOURHUNDREDANDNINETEENANDEVALUEASELEVENX

print('\n')

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

