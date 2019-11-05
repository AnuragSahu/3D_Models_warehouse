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
