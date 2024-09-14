from genshin.packet.proto import ItemParam_pb2 as _ItemParam_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeCompoundOutputRsp(_message.Message):
    __slots__ = ("retcode", "item_list")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    item_list: _containers.RepeatedCompositeFieldContainer[_ItemParam_pb2.ItemParam]
    def __init__(self, retcode: _Optional[int] = ..., item_list: _Optional[_Iterable[_Union[_ItemParam_pb2.ItemParam, _Mapping]]] = ...) -> None: ...
