from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HomeTransferReq(_message.Message):
    __slots__ = ("is_transfer_to_main_house_point", "is_transfer_to_safe_point", "guid")
    IS_TRANSFER_TO_MAIN_HOUSE_POINT_FIELD_NUMBER: _ClassVar[int]
    IS_TRANSFER_TO_SAFE_POINT_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    is_transfer_to_main_house_point: bool
    is_transfer_to_safe_point: bool
    guid: int
    def __init__(self, is_transfer_to_main_house_point: bool = ..., is_transfer_to_safe_point: bool = ..., guid: _Optional[int] = ...) -> None: ...
