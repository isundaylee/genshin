from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ItemGivingRsp(_message.Message):
    __slots__ = ("giving_group_id", "giving_id", "retcode")
    GIVING_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    GIVING_ID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    giving_group_id: int
    giving_id: int
    retcode: int
    def __init__(self, giving_group_id: _Optional[int] = ..., giving_id: _Optional[int] = ..., retcode: _Optional[int] = ...) -> None: ...
