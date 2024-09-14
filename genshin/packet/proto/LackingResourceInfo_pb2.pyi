from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LackingResourceInfo(_message.Message):
    __slots__ = ("JAODPKILOHD", "IGIDHGKOODO", "OBAKLGMMOEO", "LELGNGJOJAI", "AOECKDLECIJ", "ACAAJJBNCDM", "LHEGFHKBMKF", "HIIHFCBJLDI", "HCPKDCNKPGD")
    class IGIDHGKOODOEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class LELGNGJOJAIEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class ACAAJJBNCDMEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    JAODPKILOHD_FIELD_NUMBER: _ClassVar[int]
    IGIDHGKOODO_FIELD_NUMBER: _ClassVar[int]
    OBAKLGMMOEO_FIELD_NUMBER: _ClassVar[int]
    LELGNGJOJAI_FIELD_NUMBER: _ClassVar[int]
    AOECKDLECIJ_FIELD_NUMBER: _ClassVar[int]
    ACAAJJBNCDM_FIELD_NUMBER: _ClassVar[int]
    LHEGFHKBMKF_FIELD_NUMBER: _ClassVar[int]
    HIIHFCBJLDI_FIELD_NUMBER: _ClassVar[int]
    HCPKDCNKPGD_FIELD_NUMBER: _ClassVar[int]
    JAODPKILOHD: _containers.RepeatedScalarFieldContainer[int]
    IGIDHGKOODO: _containers.ScalarMap[int, int]
    OBAKLGMMOEO: _containers.RepeatedScalarFieldContainer[int]
    LELGNGJOJAI: _containers.ScalarMap[int, int]
    AOECKDLECIJ: _containers.RepeatedScalarFieldContainer[int]
    ACAAJJBNCDM: _containers.ScalarMap[int, int]
    LHEGFHKBMKF: _containers.RepeatedScalarFieldContainer[int]
    HIIHFCBJLDI: _containers.RepeatedScalarFieldContainer[int]
    HCPKDCNKPGD: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, JAODPKILOHD: _Optional[_Iterable[int]] = ..., IGIDHGKOODO: _Optional[_Mapping[int, int]] = ..., OBAKLGMMOEO: _Optional[_Iterable[int]] = ..., LELGNGJOJAI: _Optional[_Mapping[int, int]] = ..., AOECKDLECIJ: _Optional[_Iterable[int]] = ..., ACAAJJBNCDM: _Optional[_Mapping[int, int]] = ..., LHEGFHKBMKF: _Optional[_Iterable[int]] = ..., HIIHFCBJLDI: _Optional[_Iterable[int]] = ..., HCPKDCNKPGD: _Optional[_Iterable[int]] = ...) -> None: ...
