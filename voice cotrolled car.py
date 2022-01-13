import pyfirmata
import time
from pyttsx3 import speak
import speech_recognition as sr
from playsound import playsound

port = "COM3"
board = pyfirmata.Arduino(port)

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio,language='en-in')
    
    except Exception as e:
        print(e)
        speak("say that again please")
        return 'None'
    return query

Mot_L_Plus  = 5
Mot_L_Minus = 3
Mot_R_Plus  = 9
Mot_R_Minus = 6

if __name__ == "__main__":
    speak("welcome buddy")
    while 1:
        control = command()

        if control in ["engine start", "start the engine"]:
            print("Engine starts")
            playsound.playsound("Engine_on.mp3")
            speak("engine starts")
            speak("please wear your seat belt, have a safe ride buddy")
        
        # Forward
        elif control in ["move forward", "forward", "go front", "accelerate", "go forward"]:
            speak("moving forward")
            board.digital[Mot_L_Plus].write(1)
            board.digital[Mot_L_Minus].write(0)
            board.digital[Mot_R_Plus].write(0)
            board.digital[Mot_R_Minus].write(1)

        # Reverse
        elif control in ["move backward", "backward", "go back", "reverse", "take reverse"]:
            speak("moving backward")
            board.digital[Mot_L_Plus].write(0)
            board.digital[Mot_L_Minus].write(1)
            board.digital[Mot_R_Plus].write(1)
            board.digital[Mot_R_Minus].write(0)

        # Left
        elif control in ["take left", "turn left", "go left", "left"]:
            speak("turning left side")
            board.digital[Mot_L_Plus].write(0)
            board.digital[Mot_L_Minus].write(0)
            board.digital[Mot_R_Plus].write(0)
            board.digital[Mot_R_Minus].write(1)

        # Right
        elif control in ["take right", "turn right", "go right", "right"]:
            speak("turning right side")
            board.digital[Mot_L_Plus].write(1)
            board.digital[Mot_L_Minus].write(0)
            board.digital[Mot_R_Plus].write(0)
            board.digital[Mot_R_Minus].write(0)

        # Stop
        elif control in ["stop it", "stop", "put the break", "stop the vehicle"]:
            speak("vehicle stop")
            board.digital[Mot_L_Plus].write(0)
            board.digital[Mot_L_Minus].write(0)
            board.digital[Mot_R_Plus].write(0)
            board.digital[Mot_R_Minus].write(0)

        elif control in ["engine off", "switch off the engine"]:
            print("Engine OFF")
            speak("engine off", "see you buddy")
            break
        
        
