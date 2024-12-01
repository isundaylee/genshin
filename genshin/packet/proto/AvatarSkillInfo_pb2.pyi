from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarSkillInfo(_message.Message):
    __slots__ = ("GDFJMGGFDCH", "BHFDBBKEMAK", "CMHGDLDAHDM")
    GDFJMGGFDCH_FIELD_NUMBER: _ClassVar[int]
    BHFDBBKEMAK_FIELD_NUMBER: _ClassVar[int]
    CMHGDLDAHDM_FIELD_NUMBER: _ClassVar[int]
    GDFJMGGFDCH: _containers.RepeatedScalarFieldContainer[int]
    BHFDBBKEMAK: int
    CMHGDLDAHDM: int
    def __init__(self, GDFJMGGFDCH: _Optional[_Iterable[int]] = ..., BHFDBBKEMAK: _Optional[int] = ..., CMHGDLDAHDM: _Optional[int] = ...) -> None: ...
