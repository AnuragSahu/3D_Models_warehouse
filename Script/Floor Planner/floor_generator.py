import bpy
from random import randrange

def append_zero(num):
    return "." + str(num).zfill(3)

rack_loc = '/home/shell_basher/Project/3D_Models_warehouse/CustomMadeRacks/model1(Mixed)/model.dae'
#rack_loc = '/home/shell_basher/Project/3D_Models_warehouse/SmallPrimitives/Racks/modal.dae'
#imported_object = bpy.ops.wm.collada_import(filepath=rack_loc)
#name = "Rack"
#bpy.data.objects[name].location.x += 0.0

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

print(x_coord)
print(y_coord)

subscript = 0
#x_coord = x_start

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
        