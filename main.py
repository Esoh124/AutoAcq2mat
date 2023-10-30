import os
import glob
import subprocess

path = "Z:/101_B2X_Pilot/B2X_main/20220209_LJH/Biopac"

basepath = "20220209_LJH"

os.makedirs(basepath, exist_ok=True)

acq_files = glob.glob(os.path.join(path, "*.acq"))


acq_file_names = []

for acq_file in acq_files:
    file_name = os.path.splitext(os.path.basename(acq_file))[0]
    acq_file_names.append(file_name)
    mat_name = " "+basepath+ "/"+file_name+ ".mat"
    command = "python acq2mat.py " + acq_file +" -o "+ mat_name
    print("command : "+command)
    subprocess.call(command)
