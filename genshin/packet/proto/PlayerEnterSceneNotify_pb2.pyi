from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from genshin.packet.proto import EnterType_pb2 as _EnterType_pb2
from genshin.packet.proto import MapLayerInfo_pb2 as _MapLayerInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerEnterSceneNotify(_message.Message):
    __slots__ = ("is_skip_ui", "prev_pos", "world_level", "target_uid", "scene_begin_time", "scene_tag_id_list", "enter_scene_token", "dungeon_id", "GPJHAEEMCBK", "pos", "scene_id", "type", "ALJNJKPMOPB", "EKIBACGBHCJ", "KDHNDLANKNI", "map_layer_info", "KMDLMKGJIHH", "is_first_login_enter_scene", "DDGBKGDECME", "scene_transaction", "create_player_uid", "OKCAGDNDEJN")
    IS_SKIP_UI_FIELD_NUMBER: _ClassVar[int]
    PREV_POS_FIELD_NUMBER: _ClassVar[int]
    WORLD_LEVEL_FIELD_NUMBER: _ClassVar[int]
    TARGET_UID_FIELD_NUMBER: _ClassVar[int]
    SCENE_BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    SCENE_TAG_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    ENTER_SCENE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_ID_FIELD_NUMBER: _ClassVar[int]
    GPJHAEEMCBK_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ALJNJKPMOPB_FIELD_NUMBER: _ClassVar[int]
    EKIBACGBHCJ_FIELD_NUMBER: _ClassVar[int]
    KDHNDLANKNI_FIELD_NUMBER: _ClassVar[int]
    MAP_LAYER_INFO_FIELD_NUMBER: _ClassVar[int]
    KMDLMKGJIHH_FIELD_NUMBER: _ClassVar[int]
    IS_FIRST_LOGIN_ENTER_SCENE_FIELD_NUMBER: _ClassVar[int]
    DDGBKGDECME_FIELD_NUMBER: _ClassVar[int]
    SCENE_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_PLAYER_UID_FIELD_NUMBER: _ClassVar[int]
    OKCAGDNDEJN_FIELD_NUMBER: _ClassVar[int]
    is_skip_ui: bool
    prev_pos: _Vector_pb2.Vector
    world_level: int
    target_uid: int
    scene_begin_time: int
    scene_tag_id_list: _containers.RepeatedScalarFieldContainer[int]
    enter_scene_token: int
    dungeon_id: int
    GPJHAEEMCBK: int
    pos: _Vector_pb2.Vector
    scene_id: int
    type: _EnterType_pb2.EnterType
    ALJNJKPMOPB: int
    EKIBACGBHCJ: int
    KDHNDLANKNI: int
    map_layer_info: _MapLayerInfo_pb2.MapLayerInfo
    KMDLMKGJIHH: _Vector_pb2.Vector
    is_first_login_enter_scene: bool
    DDGBKGDECME: int
    scene_transaction: str
    create_player_uid: int
    OKCAGDNDEJN: int
    def __init__(self, is_skip_ui: bool = ..., prev_pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., world_level: _Optional[int] = ..., target_uid: _Optional[int] = ..., scene_begin_time: _Optional[int] = ..., scene_tag_id_list: _Optional[_Iterable[int]] = ..., enter_scene_token: _Optional[int] = ..., dungeon_id: _Optional[int] = ..., GPJHAEEMCBK: _Optional[int] = ..., pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., scene_id: _Optional[int] = ..., type: _Optional[_Union[_EnterType_pb2.EnterType, str]] = ..., ALJNJKPMOPB: _Optional[int] = ..., EKIBACGBHCJ: _Optional[int] = ..., KDHNDLANKNI: _Optional[int] = ..., map_layer_info: _Optional[_Union[_MapLayerInfo_pb2.MapLayerInfo, _Mapping]] = ..., KMDLMKGJIHH: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., is_first_login_enter_scene: bool = ..., DDGBKGDECME: _Optional[int] = ..., scene_transaction: _Optional[str] = ..., create_player_uid: _Optional[int] = ..., OKCAGDNDEJN: _Optional[int] = ...) -> None: ...
