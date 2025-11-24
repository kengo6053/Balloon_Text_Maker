import bpy
from .properties import BalloonTextProperties

class BT_PT_Panel(bpy.types.Panel):
    bl_label = "Balloon Text Maker Lite"
    bl_idname = "BT_PT_balloon_text_lite"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "BalloonTextLite"

    def draw(self, context):
        layout = self.layout
        props = context.scene.balloon_text_lite_props

        layout.prop(props, "text_str")
        layout.prop(props, "font")
        layout.separator()

        box = layout.box()
        box.label(text="Mesh & Thickness")
        box.prop(props, "thickness")
        box.prop(props, "bevel_width")
        layout.separator()

        box = layout.box()
        box.label(text="Subdivision / Remesh (Smooth mode)")
        box.prop(props, "subdivide_cuts")
        box.prop(props, "use_remesh")            
        if props.use_remesh:
            box.prop(props, "remesh_octree_depth")
            box.prop(props, "remesh_scale")
            box.prop(props, "remesh_voxel_size")
            box.prop(props, "remesh_remove_disconnected")
            if props.remesh_remove_disconnected:
                box.prop(props, "remesh_disconnect_threshold")
            box.prop(props, "remesh_smooth_shading")
        layout.separator()

        layout.operator("bt_lite.create_text", text="① Create Text")
        layout.operator("bt_lite.meshify_thicken", text="② Meshify & Thicken")
        layout.operator("bt_lite.subdivide_mesh", text="③ Subdivide Mesh")
        layout.separator()
        layout.operator("bt_lite.all_steps", text="Run ①→③ All Steps", icon='PLAY')
