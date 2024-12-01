from genshin.packet.proto import HDCFBPPBPLF_pb2 as _HDCFBPPBPLF_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ODBBHKMEONI(_message.Message):
    __slots__ = ("PMJGJNILMBP", "EAIPGEMKNPO", "BODIEJCLGMB")
    PMJGJNILMBP_FIELD_NUMBER: _ClassVar[int]
    EAIPGEMKNPO_FIELD_NUMBER: _ClassVar[int]
    BODIEJCLGMB_FIELD_NUMBER: _ClassVar[int]
    PMJGJNILMBP: _containers.RepeatedCompositeFieldContainer[_HDCFBPPBPLF_pb2.HDCFBPPBPLF]
    EAIPGEMKNPO: int
    BODIEJCLGMB: int
    def __init__(self, PMJGJNILMBP: _Optional[_Iterable[_Union[_HDCFBPPBPLF_pb2.HDCFBPPBPLF, _Mapping]]] = ..., EAIPGEMKNPO: _Optional[int] = ..., BODIEJCLGMB: _Optional[int] = ...) -> None: ...
