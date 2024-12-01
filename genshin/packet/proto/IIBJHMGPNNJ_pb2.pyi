from genshin.packet.proto import FCHDBLFDCPD_pb2 as _FCHDBLFDCPD_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IIBJHMGPNNJ(_message.Message):
    __slots__ = ("CFGHCCCFLCJ",)
    CFGHCCCFLCJ_FIELD_NUMBER: _ClassVar[int]
    CFGHCCCFLCJ: _containers.RepeatedCompositeFieldContainer[_FCHDBLFDCPD_pb2.FCHDBLFDCPD]
    def __init__(self, CFGHCCCFLCJ: _Optional[_Iterable[_Union[_FCHDBLFDCPD_pb2.FCHDBLFDCPD, _Mapping]]] = ...) -> None: ...
