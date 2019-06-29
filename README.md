# 3D_Models_warehouse
3D Models for the warehouse.

I made an Model by Placing the Objects manually in the Scene, 
the link to that model. <a href="https://drive.google.com/file/d/1RGn6QzW1_GJdYuNm6cQF0sSnF0QWWsHi/view?usp=sharing"> Link </a>

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
