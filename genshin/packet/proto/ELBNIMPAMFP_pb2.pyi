from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ELBNIMPAMFP(_message.Message):
    __slots__ = ("OEMMLAKCANN", "FADINCNPBMD")
    OEMMLAKCANN_FIELD_NUMBER: _ClassVar[int]
    FADINCNPBMD_FIELD_NUMBER: _ClassVar[int]
    OEMMLAKCANN: int
    FADINCNPBMD: bool
    def __init__(self, OEMMLAKCANN: _Optional[int] = ..., FADINCNPBMD: bool = ...) -> None: ...
