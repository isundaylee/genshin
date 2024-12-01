from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GDHBFFBPIIJ(_message.Message):
    __slots__ = ("ENEEHFPJBKL", "EIFLGADNMPA", "AJEKGIJODHF")
    class ENEEHFPJBKLEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    ENEEHFPJBKL_FIELD_NUMBER: _ClassVar[int]
    EIFLGADNMPA_FIELD_NUMBER: _ClassVar[int]
    AJEKGIJODHF_FIELD_NUMBER: _ClassVar[int]
    ENEEHFPJBKL: _containers.ScalarMap[str, int]
    EIFLGADNMPA: int
    AJEKGIJODHF: bool
    def __init__(self, ENEEHFPJBKL: _Optional[_Mapping[str, int]] = ..., EIFLGADNMPA: _Optional[int] = ..., AJEKGIJODHF: bool = ...) -> None: ...
