# How to trim long videos with ffmpeg

This is a python script that uses ffmpeg to trim long videos into smaller clips. It is useful to me for trimming long videos into smaller clips for uploading to social media platforms like Instagram, Facebook, Twitter, etc.

## Requirements
- Python 3
- ffmpeg

## Usage

In `chopit.py` You just need to create a list with the name of the output file (without extension), start time and end time in seconds. For example:

```python
sections = [["Intro"  ,  "0:00:18"  ,  "10:34"  ],
                ["Meaty bit" ,  "12:34", "23:23" ],
           ]
```

Then run the script with the video file as an argument:

```bash
python chopit.py video.mp4
```

This will output a list of commands that you can run to trim the video into smaller clips.