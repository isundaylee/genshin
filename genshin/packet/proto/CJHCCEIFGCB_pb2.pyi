from genshin.packet.proto import BFFALDPOKFE_pb2 as _BFFALDPOKFE_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CJHCCEIFGCB(_message.Message):
    __slots__ = ("PMJGJNILMBP", "BODIEJCLGMB", "EAIPGEMKNPO")
    PMJGJNILMBP_FIELD_NUMBER: _ClassVar[int]
    BODIEJCLGMB_FIELD_NUMBER: _ClassVar[int]
    EAIPGEMKNPO_FIELD_NUMBER: _ClassVar[int]
    PMJGJNILMBP: _containers.RepeatedCompositeFieldContainer[_BFFALDPOKFE_pb2.BFFALDPOKFE]
    BODIEJCLGMB: int
    EAIPGEMKNPO: int
    def __init__(self, PMJGJNILMBP: _Optional[_Iterable[_Union[_BFFALDPOKFE_pb2.BFFALDPOKFE, _Mapping]]] = ..., BODIEJCLGMB: _Optional[int] = ..., EAIPGEMKNPO: _Optional[int] = ...) -> None: ...
