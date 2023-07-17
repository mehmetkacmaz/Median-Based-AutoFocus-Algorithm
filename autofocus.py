import sys

import cv2
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import BSpline, make_interp_spline

class AutoFocus:
    def __init__(self) -> None:
        self.k = 700
        self.height_list = []
        self.height_listmag_list = []
        self.x = 10

    def autofocus(self):
        """
        Generate the function comment for the given function body in a markdown code block with the correct language syntax.
        This code defines a function called autofocus that performs some image processing operations. It takes no arguments and returns
        two arrays, xnew and power_smooth.

        The function iterates over a range of values, appends values to a list, and performs image processing operations on each iteration.
        It uses the OpenCV library to apply Sobel operators to calculate the gradient magnitude of the image. It then calculates the median
        of the gradient magnitudes and filters out values below a certain threshold. The function also calculates the sum of the filtered
        gradient magnitudes and appends it to another list.

        Finally, the function converts the lists to numpy arrays, creates a new array xnew using the minimum and maximum values from
        height_list, and applies a spline interpolation to smooth the height_listmag_list values. The smoothed values are stored in power_smooth
        and both xnew and power_smooth are returned from the function.
        Returns:
            xnew (numpy.ndarray): An array of x-axis values.
            power_smooth (numpy.ndarray): An array of smoothed y-axis values.
        """
        for i in range(21):
            self.height_list.append(k)
            k +=10

        self.k = 700
        for i in range(21):
            img = cv2.imread(str(self.k) + ".bmp",0)

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

            ortanca_deger3 = ortanca_deger*self.x
            #Gmag = np.where(Gmag < (ortanca_deger3), np.nan, Gmag)
            Gmag = Gmag[Gmag>ortanca_deger3]
            
            print(str(self.k) + " - SUM    = ", np.sum(Gmag))
            self.height_listmag_list.append(np.sum(Gmag))
            self.k +=10

        self.height_list = np.array(self.height_list); self.height_listmag_list = np.array(self.height_listmag_list)

        xnew = np.linspace(self.height_list.min(), self.height_list.max(), 30000) 
        spl = make_interp_spline(self.height_list, self.height_listmag_list, k=3)  # type: BSpline
        power_smooth = spl(xnew)

        return xnew, power_smooth

    def plot(self, xnew, power_smooth):
        """
        Plots the given data using matplotlib.
        This code defines a method called plot that uses matplotlib to plot data. It takes in two parameters, xnew and power_smooth,
        which are arrays of x-values and y-values respectively. The method plots the data using plt.plot, adds a legend, sets labels
        for the x-axis and y-axis, scales the y-axis using a symlog scale, and sets a title for the plot. Finally, it displays the plot
        using plt.show.
        Parameters:
            xnew (array-like): The x-values of the data.
            power_smooth (array-like): The y-values of the data.
        Returns:
            None
        """
        plt.plot(xnew, power_smooth, label="P Values for Every ε Position")
        #plt.plot(self.height_list, self.height_listmag_list, label="P Values for Every ε Position")
        plt.legend()
        plt.xlabel("ε Values")
        plt.ylabel("P Values")
        plt.yscale('symlog')
        plt.title("ς = {}".format(self.x))
        plt.show()
