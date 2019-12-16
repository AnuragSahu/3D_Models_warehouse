import bpy
from random import randrange
import random


def append_zero(num):
    return "." + str(num).zfill(3)

# rack_loc = '/home/shell_basher/Project/3D_Models_warehouse/CustomMadeRacks/model1(Mixed)/model.dae'
#rack_loc = '/home/shell_basher/Project/3D_Models_warehouse/SmallPrimitives/Racks/modal.dae'
#imported_object = bpy.ops.wm.collada_import(filepath=rack_loc)
#name = "Rack"
#bpy.data.objects[name].location.x += 0.0

all_box_loc = './SmallPrimitives/BoxModels/'
rack_loc = './SmallPrimitives/Racks/modal.dae'

offset_x = -0.5
z_positions = [0.3 , 1.63, 2.98, 4.35]
y_positions = [-2.3,-1.2 ,0, 1.5]

box_count = {"BoxA":0, "BoxB":0, "BoxC":0, "BoxD":0, "BoxF":0, "BoxG":0, "BoxH":0, "BoxI":0}

distance_between_racks_x = 1
distance_between_racks_y = 2.7


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

def place_racks_and_objects(rack_location, subscript):
    imported_object = bpy.ops.wm.collada_import(filepath=rack_loc)
    
    model = "Rack"
    change = append_zero(subscript)
    if subscript > 0:
        name = model + change
    else:
        name = model
            
    bpy.data.objects[name].location.x += rack_location[0]
    bpy.data.objects[name].location.y += rack_location[1]
    bpy.data.objects[name].location.z += rack_location[2]
    boxes = ["BoxA","BoxB","BoxD","BoxF","BoxH"]

    for rows in z_positions:
        for cols in y_positions:
            model = random.choice(boxes)
            model_temp = model
#            model = model+(append_zero(box_count[model_temp]))
            
            change = append_zero(box_count[model_temp])
            if box_count[model_temp] > 0:
                model = model + change
            else:
                model = model
                
            box_count[model_temp] += 1
            final_model_location = all_box_loc + model_temp +"/model.dae";
            print(final_model_location)
            imported_object = bpy.ops.wm.collada_import(filepath=final_model_location)
            bpy.data.objects[model].location.x = offset_x + rack_location[0]
            bpy.data.objects[model].location.y = cols + rack_location[1]
            bpy.data.objects[model].location.z = rows + rack_location[2]

for x in x_coord:
    
    for y in y_coord:
        
        model = "Rack Model"
            
        if randrange(2) == 0:
            change = append_zero(subscript)
            if subscript > 0:
                name = model + change
            else:
                name = model

            place_racks_and_objects([x, y, z], subscript)
            
            subscript += 1
            
            change = append_zero(subscript)
            if subscript > 0:
                name = model + change
            else:
                name = model

            place_racks_and_objects([x + x_rack, y, z], subscript)

            subscript += 1
        