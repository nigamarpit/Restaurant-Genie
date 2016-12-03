import os
import speech_recognition as sr
from pocketsphinx import AudioFile, get_model_path, get_data_path

model_path = os.getcwd()
data_path = os.getcwd()

def microphoneListen():
	r = sr.Recognizer()
	print('Listening...')
	with sr.Microphone() as source:
		audio = r.listen(source)
	print('Processing speech input...')
	with open('microphone-results.raw', 'wb') as f:
		f.write(audio.get_raw_data())

	config = {
		'audio_file': os.path.join(data_path, 'microphone-results.raw'),
		'hmm': os.path.join(model_path, 'model\\en-us'),
		'lm': os.path.join(model_path, 'model\\model.bin'),
		'dict': os.path.join(model_path, 'model\\7886.dic')
	}

	audio = AudioFile(**config)
	for phrase in audio:
		print(phrase)
		if len(str(phrase))==0:
			phrase=input()
		return str(phrase)
	#return ' '.join(l)
'''
import sys
import speech_recognition as sr
from os import environ, path,getcwd
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *

	# obtain audio from the microphone
def microphoneListen():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)

	#with open('microphone-results.raw', 'wb') as f:
	#	f.write(audio.get_raw_data())
	with open("microphone-results.wav", "wb") as f:
		f.write(audio.get_wav_data())

		
	DIR=getcwd()
	#input(DIR)

	config = Decoder.default_config()
	config.set_string('-hmm', path.join(DIR, 'model\\en-us'))
	#config.set_string('-lm', path.join(DIR, 'pocketsphinx-python\pocketsphinx\model\en-us.lm.bin'))
	#config.set_string('-dict', path.join(DIR, 'pocketsphinx-python\pocketsphinx\model\cmudict-en-us.dict'))
	#config.set_string('-lm', path.join(DIR, 'LanguageModel\1945.lm'))
	#input(path.join(DIR, 'LanguageModel\lm1945.dict'))
	lm=path.join(DIR, 'model\\model.bin')
	d=path.join(DIR, 'model\\2859.dic')
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
	words=list()
	[words.append(seg.word) for seg in decoder.seg()]
	print(' '.join(words[1:-1]))
	#print ('Best hypothesis segments: ', [seg.word for seg in decoder.seg()])
	'''