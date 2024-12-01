from genshin.packet.proto import HPMJAJCBEGH_pb2 as _HPMJAJCBEGH_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KPJNBBDBAEJ(_message.Message):
    __slots__ = ("JPPDBKKNHPA", "DNBEFLJLAMB", "EJNINFFFKJP")
    JPPDBKKNHPA_FIELD_NUMBER: _ClassVar[int]
    DNBEFLJLAMB_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    JPPDBKKNHPA: _containers.RepeatedCompositeFieldContainer[_HPMJAJCBEGH_pb2.HPMJAJCBEGH]
    DNBEFLJLAMB: int
    EJNINFFFKJP: int
    def __init__(self, JPPDBKKNHPA: _Optional[_Iterable[_Union[_HPMJAJCBEGH_pb2.HPMJAJCBEGH, _Mapping]]] = ..., DNBEFLJLAMB: _Optional[int] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
