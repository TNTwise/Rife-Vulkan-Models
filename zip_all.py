import os
import zipfile
for i in os.listdir():
    if '.tar.gz' not in i:
        os.system(f'tar -zcvf {i}.tar.gz {i}')
