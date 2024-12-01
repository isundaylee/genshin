from genshin.packet.proto import HLPLMKKOGNK_pb2 as _HLPLMKKOGNK_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CACGLIBJIIE(_message.Message):
    __slots__ = ("JEILNPELIAB", "type")
    JEILNPELIAB_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    JEILNPELIAB: _containers.RepeatedScalarFieldContainer[int]
    type: _HLPLMKKOGNK_pb2.HLPLMKKOGNK
    def __init__(self, JEILNPELIAB: _Optional[_Iterable[int]] = ..., type: _Optional[_Union[_HLPLMKKOGNK_pb2.HLPLMKKOGNK, str]] = ...) -> None: ...
