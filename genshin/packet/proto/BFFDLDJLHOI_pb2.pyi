from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BFFDLDJLHOI(_message.Message):
    __slots__ = ("CODADNFPICG", "PNAIIFHACPB", "MKPAMNICKDB", "NJJKMEFEEIH", "EPLDGLECANO")
    class CODADNFPICGEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    CODADNFPICG_FIELD_NUMBER: _ClassVar[int]
    PNAIIFHACPB_FIELD_NUMBER: _ClassVar[int]
    MKPAMNICKDB_FIELD_NUMBER: _ClassVar[int]
    NJJKMEFEEIH_FIELD_NUMBER: _ClassVar[int]
    EPLDGLECANO_FIELD_NUMBER: _ClassVar[int]
    CODADNFPICG: _containers.ScalarMap[int, int]
    PNAIIFHACPB: int
    MKPAMNICKDB: int
    NJJKMEFEEIH: int
    EPLDGLECANO: int
    def __init__(self, CODADNFPICG: _Optional[_Mapping[int, int]] = ..., PNAIIFHACPB: _Optional[int] = ..., MKPAMNICKDB: _Optional[int] = ..., NJJKMEFEEIH: _Optional[int] = ..., EPLDGLECANO: _Optional[int] = ...) -> None: ...
