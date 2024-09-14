from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BargainOfferPriceReq(_message.Message):
    __slots__ = ("bargain_id", "price")
    BARGAIN_ID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    bargain_id: int
    price: int
    def __init__(self, bargain_id: _Optional[int] = ..., price: _Optional[int] = ...) -> None: ...
