from genshin.packet.proto import IDODJEOKCPO_pb2 as _IDODJEOKCPO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EBLJJGFCCJF(_message.Message):
    __slots__ = ("FGOPNKBDFCK", "PMJGJNILMBP", "BODIEJCLGMB", "MPNJAOCKMAH", "EAIPGEMKNPO", "OMENIAMEDCE")
    FGOPNKBDFCK_FIELD_NUMBER: _ClassVar[int]
    PMJGJNILMBP_FIELD_NUMBER: _ClassVar[int]
    BODIEJCLGMB_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    EAIPGEMKNPO_FIELD_NUMBER: _ClassVar[int]
    OMENIAMEDCE_FIELD_NUMBER: _ClassVar[int]
    FGOPNKBDFCK: _containers.RepeatedScalarFieldContainer[int]
    PMJGJNILMBP: _containers.RepeatedCompositeFieldContainer[_IDODJEOKCPO_pb2.IDODJEOKCPO]
    BODIEJCLGMB: int
    MPNJAOCKMAH: int
    EAIPGEMKNPO: int
    OMENIAMEDCE: bool
    def __init__(self, FGOPNKBDFCK: _Optional[_Iterable[int]] = ..., PMJGJNILMBP: _Optional[_Iterable[_Union[_IDODJEOKCPO_pb2.IDODJEOKCPO, _Mapping]]] = ..., BODIEJCLGMB: _Optional[int] = ..., MPNJAOCKMAH: _Optional[int] = ..., EAIPGEMKNPO: _Optional[int] = ..., OMENIAMEDCE: bool = ...) -> None: ...
