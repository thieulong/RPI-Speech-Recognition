# Using pyttsx3 (Not recommended)

# import pyttsx3

# engine = pyttsx3.init()

# voices = engine.getProperty("voices")

# engine.setProperty("rate", 175)
# # engine.setProperty("voice", voices[-1].id)

# text = "Hello there how can I help you"

# engine.say(text)

# engine.runAndWait()

# Using espeak (Recommended)

import subprocess

def execute_unix(text):
   command = 'espeak -ven+m3 -k5 -s150 --punct="<characters>" "%s" 2>>/dev/null' % text
   p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
   (output, err) = p.communicate()
   return output

# a = "Ok sir, the light is now turned on"

# create wav file
# w = 'espeak -w temp.wav "%s" 2>>/dev/null' % a  
# execute_unix(w)

# tts using espeak
# c = 'espeak -ven+f3 -k5 -s150 --punct="<characters>" "%s" 2>>/dev/null' % a 
execute_unix("Ok sir, the light is now turned on")

