bl_info = {
    "name": "Balloon Text Maker Lite",
    "author": "Your Name",
    "version": (1, 0, 0),
    "blender": (4, 0, 0),
    "location": "View3D > Sidebar > BalloonTextLite",
    "description": "Creates balloon-style text mesh: text → mesh/thickness → subdivide",
    "warning": "",
    "wiki_url": "",
    "category": "Object",
}

import bpy

from . import properties
from . import utils
from . import operators
from . import ui

classes = (
    properties.BalloonTextProperties,
    operators.BT_OT_CreateText,
    operators.BT_OT_MeshifyAndThicken,
    operators.BT_OT_SubdivideMesh,
    operators.BT_OT_AllSteps,
    ui.BT_PT_Panel,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.balloon_text_lite_props = bpy.props.PointerProperty(type=properties.BalloonTextProperties)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.balloon_text_lite_props

if __name__ == "__main__":
    register()
