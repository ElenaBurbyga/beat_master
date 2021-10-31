My Final project at Lighthouse Labs data science boot camp

## Beat Master

In my project I created a deep learning model, that creates original drum tracks, based on particular music style or music band. 

Model : 

For my project I used the LSTM and BiLSTM model by Keras. LSTM gave me a better result.

LSTM deep learning model is the type of the model that can efficiently learn via gradient descent. Using a gating mechanism, LSTMs are able to recognize and encode long-term patterns. It is very useful when the network has to remember information for a long period of time as is the case in music generation.

A Bidirectional LSTM, or BiLSTM, is a sequence processing model that consists of two LSTMs: one taking the input in a forward direction, and the other in a backwards direction.

Data preparation: 

For my project I used MIDI files. Rather than representing musical sound directly, it transmits information about how music is produced. The command set includes note-ons, note-offs, key velocity, pitch bend and other methods of controlling a synthesizer. Since a MIDI file only represents player information, it is far more concise than formats that sound directly, and easy readable by human. Another advantage is very small size.

To work with MIDI files I used Mido library (Python). Mido parses MIDI file as an object, which consist of several tracks, and each track contains all the notes of one instrument.

To create a data set first I had to to quantization and simplification of the data. Quantization is the process of converting a continuous analog audio signal to a digital signal with discrete numerical value. In simple worlds making music mathematically perfect. And then by simplification I mean limiting the type of notes, instruments and commands. 
In very simple words I created a data set, where features were instruments, and values – 1 when note is on, and 0 when its off.



Files:

Utils - contains all the helpfull functions used in my project.

Model - contains LSTM an BiLSTM models architecture.

train_LSTM - LSTM model training. 

train_BiLSTM - BiLSTM model trainig.

generate_track – contains the processes of generating music tracks from array gotten from trained model. 
