import os
import zipfile
for i in os.listdir():
    os.system(f'tar -zcvf {i}.tar.gz {i}')