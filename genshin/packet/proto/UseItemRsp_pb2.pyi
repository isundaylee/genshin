from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UseItemRsp(_message.Message):
    __slots__ = ("target_guid", "retcode", "option_idx", "guid", "item_id")
    TARGET_GUID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    OPTION_IDX_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    target_guid: int
    retcode: int
    option_idx: int
    guid: int
    item_id: int
    def __init__(self, target_guid: _Optional[int] = ..., retcode: _Optional[int] = ..., option_idx: _Optional[int] = ..., guid: _Optional[int] = ..., item_id: _Optional[int] = ...) -> None: ...
