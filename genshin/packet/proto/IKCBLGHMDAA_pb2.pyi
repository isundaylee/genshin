from genshin.packet.proto import BPHPDCCAEGC_pb2 as _BPHPDCCAEGC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IKCBLGHMDAA(_message.Message):
    __slots__ = ("NMOOCJNBEOH", "GODOGIJJJIA")
    class NMOOCJNBEOHEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _BPHPDCCAEGC_pb2.BPHPDCCAEGC
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_BPHPDCCAEGC_pb2.BPHPDCCAEGC, _Mapping]] = ...) -> None: ...
    NMOOCJNBEOH_FIELD_NUMBER: _ClassVar[int]
    GODOGIJJJIA_FIELD_NUMBER: _ClassVar[int]
    NMOOCJNBEOH: _containers.MessageMap[int, _BPHPDCCAEGC_pb2.BPHPDCCAEGC]
    GODOGIJJJIA: int
    def __init__(self, NMOOCJNBEOH: _Optional[_Mapping[int, _BPHPDCCAEGC_pb2.BPHPDCCAEGC]] = ..., GODOGIJJJIA: _Optional[int] = ...) -> None: ...
