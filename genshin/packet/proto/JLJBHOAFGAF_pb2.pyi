from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class JLJBHOAFGAF(_message.Message):
    __slots__ = ("MJDAOHHPPPC", "DBFGJNBBDKC")
    class MJDAOHHPPPCEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    MJDAOHHPPPC_FIELD_NUMBER: _ClassVar[int]
    DBFGJNBBDKC_FIELD_NUMBER: _ClassVar[int]
    MJDAOHHPPPC: _containers.ScalarMap[int, int]
    DBFGJNBBDKC: int
    def __init__(self, MJDAOHHPPPC: _Optional[_Mapping[int, int]] = ..., DBFGJNBBDKC: _Optional[int] = ...) -> None: ...
