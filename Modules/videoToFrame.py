import cv2
import os

class videoToFrame:
    def __init__(self,video_path: str, file_path: str | None = None):
        self.video = video_path
        self.file = file_path

        newpath = r'Data/'

        if file_path:
            if not os.path.exists(file_path):
                os.makedirs(file_path)
        else:
            self.file = newpath
            if not os.path.exists(newpath):
                os.makedirs(newpath)

        #if not file_path:
            #self.file = newpath
            #if not os.path.exists(newpath):
                #os.makedirs(newpath)

        #if not os.path.exists(file_path):
            #os.makedirs(file_path)

    def frame(self):
        capture = cv2.VideoCapture(self.video)
        count = 0

        while (capture.isOpened()):
            ret, frame = capture.read()
            if (ret == True):
                cv2.imwrite(self.file + 'IMG_%04d.png' % count, frame)
                count += 1
            else:
                break

        print(count, 'images')

        capture.release()
        cv2.destroyAllWindows()
