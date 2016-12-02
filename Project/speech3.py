import sys
import speech_recognition as sr
from os import environ, path,getcwd
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
	print("Say something!")
	audio = r.listen(source)

#with open('microphone-results.raw', 'wb') as f:
#	f.write(audio.get_raw_data())
with open("microphone-results.wav", "wb") as f:
	f.write(audio.get_wav_data())

	
DIR=getcwd()
#input(DIR)

config = Decoder.default_config()
config.set_string('-hmm', path.join(DIR, 'pocketsphinx-python\pocketsphinx\model\en-us'))
#config.set_string('-lm', path.join(DIR, 'pocketsphinx-python\pocketsphinx\model\en-us.lm.bin'))
#config.set_string('-dict', path.join(DIR, 'pocketsphinx-python\pocketsphinx\model\cmudict-en-us.dict'))
#config.set_string('-lm', path.join(DIR, 'LanguageModel\1945.lm'))
#input(path.join(DIR, 'LanguageModel\lm1945.dict'))
lm=path.join(DIR, 'model.bin')
d=path.join(DIR, '2859.dic')
#input(lm)
#input(d)
config.set_string('-lm',lm)
config.set_string('-dict',d)
config.set_string('-logfn','nul')
decoder = Decoder(config)
decoder.start_utt()
stream = open(path.join(DIR, 'microphone-results.wav'), 'rb')
while True:
	buf = stream.read(1024)
	if buf:
		decoder.process_raw(buf, False, False)
	else:
		break
decoder.end_utt()
#print(list(decoder.seg()))
print ('Best hypothesis segments: ', [seg.word for seg in decoder.seg()])
