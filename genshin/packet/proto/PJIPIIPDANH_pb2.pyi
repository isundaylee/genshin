from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PJIPIIPDANH(_message.Message):
    __slots__ = ("AGIDBEEINDE", "IECEJKOPPPM")
    AGIDBEEINDE_FIELD_NUMBER: _ClassVar[int]
    IECEJKOPPPM_FIELD_NUMBER: _ClassVar[int]
    AGIDBEEINDE: int
    IECEJKOPPPM: int
    def __init__(self, AGIDBEEINDE: _Optional[int] = ..., IECEJKOPPPM: _Optional[int] = ...) -> None: ...
