from genshin.packet.proto import AbilityString_pb2 as _AbilityString_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ModifierProperty(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: _AbilityString_pb2.AbilityString
    value: float
    def __init__(self, key: _Optional[_Union[_AbilityString_pb2.AbilityString, _Mapping]] = ..., value: _Optional[float] = ...) -> None: ...
