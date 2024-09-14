from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RegionSimpleInfo(_message.Message):
    __slots__ = ("name", "title", "type", "dispatch_url")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DISPATCH_URL_FIELD_NUMBER: _ClassVar[int]
    name: str
    title: str
    type: str
    dispatch_url: str
    def __init__(self, name: _Optional[str] = ..., title: _Optional[str] = ..., type: _Optional[str] = ..., dispatch_url: _Optional[str] = ...) -> None: ...
