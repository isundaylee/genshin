from genshin.packet.proto import EPJOPBFFLFL_pb2 as _EPJOPBFFLFL_pb2
from genshin.packet.proto import BECBKBINEBD_pb2 as _BECBKBINEBD_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KGEHAJDBBPG(_message.Message):
    __slots__ = ("DNKJOJHBJLD", "ADONAEDIEBG", "EJNINFFFKJP")
    DNKJOJHBJLD_FIELD_NUMBER: _ClassVar[int]
    ADONAEDIEBG_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    DNKJOJHBJLD: _EPJOPBFFLFL_pb2.EPJOPBFFLFL
    ADONAEDIEBG: _containers.RepeatedCompositeFieldContainer[_BECBKBINEBD_pb2.BECBKBINEBD]
    EJNINFFFKJP: int
    def __init__(self, DNKJOJHBJLD: _Optional[_Union[_EPJOPBFFLFL_pb2.EPJOPBFFLFL, _Mapping]] = ..., ADONAEDIEBG: _Optional[_Iterable[_Union[_BECBKBINEBD_pb2.BECBKBINEBD, _Mapping]]] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
