from genshin.packet.proto import JDBKONEMPDD_pb2 as _JDBKONEMPDD_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EFLCLAIMPLD(_message.Message):
    __slots__ = ("AAEHPGKINOP",)
    AAEHPGKINOP_FIELD_NUMBER: _ClassVar[int]
    AAEHPGKINOP: _containers.RepeatedCompositeFieldContainer[_JDBKONEMPDD_pb2.JDBKONEMPDD]
    def __init__(self, AAEHPGKINOP: _Optional[_Iterable[_Union[_JDBKONEMPDD_pb2.JDBKONEMPDD, _Mapping]]] = ...) -> None: ...
