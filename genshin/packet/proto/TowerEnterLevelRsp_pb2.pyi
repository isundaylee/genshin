from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TowerEnterLevelRsp(_message.Message):
    __slots__ = ("tower_buff_id_list", "floor_id", "level_index", "retcode")
    TOWER_BUFF_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    FLOOR_ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_INDEX_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    tower_buff_id_list: _containers.RepeatedScalarFieldContainer[int]
    floor_id: int
    level_index: int
    retcode: int
    def __init__(self, tower_buff_id_list: _Optional[_Iterable[int]] = ..., floor_id: _Optional[int] = ..., level_index: _Optional[int] = ..., retcode: _Optional[int] = ...) -> None: ...
