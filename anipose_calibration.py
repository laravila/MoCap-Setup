"""
Aniposelib calibration script
"""
import numpy as np
from aniposelib.boards import CharucoBoard, Checkerboard
from aniposelib.cameras import Camera, CameraGroup
from aniposelib.utils import load_pose2d_fnames
import os

project_dir = "../../test_session"
calib_video_dir = "E:/ChAruCco_W5_H4_20240325"
calib_date = "20240325"
cam_names = ['Camera_Back_Right', 'Camera_Front_Left', 'Camera_Front_Right', 'Camera_Side_Left', 'Camera_Side_Right', 'Camera_Top_Left']
n_cameras = len(cam_names)

vidnames = []
for i in range(n_cameras):
    vidnames.append([f'{project_dir}/{cam_names[i]}/calibration_images/{cam_names[i]}_calibration.mp4'])



board = CharucoBoard(5, 4,
                     square_length=10, # here, in mm but any unit works
                     marker_length=6,
                     marker_bits=4, dict_size=250)


# the videos provided are fisheye, so we need the fisheye option
cgroup = CameraGroup.from_names(cam_names, fisheye=False)

# this will take about 15 minutes (mostly due to detection)
# it will detect the charuco board in the videos,
# then calibrate the cameras based on the detections, using iterative bundle adjustment
cgroup.calibrate_videos(vidnames, board)

# if you need to save and load
# example saving and loading for later
cgroup.dump(f'{project_dir}/calibration_{calib_date}.toml')