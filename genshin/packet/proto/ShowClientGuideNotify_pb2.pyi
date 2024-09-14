from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ShowClientGuideNotify(_message.Message):
    __slots__ = ("guide_name",)
    GUIDE_NAME_FIELD_NUMBER: _ClassVar[int]
    guide_name: str
    def __init__(self, guide_name: _Optional[str] = ...) -> None: ...
