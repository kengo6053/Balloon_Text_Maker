import bpy

def create_text_object(props):
    bpy.ops.object.text_add()
    obj = bpy.context.active_object
    obj.data.body = props.text_str
    if props.font:
        obj.data.font = props.font
    obj.name = "BalloonText"
    return obj

def convert_to_mesh(obj):
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.convert(target='MESH')
    return obj

def add_solidify_bevel(obj, thickness, bevel_width):
    solid = obj.modifiers.new(name="BalloonSolidify", type='SOLIDIFY')
    solid.thickness = thickness
    bevel = obj.modifiers.new(name="BalloonBevel", type='BEVEL')
    bevel.width = bevel_width
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.modifier_apply(modifier=solid.name)
    bpy.ops.object.modifier_apply(modifier=bevel.name)

def subdivide_mesh(obj, cuts):
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.subdivide(number_cuts=cuts)
    bpy.ops.object.mode_set(mode='OBJECT')

def add_remesh(obj,
               voxel_size,
               octree_depth,
               scale,
               remove_disconnected,
               disconnect_threshold,
               smooth_shading=True):

    # アクティブオブジェクトを設定
    bpy.context.view_layer.objects.active = obj
    if not obj.select_get():
        obj.select_set(True)

    # モディファイアを追加
    rem = obj.modifiers.new(name="BalloonRemesh", type='REMESH')

    # スムーズモードに設定
    rem.mode = 'SMOOTH'

    # パラメータ設定
    rem.octree_depth = octree_depth
    rem.scale = scale
    rem.voxel_size = voxel_size
    rem.use_remove_disconnected = remove_disconnected
    rem.remove_disconnected_threshold = disconnect_threshold

    # スムーズシェーディングを適用（オプション）
    if smooth_shading:
        bpy.ops.object.shade_smooth()

    # モディファイアを“適用せず”残しておくので、下行はコメントアウトまたは削除：
    # bpy.ops.object.modifier_apply(modifier=rem.name)

    return rem