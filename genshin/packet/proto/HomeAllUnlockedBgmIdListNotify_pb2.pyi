from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HomeAllUnlockedBgmIdListNotify(_message.Message):
    __slots__ = ("all_unlocked_bgm_id_list", "PFOKFHLOKEJ")
    ALL_UNLOCKED_BGM_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    PFOKFHLOKEJ_FIELD_NUMBER: _ClassVar[int]
    all_unlocked_bgm_id_list: _containers.RepeatedScalarFieldContainer[int]
    PFOKFHLOKEJ: bool
    def __init__(self, all_unlocked_bgm_id_list: _Optional[_Iterable[int]] = ..., PFOKFHLOKEJ: bool = ...) -> None: ...
