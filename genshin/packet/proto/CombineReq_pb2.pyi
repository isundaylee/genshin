from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CombineReq(_message.Message):
    __slots__ = ("combine_count", "avatar_guid", "combine_id")
    COMBINE_COUNT_FIELD_NUMBER: _ClassVar[int]
    AVATAR_GUID_FIELD_NUMBER: _ClassVar[int]
    COMBINE_ID_FIELD_NUMBER: _ClassVar[int]
    combine_count: int
    avatar_guid: int
    combine_id: int
    def __init__(self, combine_count: _Optional[int] = ..., avatar_guid: _Optional[int] = ..., combine_id: _Optional[int] = ...) -> None: ...
