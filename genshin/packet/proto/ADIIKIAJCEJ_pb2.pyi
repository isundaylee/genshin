from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ADIIKIAJCEJ(_message.Message):
    __slots__ = ("CBPAGDLIMIJ", "JCOJAPMJDNM")
    class CBPAGDLIMIJEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    CBPAGDLIMIJ_FIELD_NUMBER: _ClassVar[int]
    JCOJAPMJDNM_FIELD_NUMBER: _ClassVar[int]
    CBPAGDLIMIJ: _containers.ScalarMap[int, int]
    JCOJAPMJDNM: int
    def __init__(self, CBPAGDLIMIJ: _Optional[_Mapping[int, int]] = ..., JCOJAPMJDNM: _Optional[int] = ...) -> None: ...
