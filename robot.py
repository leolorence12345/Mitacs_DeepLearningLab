import bpy

# Select the armature object
armature_obj = bpy.data.objects['arm_link_1']
armature_obj.select_set(True)
bpy.context.view_layer.objects.active = armature_obj

# Switch to Pose Mode
bpy.ops.object.mode_set(mode='POSE')

# Access and modify the pose of a specific bone
bone_name = 'arm_link_1'
bone = armature_obj.pose.bones.get(bone_name)
if bone:
    # Modify the pose properties as needed
    bone.location = (1.0, 0.0, 0.0)  # Example translation
    bone.rotation_euler = (0.0, 0.0, 1.57)  # Example rotation in radians

# Switch back to Object Mode
bpy.ops.object.mode_set(mode='OBJECT')
