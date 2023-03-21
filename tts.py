from pygame import mixer
import pyttsx3
import getTextByWord
import os



engine = pyttsx3.init()


"""
mixer.init()
mixer.music.load("tmp/data.wav")
mixer.music.play()
"""
def generateAudioFile(text):
    if os.path.exists("C://users/{0}/tmpwavAoDev".format(os.getlogin())):
        pass
    else:
        os.mkdir("C://users/{0}/tmpwavAoDev".format(os.getlogin()))

    flushTemps()

    #say = getTextByWord.getText("fanf.docx")
    say = text
    voices = engine.getProperty('voices')
    # Задать голос по умолчанию
    engine.setProperty('voice', 'ru')
    # engine.setProperty('volume',1.0)
    engine.setProperty('rate', 230)  # setting up new voice rate
    engine.save_to_file(say, "c://users/{0}/tmpwavAoDev/data.wav".format(os.getlogin()))
    engine.runAndWait()



def play():
    stop()
    mixer.init()
    mixer.music.load("c://users/{0}/tmpwavAoDev/data.wav".format(os.getlogin()))
    mixer.music.play(loops=99999)



def stop():
    if (mixer.get_init()):
        mixer.music.stop()
        mixer.music.unload()
    else:
        pass

def flushTemps():
    if os.path.exists("C://users/{0}/tmpwavAoDev/data.wav".format(os.getlogin())):
        os.remove("C://users/{0}/tmpwavAoDev/data.wav".format(os.getlogin()))

def pause():
    mixer.music.pause()


def unpause():
    mixer.music.unpause()
