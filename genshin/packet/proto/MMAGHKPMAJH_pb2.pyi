from genshin.packet.proto import DOJJHJACOHA_pb2 as _DOJJHJACOHA_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MMAGHKPMAJH(_message.Message):
    __slots__ = ("LECPNADEJOO", "OEOCPOEKCMJ", "EJNINFFFKJP")
    LECPNADEJOO_FIELD_NUMBER: _ClassVar[int]
    OEOCPOEKCMJ_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    LECPNADEJOO: _containers.RepeatedCompositeFieldContainer[_DOJJHJACOHA_pb2.DOJJHJACOHA]
    OEOCPOEKCMJ: int
    EJNINFFFKJP: int
    def __init__(self, LECPNADEJOO: _Optional[_Iterable[_Union[_DOJJHJACOHA_pb2.DOJJHJACOHA, _Mapping]]] = ..., OEOCPOEKCMJ: _Optional[int] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
