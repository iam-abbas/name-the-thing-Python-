import speech_recognition as sr
import pyttsx3
from PIL import Image
from random import randint


run = True

while run:
   stuff = ["car", "truck", "plane"]
   obj = stuff[randint(0, 2)]
   file_name = "things/"+obj+".png"

   image = Image.open(file_name)
   image.show()

   r = sr.Recognizer()
   with sr.Microphone() as source:
       print("Tell Me What is it?")
       audio = r.listen(source)

   text = r.recognize_google(audio)

   if obj in text:
       print("Great \n \n You Said:", text)
   else:
       run = False
       print(text)
