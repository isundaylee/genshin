from genshin.packet.proto import IGKLNNDNCMG_pb2 as _IGKLNNDNCMG_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PAGLEJFJJDK(_message.Message):
    __slots__ = ("CJENICJPFGE",)
    class CJENICJPFGEEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _IGKLNNDNCMG_pb2.IGKLNNDNCMG
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_IGKLNNDNCMG_pb2.IGKLNNDNCMG, _Mapping]] = ...) -> None: ...
    CJENICJPFGE_FIELD_NUMBER: _ClassVar[int]
    CJENICJPFGE: _containers.MessageMap[int, _IGKLNNDNCMG_pb2.IGKLNNDNCMG]
    def __init__(self, CJENICJPFGE: _Optional[_Mapping[int, _IGKLNNDNCMG_pb2.IGKLNNDNCMG]] = ...) -> None: ...
