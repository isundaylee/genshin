from genshin.packet.proto import KJGAENHLKHP_pb2 as _KJGAENHLKHP_pb2
from genshin.packet.proto import IGKLNNDNCMG_pb2 as _IGKLNNDNCMG_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BFDGNFHPHIO(_message.Message):
    __slots__ = ("BAIKJMKBJPB", "AGKPEKAANCA", "CJENICJPFGE", "EJNINFFFKJP")
    class CJENICJPFGEEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _IGKLNNDNCMG_pb2.IGKLNNDNCMG
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_IGKLNNDNCMG_pb2.IGKLNNDNCMG, _Mapping]] = ...) -> None: ...
    BAIKJMKBJPB_FIELD_NUMBER: _ClassVar[int]
    AGKPEKAANCA_FIELD_NUMBER: _ClassVar[int]
    CJENICJPFGE_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    BAIKJMKBJPB: _containers.RepeatedCompositeFieldContainer[_KJGAENHLKHP_pb2.KJGAENHLKHP]
    AGKPEKAANCA: _containers.RepeatedScalarFieldContainer[int]
    CJENICJPFGE: _containers.MessageMap[int, _IGKLNNDNCMG_pb2.IGKLNNDNCMG]
    EJNINFFFKJP: int
    def __init__(self, BAIKJMKBJPB: _Optional[_Iterable[_Union[_KJGAENHLKHP_pb2.KJGAENHLKHP, _Mapping]]] = ..., AGKPEKAANCA: _Optional[_Iterable[int]] = ..., CJENICJPFGE: _Optional[_Mapping[int, _IGKLNNDNCMG_pb2.IGKLNNDNCMG]] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
