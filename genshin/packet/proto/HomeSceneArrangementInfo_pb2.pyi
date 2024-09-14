from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from genshin.packet.proto import HomeFurnitureData_pb2 as _HomeFurnitureData_pb2
from genshin.packet.proto import HomeBlockArrangementInfo_pb2 as _HomeBlockArrangementInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomeSceneArrangementInfo(_message.Message):
    __slots__ = ("born_rot", "BMAEDEOKOHL", "comfort_value", "djinn_pos", "born_pos", "door_list", "tmp_version", "scene_id", "main_house", "is_set_born_pos", "block_arrangement_info_list", "stair_list", "DFCFKJBCCAH", "bgm_id", "EJAPJLENOGL")
    BORN_ROT_FIELD_NUMBER: _ClassVar[int]
    BMAEDEOKOHL_FIELD_NUMBER: _ClassVar[int]
    COMFORT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DJINN_POS_FIELD_NUMBER: _ClassVar[int]
    BORN_POS_FIELD_NUMBER: _ClassVar[int]
    DOOR_LIST_FIELD_NUMBER: _ClassVar[int]
    TMP_VERSION_FIELD_NUMBER: _ClassVar[int]
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    MAIN_HOUSE_FIELD_NUMBER: _ClassVar[int]
    IS_SET_BORN_POS_FIELD_NUMBER: _ClassVar[int]
    BLOCK_ARRANGEMENT_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    STAIR_LIST_FIELD_NUMBER: _ClassVar[int]
    DFCFKJBCCAH_FIELD_NUMBER: _ClassVar[int]
    BGM_ID_FIELD_NUMBER: _ClassVar[int]
    EJAPJLENOGL_FIELD_NUMBER: _ClassVar[int]
    born_rot: _Vector_pb2.Vector
    BMAEDEOKOHL: bool
    comfort_value: int
    djinn_pos: _Vector_pb2.Vector
    born_pos: _Vector_pb2.Vector
    door_list: _containers.RepeatedCompositeFieldContainer[_HomeFurnitureData_pb2.HomeFurnitureData]
    tmp_version: int
    scene_id: int
    main_house: _HomeFurnitureData_pb2.HomeFurnitureData
    is_set_born_pos: bool
    block_arrangement_info_list: _containers.RepeatedCompositeFieldContainer[_HomeBlockArrangementInfo_pb2.HomeBlockArrangementInfo]
    stair_list: _containers.RepeatedCompositeFieldContainer[_HomeFurnitureData_pb2.HomeFurnitureData]
    DFCFKJBCCAH: _Vector_pb2.Vector
    bgm_id: int
    EJAPJLENOGL: _Vector_pb2.Vector
    def __init__(self, born_rot: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., BMAEDEOKOHL: bool = ..., comfort_value: _Optional[int] = ..., djinn_pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., born_pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., door_list: _Optional[_Iterable[_Union[_HomeFurnitureData_pb2.HomeFurnitureData, _Mapping]]] = ..., tmp_version: _Optional[int] = ..., scene_id: _Optional[int] = ..., main_house: _Optional[_Union[_HomeFurnitureData_pb2.HomeFurnitureData, _Mapping]] = ..., is_set_born_pos: bool = ..., block_arrangement_info_list: _Optional[_Iterable[_Union[_HomeBlockArrangementInfo_pb2.HomeBlockArrangementInfo, _Mapping]]] = ..., stair_list: _Optional[_Iterable[_Union[_HomeFurnitureData_pb2.HomeFurnitureData, _Mapping]]] = ..., DFCFKJBCCAH: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., bgm_id: _Optional[int] = ..., EJAPJLENOGL: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ...) -> None: ...
