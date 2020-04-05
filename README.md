# opencv_box_averaging
Trial scripts computing the mean / median of colors within parts of an image.

2 alterative algorithms are implemented:
- BGR: Mean / median computation of each component (B)lue, (G)reen, (R)ed
- HSV: Mean / median computation of (H)ue / color, (S)aturation, (V)alue / brightness

2 two versions exist:
- `image_color_averaging.py` computes mean / meadian of a statig image
- `camera_color_averaging.py` computes mean / meadian of a camera stream
