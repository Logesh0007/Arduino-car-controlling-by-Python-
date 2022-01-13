import pyfirmata
import time
from pyttsx3 import speak
from playsound import playsound
import keyboard

port = "COM3"
board = pyfirmata.Arduino(port)

Mot_L_Plus  = 5
Mot_L_Minus = 3
Mot_R_Plus  = 9
Mot_R_Minus = 6

if __name__ == "__main__":
    speak("welcome buddy")
    print("press SPACEBAR to start the engine ...")
    speak("press spacebar to start the engine")
    keyboard.wait("space")
    
    print("Engine starts")
    speak("engine starts")
    speak("please wear your seat belt, have a safe ride buddy")
    
    while 1:
        control = keyboard.read_key()
        # Forward
        if control == "w":
            speak("moving forward")
            board.digital[Mot_L_Plus].write(1)
            board.digital[Mot_L_Minus].write(0)
            board.digital[Mot_R_Plus].write(0)
            board.digital[Mot_R_Minus].write(1)

        # Reverse
        elif control == "s":
            speak("moving backward")
            board.digital[Mot_L_Plus].write(0)
            board.digital[Mot_L_Minus].write(1)
            board.digital[Mot_R_Plus].write(1)
            board.digital[Mot_R_Minus].write(0)

        # Left
        elif control == "a":
            speak("turning left side")
            board.digital[Mot_L_Plus].write(0)
            board.digital[Mot_L_Minus].write(0)
            board.digital[Mot_R_Plus].write(0)
            board.digital[Mot_R_Minus].write(1)

        # Right
        elif control == "d":
            speak("turning right side")
            board.digital[Mot_L_Plus].write(1)
            board.digital[Mot_L_Minus].write(0)
            board.digital[Mot_R_Plus].write(0)
            board.digital[Mot_R_Minus].write(0)

        # Stop
        elif control == "shift":
            speak("vehicle stopped")
            board.digital[Mot_L_Plus].write(0)
            board.digital[Mot_L_Minus].write(0)
            board.digital[Mot_R_Plus].write(0)
            board.digital[Mot_R_Minus].write(0)

        elif control == "esc":
            print("Engine OFF")
            speak("engine off, see you buddy")
            break
        
        
