#!/usr/bin/env python2
""" sounds from http://www.soundjig.com/pages/soundfx/drums.html"""
#from pyserial import Serial
from pandas import read_excel
import pygame
import numpy as np
from scipy.io.wavfile import read

def main(xls,rfidcode):
  
    data = read_excel(xls,index_col=0)
    
    wavfn = matchrfid(rfidcode,data)

    playmatch(wavfn)

def matchrfid(tagnum,data):
    return data.ix[tagnum,1]

def doplot(raw):
    from matplotlib.pyplot import figure,show
    ax= figure().gca()
    ax.plot(raw)
    show()
    
def playmatch(wavfn):
    fs,raw = read(wavfn)
    raw = np.atleast_2d(raw)
    r,c = raw.shape
    if r<c: raw = raw.T
    raw = raw[:20000,0] #mono, first 20000 samples
    sample_rate = 44100
    pygame.mixer.pre_init(sample_rate,size=-16,channels=1)
    pygame.mixer.init()
    sound = pygame.sndarray.make_sound((raw).astype(np.int16))
    print('sound length' + str(sound.get_length()) + 'seconds')
    sound.play(loops=0)
    
    doplot(raw)
    
if __name__ == '__main__':
    from sys import argv
    main('rfid2name.xlsx',int(argv[1]))
