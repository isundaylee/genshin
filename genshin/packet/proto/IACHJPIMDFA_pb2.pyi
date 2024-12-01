from genshin.packet.proto import Item_pb2 as _Item_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IACHJPIMDFA(_message.Message):
    __slots__ = ("ECDGLBPIMJK", "HMPDPHHDMLC")
    ECDGLBPIMJK_FIELD_NUMBER: _ClassVar[int]
    HMPDPHHDMLC_FIELD_NUMBER: _ClassVar[int]
    ECDGLBPIMJK: _Item_pb2.Item
    HMPDPHHDMLC: int
    def __init__(self, ECDGLBPIMJK: _Optional[_Union[_Item_pb2.Item, _Mapping]] = ..., HMPDPHHDMLC: _Optional[int] = ...) -> None: ...
