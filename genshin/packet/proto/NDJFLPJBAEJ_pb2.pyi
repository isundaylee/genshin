from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NDJFLPJBAEJ(_message.Message):
    __slots__ = ("JIOEOGOLPFD", "OJIFCJGPCBK", "JAPEOEJLNPD", "PIEAPGEPMLF", "NCCPPHNNPBF")
    class JIOEOGOLPFDEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    JIOEOGOLPFD_FIELD_NUMBER: _ClassVar[int]
    OJIFCJGPCBK_FIELD_NUMBER: _ClassVar[int]
    JAPEOEJLNPD_FIELD_NUMBER: _ClassVar[int]
    PIEAPGEPMLF_FIELD_NUMBER: _ClassVar[int]
    NCCPPHNNPBF_FIELD_NUMBER: _ClassVar[int]
    JIOEOGOLPFD: _containers.ScalarMap[int, int]
    OJIFCJGPCBK: bool
    JAPEOEJLNPD: int
    PIEAPGEPMLF: int
    NCCPPHNNPBF: int
    def __init__(self, JIOEOGOLPFD: _Optional[_Mapping[int, int]] = ..., OJIFCJGPCBK: bool = ..., JAPEOEJLNPD: _Optional[int] = ..., PIEAPGEPMLF: _Optional[int] = ..., NCCPPHNNPBF: _Optional[int] = ...) -> None: ...
