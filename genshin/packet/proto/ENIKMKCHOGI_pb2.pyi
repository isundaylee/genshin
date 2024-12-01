from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ENIKMKCHOGI(_message.Message):
    __slots__ = ("PGIANMGPDED", "HCJFDJHILAM", "CKPHCAGONKG", "DOCJDOGOCKM", "LDIMHBKFHIF")
    class PGIANMGPDEDEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    PGIANMGPDED_FIELD_NUMBER: _ClassVar[int]
    HCJFDJHILAM_FIELD_NUMBER: _ClassVar[int]
    CKPHCAGONKG_FIELD_NUMBER: _ClassVar[int]
    DOCJDOGOCKM_FIELD_NUMBER: _ClassVar[int]
    LDIMHBKFHIF_FIELD_NUMBER: _ClassVar[int]
    PGIANMGPDED: _containers.ScalarMap[int, int]
    HCJFDJHILAM: bool
    CKPHCAGONKG: int
    DOCJDOGOCKM: int
    LDIMHBKFHIF: int
    def __init__(self, PGIANMGPDED: _Optional[_Mapping[int, int]] = ..., HCJFDJHILAM: bool = ..., CKPHCAGONKG: _Optional[int] = ..., DOCJDOGOCKM: _Optional[int] = ..., LDIMHBKFHIF: _Optional[int] = ...) -> None: ...
