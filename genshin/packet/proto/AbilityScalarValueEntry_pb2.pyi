from genshin.packet.proto import AbilityString_pb2 as _AbilityString_pb2
from genshin.packet.proto import AbilityScalarType_pb2 as _AbilityScalarType_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AbilityScalarValueEntry(_message.Message):
    __slots__ = ("key", "value_type", "float_value", "string_value", "int_value", "uint_value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    UINT_VALUE_FIELD_NUMBER: _ClassVar[int]
    key: _AbilityString_pb2.AbilityString
    value_type: _AbilityScalarType_pb2.AbilityScalarType
    float_value: float
    string_value: str
    int_value: int
    uint_value: int
    def __init__(self, key: _Optional[_Union[_AbilityString_pb2.AbilityString, _Mapping]] = ..., value_type: _Optional[_Union[_AbilityScalarType_pb2.AbilityScalarType, str]] = ..., float_value: _Optional[float] = ..., string_value: _Optional[str] = ..., int_value: _Optional[int] = ..., uint_value: _Optional[int] = ...) -> None: ...
