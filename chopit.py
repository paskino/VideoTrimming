from time2sec import timestr2sec, ffmpeg
import os, sys

def chopit(input_file, section, outdir="."):
    start = timestr2sec(section[1])
    duration = timestr2sec(section[2]) - start
    output_file = os.path.join(outdir, section[0] + ".mp4")
    command = [ ffmpeg, "-ss", str(start), "-i", input_file, "-t", str(duration), "-c:v copy -c:a copy", section[0] + ".mp4"]
    return command

    


if __name__ == '__main__':
    sections = [["Intro"  ,  "0:00:18"  ,  "10:34"  ],
                ["Meaty bit" ,  "12:34", "23:23" ],
                [ "Closing" , "3:29:34" ,  "3:35:49" ]
                ]

    for section in sections[2:]:
        command = chopit(sys.argv[1], section)
        import functools
        print (functools.reduce(lambda x,y: x.strip()+ ' ' + y, command, '' ))
        # import subprocess
        # print (command)
        # subprocess.run(command) 
    