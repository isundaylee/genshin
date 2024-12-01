from genshin.packet.proto import IDODJEOKCPO_pb2 as _IDODJEOKCPO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HDOJJMMNLIC(_message.Message):
    __slots__ = ("PMJGJNILMBP", "EAIPGEMKNPO", "AKCLJOALODI", "BODIEJCLGMB", "MPNJAOCKMAH")
    PMJGJNILMBP_FIELD_NUMBER: _ClassVar[int]
    EAIPGEMKNPO_FIELD_NUMBER: _ClassVar[int]
    AKCLJOALODI_FIELD_NUMBER: _ClassVar[int]
    BODIEJCLGMB_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    PMJGJNILMBP: _containers.RepeatedCompositeFieldContainer[_IDODJEOKCPO_pb2.IDODJEOKCPO]
    EAIPGEMKNPO: int
    AKCLJOALODI: bool
    BODIEJCLGMB: int
    MPNJAOCKMAH: int
    def __init__(self, PMJGJNILMBP: _Optional[_Iterable[_Union[_IDODJEOKCPO_pb2.IDODJEOKCPO, _Mapping]]] = ..., EAIPGEMKNPO: _Optional[int] = ..., AKCLJOALODI: bool = ..., BODIEJCLGMB: _Optional[int] = ..., MPNJAOCKMAH: _Optional[int] = ...) -> None: ...
