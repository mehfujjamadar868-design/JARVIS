import subprocess
# Used to start Windows applications


def open_notepad():
    # Opens Windows Notepad
    subprocess.Popen("notepad.exe")


def open_calculator():
    # Opens Windows Calculator
    subprocess.Popen("calc.exe")
