import os
import wave
name_in = input("File to convert to WAV?\n")
password = input("Symmetric Encryption Key?\n")
os.system("gpg --armor --symmetric --cipher-algo AES256 --batch --passphrase "+password+" "+name_in)
ciphername = name_in+".asc"
cipher = open(ciphername, "rb")
ciphertext = cipher.read()
audio = wave.open("cipher_audio.wav", "wb")
audio.setparams((2, 2, 44100, 1, 'NONE','not compressed'))
audio.writeframes(ciphertext)
