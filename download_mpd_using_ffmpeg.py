
import os

# Path to the folder containing .mpd files
folder_path = r"C:\Users\{User}\Desktop\phys104_last\Mid_1\Mid_1_Exam\Boys\04_1444_1st"

# List all .mpd files in the folder
mpd_files = [f for f in os.listdir(folder_path) if f.endswith(".mpd")]

# Convert each .mpd file to .mp4
for mpd_file in mpd_files:
    mp4_file = os.path.splitext(mpd_file)[0] + ".mp4"
    mpd_file_path = os.path.join(folder_path, mpd_file)
    mp4_file_path = os.path.join(folder_path, mp4_file)
    os.system(f"ffmpeg -i {mpd_file_path} -codec copy {mp4_file_path}")
