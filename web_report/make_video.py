from pathlib import Path
import numpy as np
import json
from PIL import Image, ImageDraw, ImageFont
import cv2
from moviepy.editor import *

# File paths
root = Path()
info_path = root / "info"
data_proc = root / "data" / "data_proc"
out_path = root / "output"

out_tables = out_path / "exracted_tables"

data_file_name = out_tables / "collected_data_full.pkl"
stats_file_name = out_tables / "stats_full_subj_protocol.pkl"

save_fig_path = out_path / "figs"
exp_fig_path = save_fig_path / "experiments"
stats_fig_path = save_fig_path / "subject_stats"
global_fig_path = save_fig_path / "global_stats"
diff_fig_path = save_fig_path / "diff"
ir_diff_fig_path = save_fig_path / "ir_diff"
mse_fig_path = save_fig_path / "mse"


images = list(stats_fig_path.glob("*.jpg"))

fourcc = cv2.VideoWriter.fourcc(*'mp4v')
# videodims = (100,100)
# fourcc = cv2.VideoWriter_fourcc(*'avc1')    
# video = cv2.VideoWriter("test.mp4",fourcc, 60,videodims)
# img = Image.new('RGB', videodims, color = 'darkred')
# #draw stuff that goes on every frame here
# for i in range(0,60*60):
#     imtemp = img.copy()
#     # draw frame specific stuff here.
#     video.write(cv2.cvtColor(np.array(imtemp), cv2.COLOR_RGB2BGR))
# video.release()

img =  Image.open(images[0])
size = img.size

fnt = ImageFont.truetype('arial.ttf', 100)
# video = cv2.VideoWriter("test.mp4",fourcc, 60, size)
duration = 0.5
clips = []
for i in images:
    img =  Image.open(i)
    d = ImageDraw.Draw(img)
    d.text((size[0]//2 - 80, size[1]//30), i.stem, fill=(0,0,0), font= fnt )
    np_img = np.asarray(img)
    clips.append(ImageClip(np_img).set_duration(duration))
concat_clip = concatenate_videoclips(clips, method="compose")
concat_clip.write_videofile("test.mp4", fps=24)




    

