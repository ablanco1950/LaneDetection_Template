# LaneDetection_Template
Lane detection using cv.matchTemplate function, a simpler system than the one usually used to process the image and detect contours. Furthermore, it does not require establishing a region of interest.

Requirements:

have installed: opencv (cv), numpy and time

Execute:

VIDEOLaneDetection_Template.py

The detected lane lines appear on the screen with a box over each video image, the greater the thickness of the box, the greater the probability of success.The x and y target appear on the console at all times and a final balance of successes and failures.
You also get a video demonstration.mp4 in which you can see the results more precisely.

The program is based on the example that appears in the OpenCV documentation with template, in the case of detecting several template objectives in the image. (https://docs.opencv.org/3.4/d4/dc6/tutorial_py_template_matching.html)

The problem is to determine the threshold level, which is attempted to be achieved in this work through an empirical formula and, if a detection is not achieved, the threshold level is adjusted downwards in several successive steps, which cannot be many due to cv.matchTemplate's tendency to detect false positives.

As test, a low-quality video is used in circumstances at night with different lighting, shadows and streetlights and nearby trees with their shadows, made by a pedestrian approaching and leaving the lane. The results can be compared with those obtained in the project:
https://github.com/ablanco1950/Directs_Object_Following_Lane , that uses the same video.

It can also be tested with the road video that is usually used in lane detection tests. In this case, two templates are used, one for the normal lane and the other for the worn lane. Since the template function allows you to detect if a lane has been detected or if it has not been detected, in this case you can try another template.

It is tested by running:

VIDEOLaneRoadDetection_Template.py


References:

https://docs.opencv.org/3.4/d4/dc6/tutorial_py_template_matching.html

https://github.com/ablanco1950/Directs_Object_Following_Lane

https://stackoverflow.com/questions/59923076/how-to-automatically-adjust-the-threshold-for-template-matching-with-opencv

https://stackoverflow.com/questions/59401389/how-to-isolate-everything-inside-of-a-contour-scale-it-and-test-the-similarity/59402625
