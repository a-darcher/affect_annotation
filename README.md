# affect_annotation
Work-in-progress tools for annotating emotional content in movies

Purpose: Provide method for labeling basic emotional elements of a movie, in real-time while watching the video.  

Components: 
- keylogger.pyw: simple keylogger snip that runs in the background. Records key presses and their timestamp (no mouse information)
- keylogger.ipynb: same keylogger, runs in jupyter 
- keylogger_read.ipynb: reads in the text file produced by keylogger.pyw and parses it into discrete "on-screen" events. 
- annotate_test.txt: sample keylogger text file

## Use case
Currently set-up for labeling using [Ekman's 6 basic emotions (common reference point in cognitive neuro/science)](https://www.paulekman.com/wp-content/uploads/2013/07/Basic-Emotions.pdf). 

Keys and corresponding label:
(Note: keyboard number keys, not numpad keys)

0. No emotion/neutral
1. Anger
2. Joy
3. Sadness
4. Fear
5. Disgust
6. Surprise 


Labels can be modified in keylogger_read.ipynb. 
Keylogger recognizes all keyboard input--- can record pausing of video via spacebar input. 
