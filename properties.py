import bpy

class BalloonTextProperties(bpy.types.PropertyGroup):
    text_str: bpy.props.StringProperty(
        name="Text",
        description="文字列を入力",
        default="HELLO"
    )
    font: bpy.props.PointerProperty(
        name="Font",
        description="フォントを選択",
        type=bpy.types.VectorFont
    )
    thickness: bpy.props.FloatProperty(
        name="Thickness",
        description="厚み（SOLIDIFY厚み）",
        default=0.1,
        min=0.0,
        max=1.0
    )
    bevel_width: bpy.props.FloatProperty(
        name="Bevel Width",
        description="ベベル幅",
        default=0.02,
        min=0.0,
        max=0.2
    )
    subdivide_cuts: bpy.props.IntProperty(
        name="Subdivide Cuts",
        description="細分化回数",
        default=3,
        min=0,
        max=10
    )
    use_remesh: bpy.props.BoolProperty(
        name="Use Remesh",
        description="Remeshモディファイアを使う（スムーズモード専用）",
        default=False
    )
    remesh_octree_depth: bpy.props.IntProperty(
        name="Octree Depth",
        description="スムーズモード：Octree 深度（解像度）",
        default=8,
        min=1,
        max=12
    )
    remesh_scale: bpy.props.FloatProperty(
        name="Scale",
        description="スムーズモード：出力メッシュのスケール",
        default=0.9,
        min=0.1,
        max=1.0
    )
    remesh_voxel_size: bpy.props.FloatProperty(
        name="Remesh Voxel Size",
        description="スムーズモード：ボクセルサイズ／解像度",
        default=0.1,
        min=0.01,
        max=1.0
    )
    remesh_remove_disconnected: bpy.props.BoolProperty(
        name="Remove Disconnected Pieces",
        description="スムーズモード：分離した部分を削除するか",
        default=False
    )
    remesh_disconnect_threshold: bpy.props.FloatProperty(
        name="Threshold",
        description="分離部分削除：しきい値",
        default=1.0,
        min=0.0,
        max=10.0
    )
    remesh_smooth_shading: bpy.props.BoolProperty(
        name="Smooth Shading",
        description="スムーズモード適用後にスムーズシェーディングを有効にする",
        default=True
    )
    mass: bpy.props.FloatProperty(
        name="Mass",
        description="布質量（頂点単位）",  # ※将来拡張用
        default=0.3,
        min=0.0,
        max=10.0
    )
    bending_stiffness: bpy.props.FloatProperty(
        name="Bending Stiffness",
        description="布物理：曲げ剛性",  # ※将来拡張用
        default=5.0,
        min=0.0,
        max=50.0
    )
    pressure: bpy.props.FloatProperty(
        name="Pressure",
        description="圧力（風船膨張）",  # ※将来拡張用
        default=50.0,
        min=0.0,
        max=500.0
    )
