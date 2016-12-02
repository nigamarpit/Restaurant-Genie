from os import environ, path,getcwd
from pocketsphinx import AudioFile, get_model_path, get_data_path
import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
	print("Say something!")
	audio = r.listen(source)

#with open('microphone-results.raw', 'wb') as f:
#	f.write(audio.get_raw_data())
with open("microphone-results.raw", "wb") as f:
	f.write(audio.get_wav_data())

model_path = getcwd()
data_path = getcwd()

config = {
	'audio_file': path.join(data_path, 'microphone-results.raw'),
	'hmm': path.join(model_path, 'model\\en-us'),
	'lm': path.join(model_path, 'model.bin'),
	'dict': path.join(model_path, '2859.dic')
}

audio = AudioFile(**config)
for phrase in audio:
    print(phrase)