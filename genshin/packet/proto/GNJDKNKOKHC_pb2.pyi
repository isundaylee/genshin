from genshin.packet.proto import GMFOJOGGOBG_pb2 as _GMFOJOGGOBG_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GNJDKNKOKHC(_message.Message):
    __slots__ = ("ACIAPNAAHBG", "EJNINFFFKJP", "DNBEFLJLAMB")
    ACIAPNAAHBG_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    DNBEFLJLAMB_FIELD_NUMBER: _ClassVar[int]
    ACIAPNAAHBG: _containers.RepeatedCompositeFieldContainer[_GMFOJOGGOBG_pb2.GMFOJOGGOBG]
    EJNINFFFKJP: int
    DNBEFLJLAMB: int
    def __init__(self, ACIAPNAAHBG: _Optional[_Iterable[_Union[_GMFOJOGGOBG_pb2.GMFOJOGGOBG, _Mapping]]] = ..., EJNINFFFKJP: _Optional[int] = ..., DNBEFLJLAMB: _Optional[int] = ...) -> None: ...
