from genshin.packet.proto import PropValue_pb2 as _PropValue_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PropPair(_message.Message):
    __slots__ = ("type", "prop_value")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PROP_VALUE_FIELD_NUMBER: _ClassVar[int]
    type: int
    prop_value: _PropValue_pb2.PropValue
    def __init__(self, type: _Optional[int] = ..., prop_value: _Optional[_Union[_PropValue_pb2.PropValue, _Mapping]] = ...) -> None: ...
