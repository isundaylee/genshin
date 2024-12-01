from genshin.packet.proto import FDKIIFFFCGJ_pb2 as _FDKIIFFFCGJ_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FGJAFPKFBOA(_message.Message):
    __slots__ = ("MCOFCIMMEKC", "EJNINFFFKJP")
    MCOFCIMMEKC_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    MCOFCIMMEKC: _containers.RepeatedCompositeFieldContainer[_FDKIIFFFCGJ_pb2.FDKIIFFFCGJ]
    EJNINFFFKJP: int
    def __init__(self, MCOFCIMMEKC: _Optional[_Iterable[_Union[_FDKIIFFFCGJ_pb2.FDKIIFFFCGJ, _Mapping]]] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
