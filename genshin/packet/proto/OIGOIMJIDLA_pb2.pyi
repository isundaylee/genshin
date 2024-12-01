from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class OIGOIMJIDLA(_message.Message):
    __slots__ = ("MDMKONDIDGE", "EDOGEDEIDNM", "CPFFKAABOGD")
    class MDMKONDIDGEEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    MDMKONDIDGE_FIELD_NUMBER: _ClassVar[int]
    EDOGEDEIDNM_FIELD_NUMBER: _ClassVar[int]
    CPFFKAABOGD_FIELD_NUMBER: _ClassVar[int]
    MDMKONDIDGE: _containers.ScalarMap[int, int]
    EDOGEDEIDNM: int
    CPFFKAABOGD: int
    def __init__(self, MDMKONDIDGE: _Optional[_Mapping[int, int]] = ..., EDOGEDEIDNM: _Optional[int] = ..., CPFFKAABOGD: _Optional[int] = ...) -> None: ...
