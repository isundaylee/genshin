from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LDLHMMFAIPH(_message.Message):
    __slots__ = ("PCMEHIJMDHN", "FFHPDCIBKOD")
    class PCMEHIJMDHNEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    PCMEHIJMDHN_FIELD_NUMBER: _ClassVar[int]
    FFHPDCIBKOD_FIELD_NUMBER: _ClassVar[int]
    PCMEHIJMDHN: _containers.ScalarMap[int, int]
    FFHPDCIBKOD: int
    def __init__(self, PCMEHIJMDHN: _Optional[_Mapping[int, int]] = ..., FFHPDCIBKOD: _Optional[int] = ...) -> None: ...
