# Edge Detection Based Autofocus Algorithm to Detect Accurate Camera Working Distance
## Working Principle

This is the Python and Matlab implementation of our article named "Edge Detection Based Autofocus Algorithm to Detect Accurate Camera Working Distance" accepted by ISITES2022. Please feel free to use and give feedback.

![ezgif com-gif-maker (2)](https://user-images.githubusercontent.com/52501795/192199941-a4685fe7-1dde-453f-888c-bd3a8c817498.gif)

## Algorithm
As can be seen in Figure, a part of a circular geometry part image where we can see the edge information is framed in red. The frame marked here is shown zoomed in Figure (c)(d)(e). If the distance between the part and the camera is closer than the optimum focal distance, the blurred image seen in Figure (c) will be obtained. As you can see, the transition is smoother and longer. If the distance between the part and the camera is further than the optimum focal distance, a similar blurred image is obtained, as can be seen in Figure (e). However, as in Figure (d), the clearest image is obtained when the distance between the camera and the part is optimally
adjusted. The transition in the edge regions is narrower, the amount of change between the intensity values is higher. From this point of view, edge information contains critical clues about focusing. 

![image](https://user-images.githubusercontent.com/52501795/192207154-857ad214-06e2-42dc-9244-3be2b156b6c7.png)

First, images of the object are taken with an industrial camera at ε distance intervals. For each captured image, small objects in the image are eliminated and the gradient of the image is found. In order to find the median value of the image significant, all elements with zero value in the obtained image are assigned as undefined. Then all elements in the array that are smaller than the product of the found median value and ς are assigned zero. Finally, a new value is obtained by summing all the elements in the resulting array. The higher this value, the sharper the image.
![ezgif com-gif-maker (3)](https://user-images.githubusercontent.com/52501795/192206291-f01f44dc-dea3-4d06-b13c-bad642a454f7.gif)

## Requirements
###### Execution Environment
- Python 3 or Matlab
###### Packages
- Numpy 1.22.4
- Matplotlib 3.5.2
- OpenCV 4.6.0.66
- SciPy 1.8.1

## Usage
You can use the naming in line 16 of the code by adapting it for your own pictures. The x value in line 10 will be your ς value. Also this code is written in a for loop. If you want, you can apply it one by one by taking it out of the for loop according to the application area.

## Reference
Please cite this article: "Edge Detection Based Autofocus Algorithm to Detect Accurate Camera Working Distance" Poyraz A.G., Kacmaz M., ISITES'2022
