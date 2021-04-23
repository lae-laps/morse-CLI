import os
import sys
import time

dict = {
        "A" : ".-",
        "B" : "-...",
        "C" : "-.-.",
        "Ç" : "-.-..",
        "D" : "-..",
        "E" : ".",
        "F" : "..-.",
        "G" : "--.",
        "H" : "....",
        "I" : "..",
        "J" : ".---",
        "K" : "-.-",
        "L" : ".-..",
        "M" : "--",
        "N" : "-.",
        "Ñ" : "--.--",
        "O" : "---",
        "P" : ".--.",
        "Q" : "--.-",
        "R" : ".-.",
        "S" : "...",
        "T" : "-",
        "U" : "..-",
        "V" : "...-",
        "W" : ".--",
        "X" : "-..-",
        "Y" : "-.--",
        "Z" : "--..",
        "1" : "-.-..",
        "2" : "..---",
        "3" : "...--",
        "4" : "....-",
        "5" : ".....",
        "6" : "-....",
        "7" : "--...",
        "8" : "---..",
        "9" : "----.",
        "0" : "-----",
        "." : ".-.-.-",
        "," : "--..--",
        "/" : "-..-.",
        "¿" : "..-.-",
        "?" : "..--..",
        "-" : "-....-",
        "\"" : ".-..-.",
        "¡" : "--...-",
        "!" : "-.-.--",
        "=" : "-...-",
        "(" : "-.--.",
        ")" : "-.--.-",
        "@" : ".--.-.",
        ":" : "---...",
        "_" : "..--.-",
        "+" : ".-.-.",
        "'" : ".----.",
        "&" : ".-...",
        ";" : "-.-.-.",
        "$" : "...-..-",
    }

# FUNCTIONS
# =================================================================== #

def get_morse(char):
    if char in dict:
        morse_char = dict[char]
        return morse_char
    else:
        return "#"

def print_separar(text):
    split_text = text.split()
    for word in split_text:
        for char in word:
            morse_char = get_morse(char)
            print(morse_char, end="")
        print(" / ", end="")
    print()

def write_separar(text):
    morse = ""
    split_text = text.split()
    for word in split_text:
        for char in word:
            morse_char = get_morse(char)
            morse += morse_char + " "
        morse = morse + " / "
    return morse

def conditions(text, morse_list):
    if text == "/help":
        try:
            help = open("help.txt", "r")
            print(help.read())
            help.close()
        except:
            print("Couldn't open \"help.txt\"")

    elif text == "/exit":
        sure = str(input("Sure you want to exit? - (Y/n): "))
        sure = sure.lower()
        if sure == "y":
            print()
            print("Exiting... ")
            sys.exit(0)
        else:
            print(" - Not exiting - ")

    elif text == "/play":
        global morse_dt
        global morse_pitch

        print("playing", morse_list)

        for i in range(len(morse_list)):
            for char in morse_list[i]:
                if char == "-":
                    os.system('play -q -n synth %s sin %s' % (morse_dt, morse_pitch))
                    time.sleep(morse_dt/3)
                elif char == ".":
                    os.system('play -q -n synth %s sin %s' % (morse_dt/3, morse_pitch))
                    time.sleep(morse_dt/3)
                elif char == "/":
                    time.sleep(morse_dt*3)

    elif text == "/save":
        save = str(input("Save? (Y/n): "))
        save = save.lower()

        if save == "y":
            try:
                # Create/Open file
                if os.path.exists("morse.txt"):
                    print("Opening file...")
                    f = open("morse.txt", "w")
                else:
                    print("Creating file...")
                    f = open("morse.txt", "x")

                for i in range(len(morse_list)):
                    print("Saving line", i + 1, "of", len(morse_list))
                    f.write(morse_list[i],)
                    f.write("\n")

                print("Saving file...")
                f.close()
                print(" - File saved - ")
            except Exception as e:
                print('Could not open file "morse.txt"')
                print(e)

        elif save == "n":
            pass
        else:
            print("Not recognized. ")

    else:
        return False

try:
    title = open("help.txt", "r")
    print(title.read(536))
except:
    print("=================")
    print("MORSE - CONVERTER")
    print("=================")
    print()

morse_list = []

# Morse parameters
# Source: https://en.wikipedia.org/wiki/Morse_code
# Source: https://www.youtube.com/watch?v=xsDk5_bktFo

morse_dt = 0.18 # s
morse_pitch = 2000 # Hz

while(True):
    text = str(input("Input Unicode text >> "))
    test = conditions(text, morse_list)
    if test == False:
        text = text.upper()
        print_separar(text)
        morse_list.append(write_separar(text))
        continue
