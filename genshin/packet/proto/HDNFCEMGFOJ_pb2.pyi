from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HDNFCEMGFOJ(_message.Message):
    __slots__ = ("CGCNGJNCPGH", "ILGOCDGLHMJ")
    class CGCNGJNCPGHEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class ILGOCDGLHMJEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    CGCNGJNCPGH_FIELD_NUMBER: _ClassVar[int]
    ILGOCDGLHMJ_FIELD_NUMBER: _ClassVar[int]
    CGCNGJNCPGH: _containers.ScalarMap[int, int]
    ILGOCDGLHMJ: _containers.ScalarMap[int, int]
    def __init__(self, CGCNGJNCPGH: _Optional[_Mapping[int, int]] = ..., ILGOCDGLHMJ: _Optional[_Mapping[int, int]] = ...) -> None: ...
