from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HomeNewUnlockedBgmIdListNotify(_message.Message):
    __slots__ = ("new_unlocked_bgm_id_list",)
    NEW_UNLOCKED_BGM_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    new_unlocked_bgm_id_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, new_unlocked_bgm_id_list: _Optional[_Iterable[int]] = ...) -> None: ...
