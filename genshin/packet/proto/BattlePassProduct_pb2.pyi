from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BattlePassProduct(_message.Message):
    __slots__ = ("normal_product_id", "extra_product_id", "upgrade_product_id")
    NORMAL_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    normal_product_id: str
    extra_product_id: str
    upgrade_product_id: str
    def __init__(self, normal_product_id: _Optional[str] = ..., extra_product_id: _Optional[str] = ..., upgrade_product_id: _Optional[str] = ...) -> None: ...
