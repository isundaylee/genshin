from genshin.packet.proto import Uint32Pair_pb2 as _Uint32Pair_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonEntryInfoReq(_message.Message):
    __slots__ = ("scene_point_id_list", "scene_id", "point_id")
    SCENE_POINT_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    POINT_ID_FIELD_NUMBER: _ClassVar[int]
    scene_point_id_list: _containers.RepeatedCompositeFieldContainer[_Uint32Pair_pb2.Uint32Pair]
    scene_id: int
    point_id: int
    def __init__(self, scene_point_id_list: _Optional[_Iterable[_Union[_Uint32Pair_pb2.Uint32Pair, _Mapping]]] = ..., scene_id: _Optional[int] = ..., point_id: _Optional[int] = ...) -> None: ...
