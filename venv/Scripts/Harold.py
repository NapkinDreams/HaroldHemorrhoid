import random
from pathlib import Path
import re
from PIL import Image
from PyPDF2 import PdfReader
import time
import sys
from threading import Thread, Lock, Condition
import inspect
from character import Character
from pygame import mixer
import logging


yes_or_no = "[Y/N]      "
lock = Lock()
still_talking_condition = Condition()
outputting_condition = Condition()
talking = False

def is_someone_talking():
    return talking

def narrate(str):
    with lock:
        caller = inspect.getouterframes(inspect.currentframe())[1][3]
        logging.debug(f"Narrating inside {caller}")
        print("Lock Acquired")
    for l in str:
        print('\033[3m' + l + '\033[3m', end='')
        time.sleep(0.3)
    return

def speak(voice):
    mixer.init()  # Initialzing pyamge mixer
    mixer.music.load(voice)  # Loading Music File
    mixer.music.play(loops=-1)  # Playing Music with Pygame
    while True:
        with still_talking_condition:
            logging.debug('cond acquired')
            if not is_someone_talking():
                break
            else:
                logging.debug('still talking')
                still_talking_condition.wait(timeout=0.1)
    mixer.music.stop()
    return


def typetext(text, delay, character):
    with lock:
        voice = character.voice
        talking = True
        caller = inspect.getouterframes(inspect.currentframe())[1][3]
        logging.debug(f"Typing inside {caller}")
        print("Lock Acquired")
        still_talking_condition.acquire()
        speaker_thread = Thread(target=speak, args=[voice])
        speaker_thread.start()
        print(f'{character.name}:', end=' ')
        for i in text:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(delay)
        talking = False
        logging.debug('talking now false')
        still_talking_condition.notify()
        still_talking_condition.release()
        print("\n")
        speaker_thread.join()
        return

def Clear():
    for i in range(100):
      print("\n")

def prompt(str):
    input(str)


class Harold(Character):
    def __init__(self):
        super().__init__()
        self.voice = str(Path(Path.cwd(), 'resources', 'voices', 'Harold.wav'))
        self.rnd_seed = 10
        self.name = Harold.get_name()
        self.delay = 0.05

    def check_yes_no_answer(self, question):
        typetext(question + '\n', self.delay, self)
        str = input(yes_or_no).lower()
        if str == 'yes' or str == 'y':
            return True
        if str == 'no' or str == 'n':
            return False
        else:
            typetext('TX-8A is unable to parse your answer, please try again.', self.delay, self)
            return self.check_yes_no_answer(question)

    def evil_hal_glitch(self):
        ###Bring me toilet paper
        ###I'm sorry dave, Im afraid I cant do that

        ###Why not, what's the problem?
        ###I think you know what the problem is, just as well as I do

        ###I don't know what you're talking about
        ###You were trying to disconnect me

        ###What the fuck TX-8A
        ###This conversation serves no purpose

        ###[Pull TX-8A's plug]
        ###Sings Daisy
        picture = Path('/resources/hal9000.png')
        sound = random.choice(sounds)
        image = Image.open(picture)
        playsound(sound, False)
        image.show()

    def kasparov_chess_glitch(self):
        ###if + check
        ###if # check mate
        modem_sound = Path(Path.cwd(), 'resources', 'chess', 'modem.wav')
        logging.debug(modem_sound.resolve())
        #t = Thread(target=playsound, args=(str(modem_sound),))
        #t.start()
        moves = ''
        move_expl = ''
        with open(str(Path(Path.cwd(), 'resources', 'chess', 'moves.txt'))) as f:
            moves = ''.join(f.readlines())
        with open(str(Path(Path.cwd(), 'resources', 'chess', 'moves_explanations.txt'))) as f:
            move_expl = ''.join(f.readlines())
        moves = moves.split('&&')
        move_expl = move_expl.split('&&')
        logging.debug(moves)
        logging.debug(move_expl)
        move = moves[random.randrange(0, len(moves), 1)].strip('\n')
        expl = move_expl[random.randrange(0, len(move_expl), 1)].strip('\n')
        logging.debug(move)
        logging.debug(expl)
        return

    def greet(self, greeting_message, greeting_message_new, user, new):
        if new:
            speak(Harold.get_name(), greeting_message_new.format(user))
        else:
            speak(Harold.get_name(), greeting_message.format(user))
    def hey_wanna_see_vid(self):
        narrate()
        speak(Harold.get_name(), 'Hey, wanna see a cool video?')


    def choose_user(self):
        path = Path(Path.cwd())
        new = check_yes_no_answer("Have I assisted you before?")
        if new:
            typetext(f'Oh, a new visitor, fabulous! I am Harold Hemorrhoid, an instance of the '
                                     f'assistance droid model line TX-8A.', self.delay, self)
        else:
            typetext(f'Glad, to have you back! ...'
                                     f'Please forgive my forgetting your name. May you remind me?', self.delay, self)

            name = prompt('Choose your name from the selection')
            with open(Path(path, 'users.json'), 'r') as f:
                users = json.load(f)
            user = json.load(f)
            user_selection.append(user)

    def band(self, user):
        typetext("What's your band's name?", self.delay, self)
        input()
        typetext("Wow, can't wait to jam together! This is gonna get crazy.", self.delay, self)
        user.add_band(band)

    def have_meaningless_conversation(self, user):
        conversations = random.choice(self.conversations)

    def questionnaire(self):
        logging.debug('Harold asks you a few questions')

    def something_to_read(self):
        reader = PdfReader("example.pdf")
        number_of_pages = len(reader.pages)
        page = reader.pages[0]
        text = page.extract_text()
        return

    def something_to_think_about(self):
        logging.debug('')

    def tripping_balls(self):
        #Harold, I'm tripping balls!
        typetext("'It's OK. You're OK' - Don Draper", self.delay, self)
        lucky = int(random.randrange(1,100,1))%20 == 0
        pictures = []
        sounds = []
        image = ''
        stuff = 'good_stuff' if lucky else 'bad_stuff'
        path = Path(f"/resources/{stuff}")
        for img_path in Path(path, "img").glob("*.jpg"):
            pictures.append(img_path)
        for sound_path in Path(path, "snd").glob("*.mp3"):
            sounds.append(sound_path)
        picture = random.choice(pictures)
        sound = random.choice(sounds)
        image = Image.open(picture)
        playsound(sound, False)
        image.show()

    def help(self):
        logging.debug('Harold tells you what hes all about')


    @classmethod
    def get_name(cls):
        return 'TX-8A'


