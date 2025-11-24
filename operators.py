import bpy
from . import utils
from .properties import BalloonTextProperties

class BT_OT_CreateText(bpy.types.Operator):
    bl_idname = "bt_lite.create_text"
    bl_label = "① Create Text"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        props = context.scene.balloon_text_lite_props
        obj = utils.create_text_object(props)
        context.view_layer.objects.active = obj
        return {'FINISHED'}

class BT_OT_MeshifyAndThicken(bpy.types.Operator):
    bl_idname = "bt_lite.meshify_thicken"
    bl_label = "② Meshify & Thicken"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        props = context.scene.balloon_text_lite_props
        obj = context.active_object
        if obj is None or obj.type != 'FONT':
            self.report({'ERROR'}, "Active object must be a Text object")
            return {'CANCELLED'}
        obj = utils.convert_to_mesh(obj)
        utils.add_solidify_bevel(obj, props.thickness, props.bevel_width)
        return {'FINISHED'}

class BT_OT_SubdivideMesh(bpy.types.Operator):
    bl_idname = "bt_lite.subdivide_mesh"
    bl_label = "③ Subdivide Mesh"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        props = context.scene.balloon_text_lite_props
        obj = context.active_object
        if obj is None or obj.type != 'MESH':
            self.report({'ERROR'}, "Active object must be a Mesh object")
            return {'CANCELLED'}
        utils.subdivide_mesh(obj, props.subdivide_cuts)
        if props.use_remesh:
            utils.add_remesh(
                obj,
                props.remesh_voxel_size,
                props.remesh_octree_depth,
                props.remesh_scale,
                props.remesh_remove_disconnected,
                props.remesh_disconnect_threshold,
                props.remesh_smooth_shading
            )
        return {'FINISHED'}

class BT_OT_AllSteps(bpy.types.Operator):
    bl_idname = "bt_lite.all_steps"
    bl_label = "Run ①→③ All Steps"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        props = context.scene.balloon_text_lite_props
        obj = utils.create_text_object(props)
        obj = utils.convert_to_mesh(obj)
        utils.add_solidify_bevel(obj, props.thickness, props.bevel_width)
        utils.subdivide_mesh(obj, props.subdivide_cuts)
        if props.use_remesh:            
            utils.add_remesh(
                obj,
                props.remesh_voxel_size,
                props.remesh_octree_depth,
                props.remesh_scale,
                props.remesh_remove_disconnected,
                props.remesh_disconnect_threshold,
                props.remesh_smooth_shading
            )
        return {'FINISHED'}
