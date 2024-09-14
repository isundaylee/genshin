from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TryEnterHomeReq(_message.Message):
    __slots__ = ("target_uid", "is_transfer_to_main_house_point", "is_transfer_to_safe_point", "target_point")
    TARGET_UID_FIELD_NUMBER: _ClassVar[int]
    IS_TRANSFER_TO_MAIN_HOUSE_POINT_FIELD_NUMBER: _ClassVar[int]
    IS_TRANSFER_TO_SAFE_POINT_FIELD_NUMBER: _ClassVar[int]
    TARGET_POINT_FIELD_NUMBER: _ClassVar[int]
    target_uid: int
    is_transfer_to_main_house_point: bool
    is_transfer_to_safe_point: bool
    target_point: int
    def __init__(self, target_uid: _Optional[int] = ..., is_transfer_to_main_house_point: bool = ..., is_transfer_to_safe_point: bool = ..., target_point: _Optional[int] = ...) -> None: ...
