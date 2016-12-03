# Restaurant Genie: Voice Assistant for Restaurants

Restaurant GENIE is an interface that assists the users to choose restaurants based on their preferences.

- [Working](#working)
- [Domain](#domain)
- [Pre-requisites](#pre-requisites)
- [How to Execute](#execution)

## Working
It follows the complete spoken dialog architecture which includes the following components:
>- Speech Recognition
>- Natural Language Understanding
>- Dialog Manager
>- Natural Language Generation
>- Speech Synthesis

## Domain

At present user can ask question related to restaurants based upon following preferences:
- Cuisine
- Price
- Location
- Rating

## Pre-requisites

- [CMU Spinx](http://cmusphinx.sourceforge.net/)
- [CMU language modelling toolkit](http://www.speech.cs.cmu.edu/tools/lmtool.html)
- [Python Speech Recognition](https://pypi.python.org/pypi/SpeechRecognition/2.1.3)
- [PyAudio](https://pypi.python.org/pypi/PyAudio)
- [CMU PocketSphinx](https://github.com/cmusphinx/pocketsphinx)
- [Python pywin32](https://pypi.python.org/pypi/pywin32)


## Execution
Run following command from the console

`>python DailogueManager.py`
