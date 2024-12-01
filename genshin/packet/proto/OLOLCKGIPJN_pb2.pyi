from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class OLOLCKGIPJN(_message.Message):
    __slots__ = ("GBHBBLGHDLJ", "HGBBGLKPLFI", "APPIGJMKEGG", "LAILPNOOAJC", "MPFLDFDOGAI", "NMIKCMLKNDM", "EMNEIHDPFPM", "FBEJHLODCFN")
    class GBHBBLGHDLJEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    GBHBBLGHDLJ_FIELD_NUMBER: _ClassVar[int]
    HGBBGLKPLFI_FIELD_NUMBER: _ClassVar[int]
    APPIGJMKEGG_FIELD_NUMBER: _ClassVar[int]
    LAILPNOOAJC_FIELD_NUMBER: _ClassVar[int]
    MPFLDFDOGAI_FIELD_NUMBER: _ClassVar[int]
    NMIKCMLKNDM_FIELD_NUMBER: _ClassVar[int]
    EMNEIHDPFPM_FIELD_NUMBER: _ClassVar[int]
    FBEJHLODCFN_FIELD_NUMBER: _ClassVar[int]
    GBHBBLGHDLJ: _containers.ScalarMap[int, int]
    HGBBGLKPLFI: int
    APPIGJMKEGG: int
    LAILPNOOAJC: bool
    MPFLDFDOGAI: bool
    NMIKCMLKNDM: int
    EMNEIHDPFPM: int
    FBEJHLODCFN: int
    def __init__(self, GBHBBLGHDLJ: _Optional[_Mapping[int, int]] = ..., HGBBGLKPLFI: _Optional[int] = ..., APPIGJMKEGG: _Optional[int] = ..., LAILPNOOAJC: bool = ..., MPFLDFDOGAI: bool = ..., NMIKCMLKNDM: _Optional[int] = ..., EMNEIHDPFPM: _Optional[int] = ..., FBEJHLODCFN: _Optional[int] = ...) -> None: ...
