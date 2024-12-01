from genshin.packet.proto import JICKPPDLOHC_pb2 as _JICKPPDLOHC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OBKKOMBKMFM(_message.Message):
    __slots__ = ("BNJOJBOPMFJ", "JDMCFOKOBHK", "JAHLENGHNMJ")
    BNJOJBOPMFJ_FIELD_NUMBER: _ClassVar[int]
    JDMCFOKOBHK_FIELD_NUMBER: _ClassVar[int]
    JAHLENGHNMJ_FIELD_NUMBER: _ClassVar[int]
    BNJOJBOPMFJ: _containers.RepeatedCompositeFieldContainer[_JICKPPDLOHC_pb2.JICKPPDLOHC]
    JDMCFOKOBHK: _containers.RepeatedScalarFieldContainer[int]
    JAHLENGHNMJ: int
    def __init__(self, BNJOJBOPMFJ: _Optional[_Iterable[_Union[_JICKPPDLOHC_pb2.JICKPPDLOHC, _Mapping]]] = ..., JDMCFOKOBHK: _Optional[_Iterable[int]] = ..., JAHLENGHNMJ: _Optional[int] = ...) -> None: ...
