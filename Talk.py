import pyttsx
engine = pyttsx.init()
engine.setProperty('rate', 120)

voices = engine.getProperty('voices')
engine.say("Hi there, how are you ?")
engine.runAndWait()
