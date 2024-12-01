from genshin.packet.proto import IGKLNNDNCMG_pb2 as _IGKLNNDNCMG_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EPHCDNBBADA(_message.Message):
    __slots__ = ("CJENICJPFGE", "CDNNOICEECD", "EJNINFFFKJP", "DJMDOPPACPH")
    class CJENICJPFGEEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _IGKLNNDNCMG_pb2.IGKLNNDNCMG
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_IGKLNNDNCMG_pb2.IGKLNNDNCMG, _Mapping]] = ...) -> None: ...
    CJENICJPFGE_FIELD_NUMBER: _ClassVar[int]
    CDNNOICEECD_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    DJMDOPPACPH_FIELD_NUMBER: _ClassVar[int]
    CJENICJPFGE: _containers.MessageMap[int, _IGKLNNDNCMG_pb2.IGKLNNDNCMG]
    CDNNOICEECD: _containers.RepeatedScalarFieldContainer[int]
    EJNINFFFKJP: int
    DJMDOPPACPH: int
    def __init__(self, CJENICJPFGE: _Optional[_Mapping[int, _IGKLNNDNCMG_pb2.IGKLNNDNCMG]] = ..., CDNNOICEECD: _Optional[_Iterable[int]] = ..., EJNINFFFKJP: _Optional[int] = ..., DJMDOPPACPH: _Optional[int] = ...) -> None: ...