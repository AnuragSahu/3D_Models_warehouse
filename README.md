# 3D_Models_warehouse
3D Models for the warehouse.

![Alt text](./_images/sample_output.gif?raw=true "Output Sample")

These are some of the small but Important code Snippets which you might be looking for

- How to Import a .dae model in Blender

```sh

import bpy
# Enter the File Location
file_loc = '/home/anuragsahu/Desktop/Honors-1/3D-Warehouse-Models/BoxModels/model1/model.dae'
imported_object = bpy.ops.wm.collada_import(filepath=file_loc)

```
- How to Translate the Models in X, Y and Z repectively
```sh
name = "SketchUp";
bpy.data.objects[name].location.x = 3.0 # For Translation along X
bpy.data.objects[name].location.y = 3.0 # For Translation along Y
bpy.data.objects[name].location.z = 3.0 # For Translation along Z

#bpy.context.object.location[0] = 0.87 # For Translation along X
#bpy.context.object.location[1] = 0.87 # For Translation along Y
#bpy.context.object.location[2] = 0.87 # For Translation along Z

```

- How to Scale the Models in X,Y and Z axis respectively

```sh
bpy.data.objects[name].scale.x = 3.0 # For scaling along X
bpy.data.objects[name].scale.y = 3.0 # For Scaling along Y
bpy.data.objects[name].scale.z = 3.0 # For Scaling along Z

#bpy.context.object.scale[0] = 0.025 # For scaling in X
#bpy.context.object.scale[1] = 0.025 # For Scaling in Y
#bpy.context.object.scale[2] = 0.025 # For Scaling in Z

```

- How to Rotate the Models in X, Y and Z axis Respectively

```sh

bpy.data.objects[name].location.x = 3.0 # For Rotation along X
bpy.data.objects[name].location.y = 3.0 # For Rotation along Y
bpy.data.objects[name].location.z = 3.0 # For Rotation along Z

#bpy.context.object.rotation_euler[0] = 0.2 # For Rotation along X
#bpy.context.object.rotation_euler[1] = 0.2 # For Rotation along Y
#bpy.context.object.rotation_euler[2] = 0.2 # For Rotation along Z

```
- Code to Make a Rack Customised
```sh
import bpy
import random


#all_box_loc = '/home/anuragsahu/Desktop/Honors-1/SmallPrimitives/BoxModels/'
all_box_loc = '../SmallPrimitives/BoxModels/'
rack_loc = '../SmallPrimitives/Racks/modal.dae'

offset_x = -0.5
z_positions = [0.3 , 1.63, 2.98, 4.35]
y_positions = [-2.3,-1.2 ,0, 1.5]

box_count = {"BoxA":0, "BoxB":0, "BoxC":0, "BoxD":0, "BoxF":0, "BoxG":0, "BoxH":0, "BoxI":0}

distance_between_racks_x = 1
distance_between_racks_y = 2.7
rack_count = 0
def to_third_number(dig):
    if(dig==0):
        return "";
    elif(dig<10 and dig > 0):
        ret = ".00"+str(dig)
        return ret
    elif(dig<100 and dig > 9):
        ret = ".0"+str(dig)
        return ret
    elif(dig<1000 and dig > 99):
        ret = "."+str(dig)
        return ret

def place_racks_and_objects(rack_location,rack_count):
    imported_object = bpy.ops.wm.collada_import(filepath=rack_loc)
    name = "Rack" + to_third_number(rack_count)
    print(name)
    bpy.data.objects[name].location.x += rack_location[0]
    bpy.data.objects[name].location.y += rack_location[1]
    bpy.data.objects[name].location.z += rack_location[2]
    boxes = ["BoxA","BoxB","BoxD","BoxF","BoxH"]

    for rows in z_positions:
        for cols in y_positions:
            model = random.choice(boxes)
            model_temp = model
            model = model+(to_third_number(box_count[model_temp]))
            box_count[model_temp] += 1
            final_model_location = all_box_loc + model_temp +"/model.dae";
            print(final_model_location)
            imported_object = bpy.ops.wm.collada_import(filepath=final_model_location)
            bpy.data.objects[model].location.x = offset_x + rack_location[0]
            bpy.data.objects[model].location.y = cols + rack_location[1]
            bpy.data.objects[model].location.z = rows + rack_location[2]

def place_rack_pair(location,rack_count,distance_between_racks_x):
    distance_between_racks_x += 1            
    rack_location = [-distance_between_racks_x+location[0],
                      distance_between_racks_y+location[1],
                      0+location[2]]
    place_racks_and_objects(rack_location,rack_count)
    rack_location = [ distance_between_racks_x+location[0],
                      distance_between_racks_y+location[1],
                      0+location[2]]
    place_racks_and_objects(rack_location,rack_count+1)
    return rack_count+2


rack_count = place_rack_pair([0,0,0],rack_count,0)
rack_count = place_rack_pair([0,2*2.7,0],rack_count,0)
rack_count = place_rack_pair([0,4*2.7,0],rack_count,0)
 ```

![Alt text](./Script/Floor%20Planner/top_view.png "Top View")

- Code to Generate Random Floor Plans

 ```sh
 import bpy
from random import randrange

def append_zero(num):
    return "." + str(num).zfill(3)

rack_loc = '/home/shell_basher/Project/3D_Models_warehouse/CustomMadeRacks/model1(Mixed)/model.dae'

num_rack_y = 8  #14
y_rack = 5.25
y_start = -(y_rack * (num_rack_y/2.0 - 1) + y_rack/2.0)
y_end = -y_start

corridor = 5
num_rack_layer_x = 14   # should be 6, 14, 22...
x_rack = 1.5
x_start = -(num_rack_layer_x/4.0 * x_rack + (num_rack_layer_x - 2) * corridor/8.0)
x_end = -x_start

z = 0

x_coord = []
y_coord = []

x = x_start
while x <= x_end:
    x_coord.append(x)
    x += (2 * x_rack + corridor)

y = y_start
while y <= y_end:
    y_coord.append(y)
    y += y_rack

subscript = 0
for x in x_coord:

    for y in y_coord:

        model = "Rack Model"

        if randrange(2) == 0:
            change = append_zero(subscript)
            if subscript > 0:
                name = model + change
            else:
                name = model

            model_loc = rack_loc
            imported_object = bpy.ops.wm.collada_import(filepath=model_loc)
            bpy.data.objects[name].location.x = x
            bpy.data.objects[name].location.y = y
            bpy.data.objects[name].location.z = z

            subscript += 1

            change = append_zero(subscript)
            if subscript > 0:
                name = model + change
            else:
                name = model

            model_loc = rack_loc
            imported_object = bpy.ops.wm.collada_import(filepath=model_loc)
            bpy.data.objects[name].location.x = x + x_rack
            bpy.data.objects[name].location.y = y
            bpy.data.objects[name].location.z = z

            subscript += 1
 ```

 - Code to make Video from Frames
 ```sh
 import cv2
import numpy as np
import os

from os.path import isfile, join

def convert_frames_to_video(pathIn,pathOut,fps):
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]

    #for sorting the file names properly
    files.sort(key = lambda x: int(x[5:-4]))

    for i in range(len(files)):
        filename=pathIn + files[i]
        #reading each files
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        print(filename)
        #inserting the frames into an image array
        frame_array.append(img)

    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

    for i in range(len(frame_array)):
        # writing to a image array
        out.write(frame_array[i])
    out.release()

def main():
    pathIn= './data/' //this is Usually found in /tmp/ folder so you may need to apply sudo before running the command
    pathOut = 'video.avi'
    fps = 25.0
    convert_frames_to_video(pathIn, pathOut, fps)

if __name__=="__main__":
    main()
 ```
