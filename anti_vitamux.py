import os
import wave
cipher_audio=input("WAV file to decode?\n")
password = input("Passphrase for decrypt?\n")
audio = wave.open(cipher_audio, "rb")
stegimage = audio.readframes(audio.getnframes())
image_out = open("converted_steg.asc", "wb")
image_out.write(stegimage)
os.system("gpg --output decytped_file -d --batch --passphrase "+password+" converted_steg.asc")
