import numpy as np
import matplotlib.pyplot as plt
import cv2
import sys
from scipy.interpolate import make_interp_spline, BSpline

k = 700
height_list = []
mag_list = []
x = 10
for i in range(21):
    height_list.append(k)
    k +=10

k = 700
for i in range(21):
    img = cv2.imread(str(k) + ".bmp",0)

    #print("cropped/" + str(k) + ".bmp___________________")
    sobelx = cv2.Sobel(img,cv2.CV_64F,1,0)
    sobely = cv2.Sobel(img,cv2.CV_64F,0,1)
    

    Gmag = np.sqrt(sobelx*sobelx + sobely*sobely)
    Gmag = Gmag.flatten()
    #Gdir = np.arctan2(sobely, sobelx) * (180 / np.pi)

    #Gmag = np.where(Gmag == 0, np.nan, Gmag)
    Gmag = Gmag[Gmag!=0]

    ortanca_deger = np.median(Gmag)
    print(ortanca_deger)
    #print(str(k) + " - MEDIAN = ", ortanca_deger)

    ortanca_deger3 = ortanca_deger*x
    #Gmag = np.where(Gmag < (ortanca_deger3), np.nan, Gmag)
    Gmag = Gmag[Gmag>ortanca_deger3]
    
    print(str(k) + " - SUM    = ", np.sum(Gmag))
    mag_list.append(np.sum(Gmag))
    k +=10

height_list = np.array(height_list); mag_list = np.array(mag_list)

xnew = np.linspace(height_list.min(), height_list.max(), 30000) 
spl = make_interp_spline(height_list, mag_list, k=3)  # type: BSpline
power_smooth = spl(xnew)

plt.plot(xnew, power_smooth, label="P Values for Every ε Position")
#plt.plot(height_list, mag_list, label="P Values for Every ε Position")
plt.legend()
plt.xlabel("ε Values")
plt.ylabel("P Values")
plt.yscale('symlog')
plt.title("ς = {}".format(x))

plt.show()