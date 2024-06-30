#!/usr/bin/env python3
import shutil
import psutil

def check_disk_space(disk):
	du = shutil.disk_usage(disk)
	free = du.free / du.total * 100
	return free > 10

def check_cpu_usage():
	usage = psutil.cpu_percent(1)
	return usage < 75

if not check_disk_space("/") or not check_cpu_usage():
	print("Error")
else:
	print("ok")

