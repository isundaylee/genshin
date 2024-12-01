from genshin.packet.proto import JBFHHGEPHLJ_pb2 as _JBFHHGEPHLJ_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FBKPOILGBLD(_message.Message):
    __slots__ = ("EECLCLKGNOP", "DOPFDKDHBEI", "IGBDOEBPPHO", "EJNINFFFKJP")
    EECLCLKGNOP_FIELD_NUMBER: _ClassVar[int]
    DOPFDKDHBEI_FIELD_NUMBER: _ClassVar[int]
    IGBDOEBPPHO_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    EECLCLKGNOP: _containers.RepeatedCompositeFieldContainer[_JBFHHGEPHLJ_pb2.JBFHHGEPHLJ]
    DOPFDKDHBEI: _containers.RepeatedScalarFieldContainer[int]
    IGBDOEBPPHO: int
    EJNINFFFKJP: int
    def __init__(self, EECLCLKGNOP: _Optional[_Iterable[_Union[_JBFHHGEPHLJ_pb2.JBFHHGEPHLJ, _Mapping]]] = ..., DOPFDKDHBEI: _Optional[_Iterable[int]] = ..., IGBDOEBPPHO: _Optional[int] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
