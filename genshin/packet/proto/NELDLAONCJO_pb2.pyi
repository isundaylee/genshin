from genshin.packet.proto import JICKPPDLOHC_pb2 as _JICKPPDLOHC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NELDLAONCJO(_message.Message):
    __slots__ = ("NJCAFAAGMJK", "BNJOJBOPMFJ", "AGHCICLCICK")
    NJCAFAAGMJK_FIELD_NUMBER: _ClassVar[int]
    BNJOJBOPMFJ_FIELD_NUMBER: _ClassVar[int]
    AGHCICLCICK_FIELD_NUMBER: _ClassVar[int]
    NJCAFAAGMJK: _containers.RepeatedScalarFieldContainer[int]
    BNJOJBOPMFJ: _containers.RepeatedCompositeFieldContainer[_JICKPPDLOHC_pb2.JICKPPDLOHC]
    AGHCICLCICK: int
    def __init__(self, NJCAFAAGMJK: _Optional[_Iterable[int]] = ..., BNJOJBOPMFJ: _Optional[_Iterable[_Union[_JICKPPDLOHC_pb2.JICKPPDLOHC, _Mapping]]] = ..., AGHCICLCICK: _Optional[int] = ...) -> None: ...
