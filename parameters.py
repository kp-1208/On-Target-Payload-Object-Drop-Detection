########################################################################################################################
# Parameters specific to Cameras, Livestreams and Buffers
########################################################################################################################
# Frame Rate Factor to drop the frames not needed to process
FRAME_RATE_FACTOR = 3

# Set video frame height and width
FRAME_HEIGHT = 360  # 720 #576
FRAME_WIDTH = 640  # 1280 #1024

# set BATCH_SIZE for object-detection
BATCH_SIZE = 64  # for DGX 64, 8 for CPU

# buffer size for video streaming to minimize inconsistent network conditions
LIVE_STREAM_BUFFER_SIZE = 2048  # single camera

# buffer size for frames on which object detection will be performed
LIVE_STREAM_BUFFER_PURGE_SIZE = 256  # 256 for DGX

# IP Camera Details
IP_CAMS = {
    "kshitij-cam": ["http://192.168.19.194:4747/video", (300, 200, 20, 30)],
    # "shruti-cam": ["http://192.168.18.139:8080/video", (80, 360, 40, 0)],
    # "kshititj-cam-2": ["http://192.168.15.4:4747/video", (640, 360, 0, 0)],
    # "kshititj-cam-3": ["http://192.168.0.116:4747/video", (640, 360, 0, 0)],
    # "kshititj-cam-4": ["http://192.168.0.116:4747/video", (640, 360, 0, 0)],
    # "kshititj-cam-5": ["http://192.168.0.116:4747/video", (640, 360, 0, 0)],
    # "kshititj-cam-6": ["http://192.168.0.116:4747/video", (640, 360, 0, 0)],
    # "kshititj-cam-7": ["http://192.168.0.116:4747/video", (640, 360, 0, 0)],
    # "kshititj-cam-8": ["http://192.168.0.116:4747/video", (640, 360, 0, 0)],
    # "kshitij-webcam": ["http://192.168.18.222:5000", (640, 360, 0, 0)],
}

# Set wait duration for IP cam re initialization if we are not able to initialize the cam
IP_CAM_REINIT_WAIT_DURATION = 10  # seconds
