from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomeFurnitureSuiteData(_message.Message):
    __slots__ = ("is_allow_summon", "guid", "suite_id", "spawn_pos", "included_furniture_index_list")
    IS_ALLOW_SUMMON_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    SUITE_ID_FIELD_NUMBER: _ClassVar[int]
    SPAWN_POS_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_FURNITURE_INDEX_LIST_FIELD_NUMBER: _ClassVar[int]
    is_allow_summon: bool
    guid: int
    suite_id: int
    spawn_pos: _Vector_pb2.Vector
    included_furniture_index_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, is_allow_summon: bool = ..., guid: _Optional[int] = ..., suite_id: _Optional[int] = ..., spawn_pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., included_furniture_index_list: _Optional[_Iterable[int]] = ...) -> None: ...
