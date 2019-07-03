# 3D_Models_warehouse
3D Models for the warehouse.

I made an Model by Placing the Objects manually in the Scene, 
the link to that model. <a href="https://drive.google.com/file/d/1RGn6QzW1_GJdYuNm6cQF0sSnF0QWWsHi/view?usp=sharing"> Link </a>

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
- Sample Code

```sh

import bpy

file_loc = '/home/anuragsahu/Desktop/Honors-1/3D-Warehouse-Models/BoxModels/model7/model.dae'
imported_object = bpy.ops.wm.collada_import(filepath=file_loc)
name = "SketchUp";
print(name)
bpy.data.objects[name].location.x += 3.0
#    bpy.data.objects["SketchUp"].location.y += 3.0
#    bpy.data.objects["SketchUp"].location.z += 3.0

file_loc = '/home/anuragsahu/Desktop/Honors-1/3D-Warehouse-Models/BoxModels/model7/model.dae'
imported_object = bpy.ops.wm.collada_import(filepath=file_loc)
name = "SketchUp.001";
print(name)
bpy.data.objects[name].location.x += 6.0
bpy.data.objects[name].scale.x = 0.05
bpy.data.objects[name].rotation_euler.x = 0.2
bpy.data.objects[name].rotation_euler.z = 0.2
bpy.data.objects[name].rotation_euler.y = 0.2

```
- Code to Make a Rack Customised
```sh
import bpy
import random

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

#file_loc = '/home/anuragsahu/Desktop/Honors-1/BoxModels/BoxA/model.dae'
all_box_loc = '/home/anuragsahu/Desktop/Honors-1/SmallPrimitives/BoxModels/'
rack_loc = '/home/anuragsahu/Desktop/Honors-1/SmallPrimitives/Racks/modal.dae'
imported_object = bpy.ops.wm.collada_import(filepath=rack_loc)
name = "Rack"
bpy.data.objects[name].location.x += 0.0

offset_x = -0.3
z_positions = [0.3 , 1.63, 2.93, 4.2]
y_positions = [-2.3,1 ,0, 1.5]


boxes = ["BoxA","BoxB","BoxC","BoxD","BoxF","BoxH","BoxI"]
box_count = {"BoxA":0, "BoxB":0, "BoxC":0, "BoxD":0, "BoxF":0, "BoxG":0, "BoxH":0, "BoxI":0}
#box_placements = {"BoxA":{"x":[]}


for rows in z_positions:
    for cols in y_positions:
        model = random.choice(boxes)
        model_temp = model
        model = model+(to_third_number(box_count[model_temp]))
        box_count[model_temp] += 1
        final_model_location = all_box_loc + model_temp +"/model.dae";
        print(final_model_location)
        imported_object = bpy.ops.wm.collada_import(filepath=final_model_location)
        bpy.data.objects[model].location.x = offset_x
        bpy.data.objects[model].location.y = cols
        bpy.data.objects[model].location.z = rows
        if(model_temp=="BoxH"):
                    bpy.data.objects[model].location.z += 0.1
            
 ```
