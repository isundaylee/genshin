from genshin.packet.proto import PAHOICKNMEP_pb2 as _PAHOICKNMEP_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JMHOGADNPCE(_message.Message):
    __slots__ = ("OENAHHEEFLG", "MPNJAOCKMAH", "EAIPGEMKNPO", "JBFDOGPAKKC", "AELJDIPLELM")
    OENAHHEEFLG_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    EAIPGEMKNPO_FIELD_NUMBER: _ClassVar[int]
    JBFDOGPAKKC_FIELD_NUMBER: _ClassVar[int]
    AELJDIPLELM_FIELD_NUMBER: _ClassVar[int]
    OENAHHEEFLG: _containers.RepeatedCompositeFieldContainer[_PAHOICKNMEP_pb2.PAHOICKNMEP]
    MPNJAOCKMAH: int
    EAIPGEMKNPO: int
    JBFDOGPAKKC: int
    AELJDIPLELM: int
    def __init__(self, OENAHHEEFLG: _Optional[_Iterable[_Union[_PAHOICKNMEP_pb2.PAHOICKNMEP, _Mapping]]] = ..., MPNJAOCKMAH: _Optional[int] = ..., EAIPGEMKNPO: _Optional[int] = ..., JBFDOGPAKKC: _Optional[int] = ..., AELJDIPLELM: _Optional[int] = ...) -> None: ...
