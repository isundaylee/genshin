from genshin.packet.proto import LCFCOCGNPOM_pb2 as _LCFCOCGNPOM_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LLPEEGBJOFA(_message.Message):
    __slots__ = ("MIEAFINBNDK", "OELCNLOJHHE", "IPEIHFLKPJI", "CFLBHGMKAPA")
    MIEAFINBNDK_FIELD_NUMBER: _ClassVar[int]
    OELCNLOJHHE_FIELD_NUMBER: _ClassVar[int]
    IPEIHFLKPJI_FIELD_NUMBER: _ClassVar[int]
    CFLBHGMKAPA_FIELD_NUMBER: _ClassVar[int]
    MIEAFINBNDK: _containers.RepeatedCompositeFieldContainer[_LCFCOCGNPOM_pb2.LCFCOCGNPOM]
    OELCNLOJHHE: int
    IPEIHFLKPJI: int
    CFLBHGMKAPA: bool
    def __init__(self, MIEAFINBNDK: _Optional[_Iterable[_Union[_LCFCOCGNPOM_pb2.LCFCOCGNPOM, _Mapping]]] = ..., OELCNLOJHHE: _Optional[int] = ..., IPEIHFLKPJI: _Optional[int] = ..., CFLBHGMKAPA: bool = ...) -> None: ...
