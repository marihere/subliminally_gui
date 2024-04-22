# This file contains the code responsible
# for the creation of the subliminal audio.

from gtts import gTTS
from pydub import AudioSegment
from librosa import *


def sub_creator(title, affs_txt, bg_path):

    # Generates a TTS audio file of the given affirmations
    gTTS(text=affs_txt, lang='en', slow=False).save('lib/.files/affs.wav')

    affs = AudioSegment.from_file('lib/.files/affs.wav')
    bg = AudioSegment.from_file(bg_path)

    length_affs = get_duration(path='lib/.files/affs.wav')
    length_bg = get_duration(path=bg_path)


    # If the affirmations' audio file is SHORTER
    # than the background's audio file, REPEAT
    # the affirmations' audio file until the
    # two lengths are equal or there's a small
    # difference between them.
    if length_affs < length_bg:
        x = int(length_bg / length_affs)

        affs = affs * x
        affs = affs.export('lib/.files/affs.wav')

    # If the affirmations' audio file is LONGER
    # than the background's audio file, SPED UP
    # the affirmations' audio file (by 1.25x) until the
    # two lengths are equal or there's a small
    # difference between them.
    elif length_affs > length_bg:
        i = 1
        speed = 1.25
        
        while length_affs > length_bg:
            length_affs /= speed

            i = i + 1
        
        affs = speed_change(affs, speed)
        affs.export('lib/.files/affs.wav', format='wav')
            

    affs = AudioSegment.from_file('lib/.files/affs.wav')
    affs = affs - 36 # Lower the volume by 36 dB.
    affs.export('lib/.files/quieter.wav', format='wav')

    affs = AudioSegment.from_file('lib/.files/quieter.wav')
    combined = bg.overlay(affs) # Overlay the affirmations' audio onto the background's audio.
    combined.export('subliminals/audios/' + title + '.wav', format='wav') # The subliminal audio is finally ready! :)

# Idk what this is but it works
def speed_change(sound, speed=1.0):
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={'frame_rate': int(sound.frame_rate * speed)})
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)

