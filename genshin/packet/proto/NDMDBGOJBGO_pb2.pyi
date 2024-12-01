from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NDMDBGOJBGO(_message.Message):
    __slots__ = ("GLJDLOHDOGL", "EAIPGEMKNPO", "GLKNGDDNOCN")
    class GLJDLOHDOGLEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    GLJDLOHDOGL_FIELD_NUMBER: _ClassVar[int]
    EAIPGEMKNPO_FIELD_NUMBER: _ClassVar[int]
    GLKNGDDNOCN_FIELD_NUMBER: _ClassVar[int]
    GLJDLOHDOGL: _containers.ScalarMap[int, int]
    EAIPGEMKNPO: int
    GLKNGDDNOCN: bool
    def __init__(self, GLJDLOHDOGL: _Optional[_Mapping[int, int]] = ..., EAIPGEMKNPO: _Optional[int] = ..., GLKNGDDNOCN: bool = ...) -> None: ...
