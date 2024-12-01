from genshin.packet.proto import PropValue_pb2 as _PropValue_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KEPJHNGFNDP(_message.Message):
    __slots__ = ("MGDFIJMHGND",)
    MGDFIJMHGND_FIELD_NUMBER: _ClassVar[int]
    MGDFIJMHGND: _containers.RepeatedCompositeFieldContainer[_PropValue_pb2.PropValue]
    def __init__(self, MGDFIJMHGND: _Optional[_Iterable[_Union[_PropValue_pb2.PropValue, _Mapping]]] = ...) -> None: ...
