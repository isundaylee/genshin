from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BreakoutSyncConnectUidInfo(_message.Message):
    __slots__ = ("uid", "skill_id_list", "skill_level_list")
    UID_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    SKILL_LEVEL_LIST_FIELD_NUMBER: _ClassVar[int]
    uid: int
    skill_id_list: _containers.RepeatedScalarFieldContainer[int]
    skill_level_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, uid: _Optional[int] = ..., skill_id_list: _Optional[_Iterable[int]] = ..., skill_level_list: _Optional[_Iterable[int]] = ...) -> None: ...
