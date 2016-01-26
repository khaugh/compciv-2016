import os
import requests
import shutil

filename = 'tempdata/matty.shakespeare.tar.gz'
dirname = 'tempdata'
shutil.unpack_archive(filename, extract_dir=dirname)
print('Unpacked', filename, 'into', dirname)
