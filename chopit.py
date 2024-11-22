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
                ["Casper" ,  "12:34", "23:23" ],
                [ "Andrew" , "24:37" , "56:41" ],
                [ "JeffF" , "1:03:39" , "1:33:09" ],
                [ "Georg" , "1:59:04" , "2:15:13" ],
                [ "Imraj" , "2:15:26" , "2:27:15" ], 
                [ "Sam" ,   "2:27:34" , "2:36:15" ],
                [ "Award" , "2:38:22" ,  "2:50:44" ],
                [ "DavidMcG", "2:53:09", "3:35:49"],
                [ "Closing" , "3:29:34" ,  "3:35:49" ]
                ]

    for section in sections[2:]:
        command = chopit(sys.argv[1], section)
        import functools
        print (functools.reduce(lambda x,y: x.strip()+ ' ' + y, command, '' ))
        # import subprocess
        # print (command)
        # subprocess.run(command) 
    