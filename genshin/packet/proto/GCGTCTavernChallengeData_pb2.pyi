from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GCGTCTavernChallengeData(_message.Message):
    __slots__ = ("character_id", "unlock_level_id_list")
    CHARACTER_ID_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_LEVEL_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    character_id: int
    unlock_level_id_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, character_id: _Optional[int] = ..., unlock_level_id_list: _Optional[_Iterable[int]] = ...) -> None: ...
