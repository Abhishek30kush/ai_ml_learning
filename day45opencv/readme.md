Goal
Learn to:

Access pixel values and modify them
Access image properties
Set a Region of Interest (ROI)
Split and merge images
Almost all the operations in this section are mainly related to Numpy rather than OpenCV. A good knowledge of Numpy is required to write better optimized code with OpenCV.

( Examples will be shown in a Python terminal, since most of them are just single lines of code )

Accessing Image Properties
Image properties include number of rows, columns, and channels; type of image data; number of pixels; etc.

The shape of an image is accessed by img.shape. It returns a tuple of the number of rows, columns, and channels (if the image is color):

