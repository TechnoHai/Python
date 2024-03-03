import os
import subprocess

subprocess.call("cls", shell=True) # windows

def clear():
    return os.system('cls')  # on Windows System


print("hellow world")
clear()
print('\033[H\033[J', end='')
