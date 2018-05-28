import cv2
import opencv
import numpy as np
import imutils as im
import glob
import random

def noisy(image):
      row,col,ch= image.shape
      mean = 1
      var = 50
      sigma = var**0.9
      gauss = np.random.normal(mean,sigma,(row,col,ch))
      gauss = gauss.reshape(row,col,ch)
      noisy = image + gauss
      return noisy

def alphify(img):
    b_channel, g_channel, r_channel = cv2.split(img)
    alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255# creating a dummy alpha channel image.
    return(cv2.merge((b_channel, g_channel, r_channel, alpha_channel)))

def rm_black(img):
    for i in img:
        for j in i:
            if j[0] == 0 and j[1] == 0 and j[2] == 0:
                j[3] = 0
    return img

def prepare_sword(img):
    img = cv2.resize(img,(0,0),None,0.3,0.3)
    img = alphify(img)
    angle = np.random.randint(0,360)
    rotated = im.rotate_bound(img, angle)
    img = rm_black(rotated)
    return img

def prepare_bgrd(img):
    #img = cv2.resize(img,(0,0),None,0.5,0.5)
    img = alphify(img)
    return img

def open_bgrd():
    images = []
    for img in glob.glob("scenery/*.*"):
        try:
            image = cv2.imread(img,-1)
            images.append(image)
        except:
            continue
    return images

miecze = opencv.miecze()
print("mieczedone")
bgrds = open_bgrd()
print(bgrds)
print("tladone")
labels = []
overlays = []
labelfile = open("labels.kupa", "w+")
for i in range(1500):
    miecz = prepare_sword(random.choice(miecze))
    bgrd = prepare_bgrd(random.choice(bgrds))
    y1 = np.random.randint(0,(bgrd.shape[0]-miecz.shape[0]))
    x1 = np.random.randint(0,(bgrd.shape[1]-miecz.shape[1]))
    y2 = y1 + miecz.shape[0]
    x2 = x1 + miecz.shape[1]

    alpha_s = miecz[:, :, 3] / 255.0
    #print(alpha_s.shape,miecz.shape,bgrd.shape)
    alpha_l = 1.0 - alpha_s

    #print(bgrd[y1:y2,x1:x2,0].shape,[x2-x1,y2-y1])
    for c in range(0, 3):
        bgrd[y1:y2, x1:x2, c] = (alpha_s * miecz[:, :, c] + alpha_l * bgrd[y1:y2, x1:x2, c])
    bgr = noisy(bgrd)
    cv2.imwrite("end"+ '\\' +str(i)+".jpg",bgr)
    labels.append([str(i),(x1,y1,x2,y2)])


#tlo[y_offset:y_offset+miecze[0].shape[0], x_offset:x_offset+miecze[0].shape[1]] = miecze[0]
for i in labels:
    labelfile.write("\n"+str(i))
labelfile.close()