import numpy as np
import cv2
import pickle
frames = []


# read video from path - save images as np matrices in frames
path = "c:/prog/python/data.mp4"
cap = cv2.VideoCapture(path)

ret = True
while ret:
    ret, img = cap.read() # read one frame from the 'capture' object; img is (H, W, C)
    if ret:
        frames.append(img)
        # show frames --
        #cv2.imshow("Sup", img)
        #cv2.waitKey(1)


print(len(frames))

pickle_out = open('name_of_data.Pickle', "wb")
pickle.dump(frames, pickle_out)
pickle_out.close()

# load data - comment out the rest when done creating data
pickle_in = open("name_of_data.Pickle", "rb")
frames = np.array(pickle.load(pickle_in)) #optional
print(frames.shape)
