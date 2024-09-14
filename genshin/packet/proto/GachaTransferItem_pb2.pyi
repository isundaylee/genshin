from genshin.packet.proto import ItemParam_pb2 as _ItemParam_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GachaTransferItem(_message.Message):
    __slots__ = ("item", "is_transfer_item_new")
    ITEM_FIELD_NUMBER: _ClassVar[int]
    IS_TRANSFER_ITEM_NEW_FIELD_NUMBER: _ClassVar[int]
    item: _ItemParam_pb2.ItemParam
    is_transfer_item_new: bool
    def __init__(self, item: _Optional[_Union[_ItemParam_pb2.ItemParam, _Mapping]] = ..., is_transfer_item_new: bool = ...) -> None: ...
