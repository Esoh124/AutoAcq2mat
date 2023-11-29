import os
import glob
import subprocess



subjects = ['20211113_KDH', '20211123_HHB', '20211229_PSR','20211230_CJK','20220104_CKM', '20220118_KDH', '20220119_PSR', '20220120_HHB', '20220121_CKM', '20220124_CSJ', '20220125_KMS', '20220126_CJK', '20220126_CSJ', '20220127_KMS', '20220203_LJH', '20220203_PBJ', '20220204_PBJ', '20220207_SYH', '20220208_SYH', '20220209_LJH']

for i in subjects:
    path = "Z:/101_B2X_Pilot/B2X_main/"+i+"/Biopac"

    os.makedirs(i, exist_ok=True)

    acq_files = glob.glob(os.path.join(path, "*.acq"))

    acq_file_names = []

    for acq_file in acq_files:
        file_name = os.path.splitext(os.path.basename(acq_file))[0]
        acq_file_names.append(file_name)
        mat_name = " "+i+ "/"+file_name+ ".mat"
        command = "python acq2mat.py " + acq_file +" -o "+ mat_name
        print("command : "+command)
        subprocess.call(command)
