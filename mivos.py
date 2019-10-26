#!bin/python

import tempfile
import json

temp_dir = tempfile.TemporaryDirectory()
print(temp_dir.name)



with open('init.json') as json_data:
    data_dict = json.load(json_data)
    repos = data_dict["repositories"]
    deps = data_dict["dependencies"]
    print(repos)

print(repos)
# use temp_dir, and when done:
# shutil.rmtree(temp_dir.name)