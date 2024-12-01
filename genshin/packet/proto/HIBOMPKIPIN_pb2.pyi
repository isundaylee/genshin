from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HIBOMPKIPIN(_message.Message):
    __slots__ = ("OGLBNKAEEMI", "AJKPLBPKCAB", "HPMNAOJDHME", "OALIOHAMLGN", "MPFLDFDOGAI", "APCKFLANKIL")
    class OGLBNKAEEMIEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class AJKPLBPKCABEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    OGLBNKAEEMI_FIELD_NUMBER: _ClassVar[int]
    AJKPLBPKCAB_FIELD_NUMBER: _ClassVar[int]
    HPMNAOJDHME_FIELD_NUMBER: _ClassVar[int]
    OALIOHAMLGN_FIELD_NUMBER: _ClassVar[int]
    MPFLDFDOGAI_FIELD_NUMBER: _ClassVar[int]
    APCKFLANKIL_FIELD_NUMBER: _ClassVar[int]
    OGLBNKAEEMI: _containers.ScalarMap[int, int]
    AJKPLBPKCAB: _containers.ScalarMap[int, int]
    HPMNAOJDHME: int
    OALIOHAMLGN: int
    MPFLDFDOGAI: bool
    APCKFLANKIL: bool
    def __init__(self, OGLBNKAEEMI: _Optional[_Mapping[int, int]] = ..., AJKPLBPKCAB: _Optional[_Mapping[int, int]] = ..., HPMNAOJDHME: _Optional[int] = ..., OALIOHAMLGN: _Optional[int] = ..., MPFLDFDOGAI: bool = ..., APCKFLANKIL: bool = ...) -> None: ...
