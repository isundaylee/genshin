from genshin.packet.proto import Item_pb2 as _Item_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TrifleGadget(_message.Message):
    __slots__ = ("item", "EJNBFCIJOMO")
    ITEM_FIELD_NUMBER: _ClassVar[int]
    EJNBFCIJOMO_FIELD_NUMBER: _ClassVar[int]
    item: _Item_pb2.Item
    EJNBFCIJOMO: int
    def __init__(self, item: _Optional[_Union[_Item_pb2.Item, _Mapping]] = ..., EJNBFCIJOMO: _Optional[int] = ...) -> None: ...
