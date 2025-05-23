"""
Triangulation - SleapAnipose
"""
import numpy as np

import os
import sleap_anipose as slap

project_dir = "/Users/laravila/Desktop/Anipose/calibration_2905" #"../../test_M027_2024_03_20_11_30"
calibration_path = os.path.join(project_dir, "calibration.toml")

frames = (0, 4409) #(0, 6000)


## example triangulation without filtering, should take < 15 seconds

fname_dict = {
    'Camera_0': '/Users/laravila/Desktop/Anipose/calibration_2905/Camera_0/labels.Camera_0.proofread.analysis.h5',
    'Camera_1': '/Users/laravila/Desktop/Anipose/calibration_2905/Camera_1/labels.Camera_1.proofread.analysis.h5',
    'Camera_2': '/Users/laravila/Desktop/Anipose/calibration_2905/Camera_2/labels.Camera_2.proofread.analysis.h5',
    'Camera_5': '/Users/laravila/Desktop/Anipose/calibration_2905/Camera_5/labels.Camera_5.proofread.analysis.h5',
}
    #'Camera_Back_Right': f'{project_dir}/Camera_Back_Right/Camera_Back_Right.analysis.h5',
    #'Camera_Front_Left': f'{project_dir}/Camera_Front_Left/Camera_Front_Left.analysis.h5',
    #'Camera_Front_Right': f'{project_dir}/Camera_Front_Right/Camera_Front_Right.analysis.h5',
    #'Camera_Side_Left': f'{project_dir}/Camera_Side_Left/Camera_Side_Left.analysis.h5',
    #'Camera_Side_Right': f'{project_dir}/Camera_Side_Right/Camera_Side_Right.analysis.h5',
    #'Camera_Top_Left': f'{project_dir}/Camera_Top_Left/Camera_Top_Left.analysis.h5',


print('Loading 2D points...')
# number of keypoints in hand: 22
# T1,T2,T3,T4, I1,I2,I3,I4, M1,M2,M3,M4, R1,R2,R3,R4, P1,P2,P3,P4, L,R
# 0,1,2,3,     4,5,6,7,     8,9,10,11,   12,13,14,15, 16,17,18,19, 20,21
# number of edges in hand: 27
constraints = [[0,1],[1,2],[2,3],[3,20],
               [4,5],[5,6],[6,7],
               [8,9],[9,10],[10,11],
               [12,13],[13,14],[14,15],
               [16,17],[17,18],[18,19],
               [20,21],
               [7,11],[11,15],[15,19],[19,21],
               [7,21]
               ]
#[7,11],[11,15],[15,19],[19,21],
constraints_weak = []
#constraints = [[0,1],[0,3],[2,17],[5,18],[8,9],[11,12],[14,15],[15,16]]
#constraints_weak = [[0,6],[3,4],[1,16],[1,3]]

points3d = slap.triangulate(p2d = project_dir, 
                            calib = calibration_path, 
                            frames = frames, 
                            fname = f'{project_dir}/points3d.h5', 
                            disp_progress=True, 
                            constraints = constraints,
                            constraints_weak = constraints_weak,
                            scale_smooth = 5, 
                            scale_length = 4, 
                            scale_length_weak = 1, 
                            reproj_error_threshold = 5, 
                            reproj_loss = 'l2', 
                            n_deriv_smooth = 2)

print('Triangulation done!')