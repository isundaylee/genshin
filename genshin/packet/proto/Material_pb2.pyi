from genshin.packet.proto import JDNCHHPCNMD_pb2 as _JDNCHHPCNMD_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Material(_message.Message):
    __slots__ = ("KPNDJLKLKFO", "OFIPBEGGHCD")
    KPNDJLKLKFO_FIELD_NUMBER: _ClassVar[int]
    OFIPBEGGHCD_FIELD_NUMBER: _ClassVar[int]
    KPNDJLKLKFO: _JDNCHHPCNMD_pb2.JDNCHHPCNMD
    OFIPBEGGHCD: int
    def __init__(self, KPNDJLKLKFO: _Optional[_Union[_JDNCHHPCNMD_pb2.JDNCHHPCNMD, _Mapping]] = ..., OFIPBEGGHCD: _Optional[int] = ...) -> None: ...
