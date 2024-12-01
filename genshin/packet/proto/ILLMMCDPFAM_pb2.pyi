from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ILLMMCDPFAM(_message.Message):
    __slots__ = ("GGEGDEOHEIE", "OMPKOEJIOKN", "DHGJOAKPPOC", "OIHINGLBFCE", "ONBFFAMKPPK", "DCGOEAEFEML", "JFKKMFFPNGI", "BMMEJPDMMCH", "JJEAODIEJCL")
    class ONBFFAMKPPKEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class BMMEJPDMMCHEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class JJEAODIEJCLEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    GGEGDEOHEIE_FIELD_NUMBER: _ClassVar[int]
    OMPKOEJIOKN_FIELD_NUMBER: _ClassVar[int]
    DHGJOAKPPOC_FIELD_NUMBER: _ClassVar[int]
    OIHINGLBFCE_FIELD_NUMBER: _ClassVar[int]
    ONBFFAMKPPK_FIELD_NUMBER: _ClassVar[int]
    DCGOEAEFEML_FIELD_NUMBER: _ClassVar[int]
    JFKKMFFPNGI_FIELD_NUMBER: _ClassVar[int]
    BMMEJPDMMCH_FIELD_NUMBER: _ClassVar[int]
    JJEAODIEJCL_FIELD_NUMBER: _ClassVar[int]
    GGEGDEOHEIE: _containers.RepeatedScalarFieldContainer[int]
    OMPKOEJIOKN: _containers.RepeatedScalarFieldContainer[int]
    DHGJOAKPPOC: _containers.RepeatedScalarFieldContainer[int]
    OIHINGLBFCE: _containers.RepeatedScalarFieldContainer[int]
    ONBFFAMKPPK: _containers.ScalarMap[int, int]
    DCGOEAEFEML: _containers.RepeatedScalarFieldContainer[int]
    JFKKMFFPNGI: _containers.RepeatedScalarFieldContainer[int]
    BMMEJPDMMCH: _containers.ScalarMap[int, int]
    JJEAODIEJCL: _containers.ScalarMap[int, int]
    def __init__(self, GGEGDEOHEIE: _Optional[_Iterable[int]] = ..., OMPKOEJIOKN: _Optional[_Iterable[int]] = ..., DHGJOAKPPOC: _Optional[_Iterable[int]] = ..., OIHINGLBFCE: _Optional[_Iterable[int]] = ..., ONBFFAMKPPK: _Optional[_Mapping[int, int]] = ..., DCGOEAEFEML: _Optional[_Iterable[int]] = ..., JFKKMFFPNGI: _Optional[_Iterable[int]] = ..., BMMEJPDMMCH: _Optional[_Mapping[int, int]] = ..., JJEAODIEJCL: _Optional[_Mapping[int, int]] = ...) -> None: ...
