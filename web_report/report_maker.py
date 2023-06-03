from pathlib import Path
import os

from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('./web_report/templates')
env = Environment(loader=file_loader)

#File paths
root = Path()
info_path = root / 'info'
data_proc = root / 'data' / 'data_proc'
out_path =root / 'output'

out_tables = out_path / 'exracted_tables'

data_file_name = out_tables / 'collected_data_full.pkl'
stats_file_name = out_tables / 'stats_full_subj_protocol.pkl'

save_fig_path = out_path / 'figs'
exp_fig_path = save_fig_path / 'experiments'
stats_fig_path = save_fig_path / 'subject_stats'
global_fig_path = save_fig_path / 'global_stats'
diff_fig_path = save_fig_path / 'diff'
ir_diff_fig_path = save_fig_path / 'ir_diff'
mse_fig_path = save_fig_path / 'mse'


# Experimets graphics

fig_dict_list = []

images = exp_fig_path.glob('*.jpg')

for i in images:
    temp_dict ={}
    temp_dict["img_path"] = "../../" + i.__str__().replace('\\', '/')
    title_list = i.stem.split('_')
    temp_dict["title"] = "Subject: {} - {}, {}".format(title_list[0], title_list[1], title_list[2])

    fig_dict_list.append(temp_dict)


rendered = env.get_template("experiments.html").render( img_dict=fig_dict_list)

file_name = 'experiments_figs.html'

with open(f'./web_report/web_site/{file_name}', 'w') as f:
    f.write(rendered)


