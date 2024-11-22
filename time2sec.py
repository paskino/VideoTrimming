# https://stackoverflow.com/questions/6402812/how-to-convert-an-hmmss-time-string-to-seconds-in-python
import sys
import os
import subprocess

ffmpeg = os.path.abspath("C:/Apps/ffmpeg-n5.0-latest-win64-gpl-5.0/bin/ffmpeg.exe")

# -ss 1:46:35 -i C:\Users\ofn77899\Downloads\28.06.mp4 -t 0:27:55 -c:v copy -c:a copy Jakob.mp")

def timestr2sec(ts):
    return sum( [int(x) * 60 ** i for i, x in enumerate(reversed(ts.split(':')))]) 

if __name__ == '__main__':

    

    input_file = os.path.abspath(sys.argv[1])
    output_file = os.path.abspath(sys.argv[2])

    if len(sys.argv) == 4:
        start = timestr2sec(sys.argv[3])
    elif len(sys.argv) == 5:
        start = timestr2sec(sys.argv[3])
        duration = timestr2sec(sys.argv[4]) -  timestr2sec(sys.argv[3])
    else:
        raise ValueError('You need to provide start and optionally stop times')

    command = [ ffmpeg, "-ss", str(start), "-i", input_file, "-t", str(duration), "-c:v copy -c:a copy", output_file]
    import functools
    print (functools.reduce(lambda x,y: x+ ' ' + y, command, '' ))
    


    