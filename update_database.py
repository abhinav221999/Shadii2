import subprocess
import time

while True:
    time.sleep(60*60*24)
    subprocess.call(["g++", "prog.cpp"])



