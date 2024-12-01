from genshin.packet.proto import LAMEAODOJID_pb2 as _LAMEAODOJID_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JDAPCOMIMKO(_message.Message):
    __slots__ = ("BBOPFHAODOP", "BODIEJCLGMB", "CKECBIMKAPE", "FIIGJJAAAKH")
    BBOPFHAODOP_FIELD_NUMBER: _ClassVar[int]
    BODIEJCLGMB_FIELD_NUMBER: _ClassVar[int]
    CKECBIMKAPE_FIELD_NUMBER: _ClassVar[int]
    FIIGJJAAAKH_FIELD_NUMBER: _ClassVar[int]
    BBOPFHAODOP: _containers.RepeatedCompositeFieldContainer[_LAMEAODOJID_pb2.LAMEAODOJID]
    BODIEJCLGMB: int
    CKECBIMKAPE: int
    FIIGJJAAAKH: int
    def __init__(self, BBOPFHAODOP: _Optional[_Iterable[_Union[_LAMEAODOJID_pb2.LAMEAODOJID, _Mapping]]] = ..., BODIEJCLGMB: _Optional[int] = ..., CKECBIMKAPE: _Optional[int] = ..., FIIGJJAAAKH: _Optional[int] = ...) -> None: ...
