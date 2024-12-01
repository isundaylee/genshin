from genshin.packet.proto import MBJEPLKJNIG_pb2 as _MBJEPLKJNIG_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MOBLFMPCJKE(_message.Message):
    __slots__ = ("DMIGLEHJPDC", "AAFLLAHKNJE")
    DMIGLEHJPDC_FIELD_NUMBER: _ClassVar[int]
    AAFLLAHKNJE_FIELD_NUMBER: _ClassVar[int]
    DMIGLEHJPDC: _containers.RepeatedScalarFieldContainer[int]
    AAFLLAHKNJE: _containers.RepeatedCompositeFieldContainer[_MBJEPLKJNIG_pb2.MBJEPLKJNIG]
    def __init__(self, DMIGLEHJPDC: _Optional[_Iterable[int]] = ..., AAFLLAHKNJE: _Optional[_Iterable[_Union[_MBJEPLKJNIG_pb2.MBJEPLKJNIG, _Mapping]]] = ...) -> None: ...
