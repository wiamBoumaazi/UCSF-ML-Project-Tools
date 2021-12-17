# UCSF-ML-Project-Tools

Ruubing video_viewer.py:
This file will help you view your video frame by frame and enables the folowing operation:
- pause the video
- Move forward
- Move backward
- Quit
- Move slower in both directions

Tools needed to be installed:
- OpenCv
- NumPy
- Dlib

Please follow those instructions in order to use the video_viewer.py
p (pause)  c (continue)  q(quit) 
once you pause mode, you can b(back) and n(next).  
             
For you to exit pause, you have to press c(continue.)  
If you would like to adjust buffer size to navigate, adjust buffer_size var in the below
If you would like to adjust play speed, adjust labTime var in the below.
Where to locate video file : refer to cap var.

Running video_viewer_textfile_data_reader.py:
This file will enable you to read data from text file and display it on your video frames.
This data is generated from other headpose/ gaze algorithms and stored in textfile.
You can find the headpose and gaze algorithms here: https://github.com/wiamBoumaazi/UCSF-ML-project

There are three files that you need to download and use in order to display the data on the frame. 
- one file contains head pose data in a video for each frame. each line in the file contain this information: frame_index pitch roll yaw (in degree)
- second file contains Normalized gaze (in degree): frame_index Normalized_gaze
- Third file contains DeNormalized gaze (in degree): frame_index DeNormalized_gaze
an exaple of the data/ text file can be found here: 
https://drive.google.com/drive/folders/16VIMqPLhwlpjXg6ge0iq3lsX7DExaBiu 

While the videos used for this study can be found here: 
https://drive.google.com/drive/folders/1_BerUOLEnzt3vUBzGljTIsfrXjUd3Zk_

Please Note that each video has a meanigful name: name of the subject, portrait/landscape, distance from camera, with/without light
The video name matches the name of the head pose and gaze data generated from it. 

