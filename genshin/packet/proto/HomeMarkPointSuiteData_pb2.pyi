from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HomeMarkPointSuiteData(_message.Message):
    __slots__ = ("suite_id",)
    SUITE_ID_FIELD_NUMBER: _ClassVar[int]
    suite_id: int
    def __init__(self, suite_id: _Optional[int] = ...) -> None: ...
