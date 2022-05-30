from PyPDF2 import PdfReader
import random
from pathlib import Path
from playsound import playsound
from conversation import Conversation
from Harold import typetext, speak, Harold
from threading import Thread
import time
import logging
import pygame


def kasparov_chess_glitch():
    ###if + check
    ###if # check mate
    modem_sound = Path(Path.cwd(), 'resources', 'chess', 'modem.wav')
    logging.debug(modem_sound.resolve())
    t = Thread(target=playsound, args=(str(modem_sound),))
    t.start()
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
    move = moves[random.randrange(0, len(moves),1)].strip('\n')
    expl = move_expl[random.randrange(0, len(move_expl),1)].strip('\n')
    logging.debug(move)
    logging.debug(expl)
    return


def main():
    logging.basicConfig(encoding='utf-8', level=logging.DEBUG)
    harry = Harold()
    harry.kasparov_chess_glitch()
    #typetext("I'm trying to add voice beeps into the dialogue of a certain character, so that whenever a letter of dialogue is displayed on the screen as scrolling text, a short sound clip is played, so as they speak a sentence, a rapid series of short beeps are played. Additionally I'd like it that when you skip the scrolling text to make the whole line appear at once, the beeping stops. "
    #         "I've read a few posts on this forum about adding voice beeps, and I've tried several variations of the solutions posted there, but none have worked for me as of yet. Here is my code right for it right now",
    #         0.05, harry)
    harry.check_yes_no_answer('Are you dumb?')


if __name__ == "__main__":
    main()