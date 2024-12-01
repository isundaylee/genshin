from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BKJEFHMCCNM(_message.Message):
    __slots__ = ("ABPHKNKNJIC", "GEFNMJHABGJ", "OAGLNCFKONI")
    class ABPHKNKNJICEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    ABPHKNKNJIC_FIELD_NUMBER: _ClassVar[int]
    GEFNMJHABGJ_FIELD_NUMBER: _ClassVar[int]
    OAGLNCFKONI_FIELD_NUMBER: _ClassVar[int]
    ABPHKNKNJIC: _containers.ScalarMap[int, int]
    GEFNMJHABGJ: int
    OAGLNCFKONI: int
    def __init__(self, ABPHKNKNJIC: _Optional[_Mapping[int, int]] = ..., GEFNMJHABGJ: _Optional[int] = ..., OAGLNCFKONI: _Optional[int] = ...) -> None: ...
