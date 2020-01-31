# Meeting Minutes
## Meeting Information
**Meeting Date/Time:** 30 Jan 19, 18:00
**Meeting Purpose:** Weekly Thursday Meeting 
**Meeting Location:** Prof. Madhav's Office
**Note Taker:** Anurag Sahu

## Attendees
People who attended:
-  Prof. Madhav Krishna
- Anurag Sahu
- Puru Gupta
- Meher Shashwat Nigam

## Agenda Items

Item | Description
---- | ----
Solving problems on Warehouse Enviroment | • Able to get the agent in the Gazebo Enviroment One rack only<br>• Move the agent in the Environment with Capturing RGBD images<br>• Make the Octomap from the moving Depth map.<br>
Warehouse Generation | • Able to get the fully filled warehouse with complete random boxes in the shelfs and randomly genetated floor plan. <br>• Added Lights to the warehouse by Script.<br>

## Discussion Items
Item | Who | Notes |
---- | ---- | ---- |
Solving problems on Warehouse Enviroment | Prof. Madhav | Now that we are able to get the Octomap and Depth Map we can try to estimate the Free space, One way to do that can be to find the line with same vanishing points and then estimating the distane between the lines to get the height of the racks and since we have the rack's occupancy map we can estimate the free space in the rack |
Solving problems on Warehouse Enviroment|Anurag|Also since we are releasing the Dataset it will be in best interest of the community if we are able to solve some very popular problems in our dataset, like Navigation and since we also started with warehouse generation to do the same thing like we can solve the problems in Navigation, Object Detection, Loop Detection. |
Warehouse Generation| Shashwat| We can now try to make the Windows and roof Translucent so that if we place a sun the light can seep in. Also we can now add the Some random objects like Cylinder and some random carts here and there.|
Warehouse Generation| Prof. Madhav| Yes, is it possible to check if we can get the pixels wise schemantic Segmentation of the objects in the blender itself. Can we annotate objects in the images and also get the Bounding boxes of the objects so that we can set ground truth values for others.|



## Action Items
| Done? | Item | Responsible |
| ---- | ---- | ---- |
| | Get the problems which our dataset can solve and compare it with the State of the art. | Anurag Sahu |
| | Look if we can get the Pixel wise schemantic Segementation, Bounding Boxes for the Objects, Annotations for the objects|Shashwat and Puru| 

## Other Notes & Information
-

