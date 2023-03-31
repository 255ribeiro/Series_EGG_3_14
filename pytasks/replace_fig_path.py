import fileinput
from pathlib import Path
import shutil
tex_dir = Path('./latex_eng')
tex_file_path = tex_dir / 'plos_latex_template.tex'


with open(tex_file_path, 'r', encoding='utf-8') as f:
    repalce_count = 0
    for  line in f:
        if '../output/figs' in line:
            repalce_count += 1
            path = line.split('{')
            path = path[1].split('}')[0]
            path1 = Path.cwd() / path[3:]
            path2 = tex_dir / '/'.join(path.split(r'/')
            [1:])
            print(path2)
            path2.parent.mkdir( parents=True, exist_ok=True)
            
                                      
            shutil.copy2(path1,path2.parent)
            line = line.replace('../output', './output')
            #print(repalce_count, line)

if repalce_count == 0:
    for line in fileinput.input(tex_file_path, inplace=True):
        if '../output' in line:
            line = line.replace('../output', './output')
        print(line)


