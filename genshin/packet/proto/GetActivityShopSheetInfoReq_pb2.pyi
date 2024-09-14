from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetActivityShopSheetInfoReq(_message.Message):
    __slots__ = ("shop_type",)
    SHOP_TYPE_FIELD_NUMBER: _ClassVar[int]
    shop_type: int
    def __init__(self, shop_type: _Optional[int] = ...) -> None: ...
