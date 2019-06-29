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

bpy.context.object.location[0] = 0.87 # For Translation along X
bpy.context.object.location[1] = 0.87 # For Translation along Y
bpy.context.object.location[2] = 0.87 # For Translation along Z

```

- How to Scale the Models in X,Y and Z axis respectively

```sh

bpy.context.object.scale[0] = 0.025 # For scaling in X
bpy.context.object.scale[1] = 0.025 # For Scaling in Y
bpy.context.object.scale[2] = 0.025 # For Scaling in Z

```

- How to Rotate the Models in X, Y and Z axis Respectively

```sh

bpy.context.object.rotation_euler[0] = 0.2 # For Rotation along X
bpy.context.object.rotation_euler[1] = 0.2 # For Rotation along Y
bpy.context.object.rotation_euler[2] = 0.2 # For Rotation along Z

```
