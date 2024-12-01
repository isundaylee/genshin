from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PDALAMDHIOB(_message.Message):
    __slots__ = ("MFHKFMFACIN", "skill_depot_id")
    MFHKFMFACIN_FIELD_NUMBER: _ClassVar[int]
    SKILL_DEPOT_ID_FIELD_NUMBER: _ClassVar[int]
    MFHKFMFACIN: _containers.RepeatedScalarFieldContainer[int]
    skill_depot_id: int
    def __init__(self, MFHKFMFACIN: _Optional[_Iterable[int]] = ..., skill_depot_id: _Optional[int] = ...) -> None: ...
