from pathlib import Path
import numpy as np
import json
from PIL import Image, ImageDraw, ImageFont
import cv2
from moviepy.editor import *

# File paths
root = Path()
out_path = root / "output"
save_fig_path = out_path / "figs"
exp_fig_path = save_fig_path / "experiments"
stats_fig_path = save_fig_path / "subject_stats"
global_fig_path = save_fig_path / "global_stats"
diff_fig_path = save_fig_path / "diff"
ir_diff_fig_path = save_fig_path / "ir_diff"
mse_fig_path = save_fig_path / "mse"

# Make video path
video_path = out_path / "videos"
video_path.mkdir(exist_ok=True)

# Subjects stats
print('--> Subject stats video')
images = list(stats_fig_path.glob("*.jpg"))

img =  Image.open(images[0])
size = img.size
img.close()

fnt = ImageFont.truetype('arial.ttf', 100)

duration = 0.5
clips = []
for i in images:
    img =  Image.open(i)
    d = ImageDraw.Draw(img)
    d.text((size[0]//2 -80 , size[1]//30), i.stem, fill=(0,0,0), font= fnt, align = "center" )
    np_img = np.asarray(img)
    img.close()
    clips.append(ImageClip(np_img).set_duration(duration))
concat_clip = concatenate_videoclips(clips, method="compose")
concat_clip.write_videofile( str(video_path) + "/" + "subjects_dmcx2.mp4", fps=24)
del concat_clip

### Diferences
print('-->  Diferences video:')
images = list(diff_fig_path.glob("*.jpg"))

img =  Image.open(images[0])
size = img.size
img.close()
fnt = ImageFont.truetype('arial.ttf', 100)

duration = 0.5
clips = []
for i in images:
    img =  Image.open(i)
    d = ImageDraw.Draw(img)
    d.text((size[0]//2 -80 , size[1]//30), i.stem, fill=(0,0,0), font= fnt, align = "center" )
    np_img = np.asarray(img)
    img.close()
    clips.append(ImageClip(np_img).set_duration(duration))
concat_clip = concatenate_videoclips(clips, method="compose")
concat_clip.write_videofile( str(video_path) + "/" + "diff_global_mean.mp4", fps=24)
del concat_clip


# Difference imaginary - real
print('--> Diferences (imaginary - real) video:')
images = list(ir_diff_fig_path.glob("*.jpg"))

img =  Image.open(images[0])
size = img.size
img.close()

fnt = ImageFont.truetype('arial.ttf', 100)

duration = 0.5
clips = []
for i in images:
    img =  Image.open(i)
    d = ImageDraw.Draw(img)
    d.text((size[0]//2 -80 , size[1]//30), i.stem, fill=(0,0,0), font= fnt, align = "center" )
    np_img = np.asarray(img)
    img.close()
    clips.append(ImageClip(np_img).set_duration(duration))
concat_clip = concatenate_videoclips(clips, method="compose")
concat_clip.write_videofile( str(video_path) + "/" + "diff_imag_real.mp4", fps=24)
del concat_clip
