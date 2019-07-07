import bpy

def append_zero(num):
    return "." + str(num).zfill(3)

all_box_loc = '/home/shell_basher/Project/3D_Models_warehouse/BoxModels/'
rack_loc = '/home/shell_basher/Project/3D_Models_warehouse/SmallPrimitives/Racks/modal.dae'
imported_object = bpy.ops.wm.collada_import(filepath=rack_loc)
name = "Rack"
bpy.data.objects[name].location.x += 0.0

x = -0.75
y_coord = [-2.5, -1.2, 0.1, 1.4]

z_coord = [0.25,1.62,3]

i = 0
for z in z_coord:
    for y in y_coord:
        model = "model1"
        change = append_zero(i)
        
        if i > 0:
            name = "SketchUp"+ change
        else:
            name = "SketchUp"
        
        model_loc = all_box_loc + model + "/model.dae"
        imported_object = bpy.ops.wm.collada_import(filepath=model_loc)
        bpy.data.objects[name].location.x = x
        bpy.data.objects[name].location.y = y
        bpy.data.objects[name].location.z = z
        
        i += 1
