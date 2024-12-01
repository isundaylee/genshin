from genshin.packet.proto import OFIFGOOPCDO_pb2 as _OFIFGOOPCDO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HIBENGBCKLE(_message.Message):
    __slots__ = ("PMJGJNILMBP", "EAIPGEMKNPO", "BODIEJCLGMB")
    PMJGJNILMBP_FIELD_NUMBER: _ClassVar[int]
    EAIPGEMKNPO_FIELD_NUMBER: _ClassVar[int]
    BODIEJCLGMB_FIELD_NUMBER: _ClassVar[int]
    PMJGJNILMBP: _containers.RepeatedCompositeFieldContainer[_OFIFGOOPCDO_pb2.OFIFGOOPCDO]
    EAIPGEMKNPO: int
    BODIEJCLGMB: int
    def __init__(self, PMJGJNILMBP: _Optional[_Iterable[_Union[_OFIFGOOPCDO_pb2.OFIFGOOPCDO, _Mapping]]] = ..., EAIPGEMKNPO: _Optional[int] = ..., BODIEJCLGMB: _Optional[int] = ...) -> None: ...
