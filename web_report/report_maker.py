from pathlib import Path
import json
from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader("./web_report/templates")
env = Environment(loader=file_loader)

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

# Experimets graphics

main_title = "Experiments graphics"
description = """ """
file_name = "experiments_figs.html"

## video dict
video_dict = {}
video_dict['title'] = None
video_dict['description'] = """ """
video_dict['link'] = ""

## fig_list
fig_dict_list = []

images = exp_fig_path.glob("*.jpg")

for i in images:
    temp_dict = {}
    temp_dict["img_path"] = "../../" + i.__str__().replace("\\", "/")
    title_list = i.stem.split("_")
    temp_dict["title"] = "Subject code: {} - {}, {}".format(
        title_list[0], title_list[1], title_list[2]
    )

    fig_dict_list.append(temp_dict)


rendered = env.get_template("experiments.html").render(
    img_dict=fig_dict_list, main_title=main_title, description=description, video_dict=video_dict
)


with open(f"./web_report/web_site/{file_name}", "w") as f:
    f.write(rendered)


# Tasks mean graphics

main_title = "Mean by task per subject"
description = """ """
file_name = "subject_mean.html"


## video dict
video_dict = {}
video_dict['title'] = "Video resume of the graphics:\nSubject - 4 tasks mean video"
video_dict['description'] = """ """
video_dict['link'] = "../../output/videos/subjects_dmcx2.mp4"


fig_dict_list = []

images = stats_fig_path.glob("*.jpg")

for i in images:
    temp_dict = {}
    temp_dict["img_path"] = "../../" + i.__str__().replace("\\", "/")
    temp_dict["title"] = "Subject code: {}".format(i.stem)

    fig_dict_list.append(temp_dict)


rendered = env.get_template("experiments.html").render(
    img_dict=fig_dict_list, main_title=main_title, description=description, video_dict=video_dict
)


with open(f"./web_report/web_site/{file_name}", "w") as f:
    f.write(rendered)


# Global statistics

main_title = "Global statistics"
description = """ """
file_name = "global_stats.html"

## video dict
video_dict = {}
video_dict['title'] = None
video_dict['description'] = """ """
video_dict['link'] = ""


fig_dict_list = []

images = global_fig_path.glob("*.jpg")

for i in images:
    if i.stem != "std":
        temp_dict = {}
        temp_dict["img_path"] = "../../" + i.__str__().replace("\\", "/")
        temp_dict["title"] = "{}".format(i.stem.title())
        if temp_dict["title"] == "Std Pop":
            temp_dict["title"] = "Standard deviation"

        fig_dict_list.append(temp_dict)


rendered = env.get_template("experiments.html").render(
    img_dict=fig_dict_list, main_title=main_title, description=description, video_dict=video_dict
)


with open(f"./web_report/web_site/{file_name}", "w") as f:
    f.write(rendered)


# Difference

main_title = "Difference from the mean"
description = """ """
file_name = "diff_mean.html"

## video dict
video_dict = {}
video_dict['title'] = "Video resume of the graphics:\nDiference (subject - global mean)"
video_dict['description'] = """ """
video_dict['link'] = "../../output/videos/diff_global_mean.mp4"



fig_dict_list = []

images = diff_fig_path.glob("*.jpg")

for i in images:
    temp_dict = {}
    temp_dict["img_path"] = "../../" + i.__str__().replace("\\", "/")
    temp_dict["title"] = "Subject code: {}".format(i.stem)

    fig_dict_list.append(temp_dict)


rendered = env.get_template("experiments.html").render(
    img_dict=fig_dict_list, main_title=main_title, description=description, video_dict=video_dict
)


with open(f"./web_report/web_site/{file_name}", "w") as f:
    f.write(rendered)

#  Imaginary - real
main_title = "Video resume of the graphics:\nDifference (imaginary - real)"
description = """ """
file_name = "diff_ir.html"

## video dict
video_dict = {}
video_dict['title'] = "Diference (Imaginary - Real)"
video_dict['description'] = """ """
video_dict['link'] = "../../output/videos/diff_imag_real.mp4"

fig_dict_list = []

images = ir_diff_fig_path.glob("*.jpg")

for i in images:
    temp_dict = {}
    temp_dict["img_path"] = "../../" + i.__str__().replace("\\", "/")
    temp_dict["title"] = "Subject code: {}".format(i.stem)

    fig_dict_list.append(temp_dict)


rendered = env.get_template("experiments.html").render(
    img_dict=fig_dict_list, main_title=main_title, description=description, video_dict=video_dict
)

with open(f"./web_report/web_site/{file_name}", "w") as f:
    f.write(rendered)

# MSE

main_title = "Mean square error"
description = """ """
fig_dict_list = []
file_name = "mse.html"

#video dict
video_dict = {}
video_dict['title'] = None
video_dict['description'] = """ """
video_dict['link'] = None

cha_dict_file = info_path / "channels_code_proc.json"
with open(cha_dict_file) as f:
    cha_dict_aux = json.load(f)
cha_dict = {}
for i in cha_dict_aux:
    cha_dict[i["Simple_code"]] = {"Prefix": i["Prefix"], "Underscore": i["Underscore"]}

images = mse_fig_path.glob("*.jpg")

for i in images:
    temp_dict = {}
    temp_dict["img_path"] = "../../" + i.__str__().replace("\\", "/")
    temp_dict["title"] = "Mse: Channel {}<sub>{}</sub>".format(
        cha_dict[i.stem.split("_")[1]]["Prefix"],
        cha_dict[i.stem.split("_")[1]]["Underscore"],
    )

    fig_dict_list.append(temp_dict)


rendered = env.get_template("experiments.html").render(
    img_dict=fig_dict_list, main_title=main_title, description=description, video_dict=video_dict
)

with open(f"./web_report/web_site/{file_name}", "w") as f:
    f.write(rendered)

#################

######## tables

#################

# import pandas as pd

# # full data

# main_title = 'Full tables'
# description = """ """
# file_name = 'table_full.html'

# df = pd.read_excel("./output/exracted_tables/collected_data_full.xlsx")

# rendered = env.get_template("tables.html").render( results=df , main_title = main_title, description = description)

# with open(f'./web_report/web_site/{file_name}', 'w') as f:
#     f.write(rendered)
