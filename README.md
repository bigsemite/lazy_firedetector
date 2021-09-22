# lazy_firedetector
Fire detector  solution developed in python using the OpenCV.
## The Concept
Leveraging on the concept of image processing, 

The application takes the video stream as input *getVid() function*

The video is being read into the app on per frame basis.


**findsmoke() function**

Utilize the HSV feature in image processing to get the intensity of the image in each frame

The app use the first 30 seconds to study the environment and stores the highest intensity discovered during the period

After the 30 seconds time, any frame that has intensity that is higher than the highest stored value will be considered as intensity created by the presence of fire.

## Limitations 
The application can perform best in a closed environment where there's no much variation in the brightness/darkness 

The application will consider the excessive brightness of electric bulb as a fire.
