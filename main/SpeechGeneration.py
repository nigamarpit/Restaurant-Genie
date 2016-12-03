import win32com.client as wincl

speak = wincl.Dispatch("SAPI.SpVoice")
def SpeechOutput(str):	
	print(str)
	speak.Speak(str)
#speak.Speak("I found following restaurants near you!")
#speak.Speak("I found 20 restuarant that serve Italian food near your locality. Out of which 13 are highly rated and 6 of them are cheap with price range of $15 per person.")
#speak.Speak("The most preferred restaurants based on rating are:")