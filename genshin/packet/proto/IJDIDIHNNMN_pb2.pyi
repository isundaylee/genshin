from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class IJDIDIHNNMN(_message.Message):
    __slots__ = ("JIOEOGOLPFD", "JAPEOEJLNPD", "FFHPDCIBKOD", "PIEAPGEPMLF", "CJDIMMAIMHO", "OJIFCJGPCBK")
    class JIOEOGOLPFDEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    JIOEOGOLPFD_FIELD_NUMBER: _ClassVar[int]
    JAPEOEJLNPD_FIELD_NUMBER: _ClassVar[int]
    FFHPDCIBKOD_FIELD_NUMBER: _ClassVar[int]
    PIEAPGEPMLF_FIELD_NUMBER: _ClassVar[int]
    CJDIMMAIMHO_FIELD_NUMBER: _ClassVar[int]
    OJIFCJGPCBK_FIELD_NUMBER: _ClassVar[int]
    JIOEOGOLPFD: _containers.ScalarMap[int, int]
    JAPEOEJLNPD: int
    FFHPDCIBKOD: int
    PIEAPGEPMLF: int
    CJDIMMAIMHO: int
    OJIFCJGPCBK: bool
    def __init__(self, JIOEOGOLPFD: _Optional[_Mapping[int, int]] = ..., JAPEOEJLNPD: _Optional[int] = ..., FFHPDCIBKOD: _Optional[int] = ..., PIEAPGEPMLF: _Optional[int] = ..., CJDIMMAIMHO: _Optional[int] = ..., OJIFCJGPCBK: bool = ...) -> None: ...
