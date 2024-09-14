from genshin.packet.proto import HomeMarkPointFurnitureData_pb2 as _HomeMarkPointFurnitureData_pb2
from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomeMarkPointSceneData(_message.Message):
    __slots__ = ("scene_id", "furniture_list", "teapot_spirit_pos", "safe_point_pos", "module_id")
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    FURNITURE_LIST_FIELD_NUMBER: _ClassVar[int]
    TEAPOT_SPIRIT_POS_FIELD_NUMBER: _ClassVar[int]
    SAFE_POINT_POS_FIELD_NUMBER: _ClassVar[int]
    MODULE_ID_FIELD_NUMBER: _ClassVar[int]
    scene_id: int
    furniture_list: _containers.RepeatedCompositeFieldContainer[_HomeMarkPointFurnitureData_pb2.HomeMarkPointFurnitureData]
    teapot_spirit_pos: _Vector_pb2.Vector
    safe_point_pos: _Vector_pb2.Vector
    module_id: int
    def __init__(self, scene_id: _Optional[int] = ..., furniture_list: _Optional[_Iterable[_Union[_HomeMarkPointFurnitureData_pb2.HomeMarkPointFurnitureData, _Mapping]]] = ..., teapot_spirit_pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., safe_point_pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., module_id: _Optional[int] = ...) -> None: ...
