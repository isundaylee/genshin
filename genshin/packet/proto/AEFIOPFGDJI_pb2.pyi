from genshin.packet.proto import NEIFCKNFNAK_pb2 as _NEIFCKNFNAK_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AEFIOPFGDJI(_message.Message):
    __slots__ = ("DDDBBIPMMJA", "IGHMLOENDHP", "PGEJGJMGGOG", "GLKNGDDNOCN", "EAIPGEMKNPO")
    DDDBBIPMMJA_FIELD_NUMBER: _ClassVar[int]
    IGHMLOENDHP_FIELD_NUMBER: _ClassVar[int]
    PGEJGJMGGOG_FIELD_NUMBER: _ClassVar[int]
    GLKNGDDNOCN_FIELD_NUMBER: _ClassVar[int]
    EAIPGEMKNPO_FIELD_NUMBER: _ClassVar[int]
    DDDBBIPMMJA: _containers.RepeatedScalarFieldContainer[int]
    IGHMLOENDHP: _containers.RepeatedScalarFieldContainer[int]
    PGEJGJMGGOG: _containers.RepeatedCompositeFieldContainer[_NEIFCKNFNAK_pb2.NEIFCKNFNAK]
    GLKNGDDNOCN: bool
    EAIPGEMKNPO: int
    def __init__(self, DDDBBIPMMJA: _Optional[_Iterable[int]] = ..., IGHMLOENDHP: _Optional[_Iterable[int]] = ..., PGEJGJMGGOG: _Optional[_Iterable[_Union[_NEIFCKNFNAK_pb2.NEIFCKNFNAK, _Mapping]]] = ..., GLKNGDDNOCN: bool = ..., EAIPGEMKNPO: _Optional[int] = ...) -> None: ...
