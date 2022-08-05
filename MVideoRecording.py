import cv2
import numpy as np
import pyautogui
import os
import threading



class MultiThreadVideoRecording:
    def __init__(self,File_Name,Fps=30,Screen_Size = pyautogui.size()):
        self.SCREEN_SIZE = Screen_Size
        # define the codec
        self.fourcc = cv2.VideoWriter_fourcc(*"XVID")
        # frames per second
        self.fps = Fps
        # create the video write object
        self.out = cv2.VideoWriter(File_Name, self.fourcc, self.fps, (self.SCREEN_SIZE))

    def capture_video(self):
        
        while True:
            # make a screenshot
            img = pyautogui.screenshot()
            # convert these pixels to a proper numpy array to work with OpenCV
            frame = np.array(img)
            # convert colors from BGR to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # write the frame
            self.out.write(frame)
            if not os.path.exists('capturing.phy'):
                break
        # make sure everything is closed when exited
        cv2.destroyAllWindows()
        self.out.release()
    
    def start(self):
        if not os.path.exists('capturing.phy'):
            with open('capturing.phy', mode='a'): pass
        t = threading.Thread(target= self.capture_video)
        t.start()     
        
        
    def stop(self):
        if os.path.exists('capturing.phy'):
            os.remove('capturing.phy')
        
    
