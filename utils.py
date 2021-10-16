from mido import Message, MidiFile, MidiTrack, MetaMessage, bpm2tempo

import pandas as pd
import numpy as np
import os
from os import listdir, remove
from os.path import isfile, join


MIDI_DIR = '../Music'

def get_bad_files(files):
    bad_files = []
    for file in files:
        # print(song)
        mp = MidiProcessor(MIDI_DIR + '/' + file)
        found = False
        for i in range(len(mp.midi.tracks)):
            if mp.midi.tracks[i][0].channel == 9:
                found = True

        if not found:
            bad_files.append(song)
    return bad_files

def remove_files(files):
    for file in files:
        remove(FILES_DIR + '/' + file)
        

def get_files():
    return [f for f in listdir(MIDI_DIR) if isfile(join(MIDI_DIR, f))]
    
def get_good_files():
    file_list = get_files()
    remove_files(get_bad_files(file_list))
    
    return get_files()
    
    
class MidiProcessor:
    def __init__(self, midi_dir):

        self.midi_dir = midi_dir
        self.midi = MidiFile(self.midi_dir)
        self.drum_track_ind = [i for i in range(
            len(self.midi.tracks)) if self.midi.tracks[i][0].channel == 9][0]
#         self.meta_track = MidiFile(self.midi_dir).tracks[0]
        self.drum_track = self.midi.tracks[self.drum_track_ind]
#         self.meta_ind = [i for i, m in enumerate(self.meta_track) if 'numerator' in m.dict()][0]
#         self.numerator = self.meta_track[self.meta_ind].numerator
#         self.denominator = self.meta_track[self.meta_ind].denominator
        self.ticks_per_beat = self.midi.ticks_per_beat
        self.ticks_per_32nt = self.ticks_per_beat/8

    def midi_to_df(self):

        df = pd.DataFrame([m.dict() for m in self.drum_track])

        # get time passed since the first message and quantize
        df.time = [round(sum(df.time[0:i])/self.ticks_per_32nt)
                   for i in range(1, len(df)+1)]
        df = df[df.type == 'note_on']
        df = df.pivot_table(index='time', columns='note',
                            values='velocity', fill_value=0)

        # Fill empty notes
        df = df.reindex(pd.RangeIndex(df.index.max()+1)).fillna(0).sort_index()

        # if velocity > 0, change it to 1
        df = (df > 0).astype(int)
        df.columns = df.columns.astype(int)

        return df

    


    
