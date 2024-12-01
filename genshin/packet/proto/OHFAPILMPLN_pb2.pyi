from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class OHFAPILMPLN(_message.Message):
    __slots__ = ("GOHAGOHHGLK", "MEJLFKPFPGK", "skill_depot_id", "AGIDBEEINDE")
    GOHAGOHHGLK_FIELD_NUMBER: _ClassVar[int]
    MEJLFKPFPGK_FIELD_NUMBER: _ClassVar[int]
    SKILL_DEPOT_ID_FIELD_NUMBER: _ClassVar[int]
    AGIDBEEINDE_FIELD_NUMBER: _ClassVar[int]
    GOHAGOHHGLK: _containers.RepeatedScalarFieldContainer[int]
    MEJLFKPFPGK: int
    skill_depot_id: int
    AGIDBEEINDE: int
    def __init__(self, GOHAGOHHGLK: _Optional[_Iterable[int]] = ..., MEJLFKPFPGK: _Optional[int] = ..., skill_depot_id: _Optional[int] = ..., AGIDBEEINDE: _Optional[int] = ...) -> None: ...
