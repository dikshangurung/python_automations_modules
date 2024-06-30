#!/usr/bin/env python3

import os
import subprocess

my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/home/dikshan/Desktop/Python_automation/module3/app_dir/myapp/", my_env["PATH"]])
result = subprocess.run(["myapp"],env=my_env)
print(result.returncode)


