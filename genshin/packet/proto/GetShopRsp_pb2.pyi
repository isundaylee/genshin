from genshin.packet.proto import Shop_pb2 as _Shop_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetShopRsp(_message.Message):
    __slots__ = ("shop", "retcode")
    SHOP_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    shop: _Shop_pb2.Shop
    retcode: int
    def __init__(self, shop: _Optional[_Union[_Shop_pb2.Shop, _Mapping]] = ..., retcode: _Optional[int] = ...) -> None: ...
