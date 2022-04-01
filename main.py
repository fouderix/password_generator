import random
import sys
import time

animation = "F%^^ù*µR|FO^ù*µR|FOU^ù*µR|FOUDù*µR|FOUDE*µR|FOUDERµR|FOUDERI%|FOUDERIX\n"

for i in range(8):
    time.sleep(0.1)
    sys.stdout.write("\r" + animation.split("|")[i])
    sys.stdout.flush()

animation = "P|PA|PAS|PASS|PASSW|PASSWO|PASSWOR|PASSWORD|PASSWORD |PASSWORD G|PASSWORD GE|PASSWORD GEN|PASSWORD GENE|PASSWORD GENER|PASSWORD GENERA|PASSWORD GENERAT|PASSWORD GENERATO|PASSWORD GENERATOR\n"

for i in range(18):
    time.sleep(0.1)
    sys.stdout.write("\r" + animation.split("|")[i])
    sys.stdout.flush()

how_many = input("Enter the lenght of the password: ")
symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789?,.;/:§!%ùµ*£$¨^+=}°)]0à@ç^_è`-|(['{\"#é~&"
password = ""



for letter in range(int(how_many)):
    password += random.choice(symbols)

animation = "|/-\\"
for i in range(10):
    time.sleep(0.1)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

print("Votre mot de passe est: " + password)