from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PPDGNKECFKM(_message.Message):
    __slots__ = ("NPDFBDOGHPO", "IGFHLKHKGAI", "IFGGHINCLPA", "EDFGADDMMJD", "EOJICCEHGAL", "OBKMDJGFBFA", "GJLFOGBBHPD", "EBHEDMCBBPO", "MCGLLLFCJOB", "EJNINFFFKJP")
    class IGFHLKHKGAIEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    NPDFBDOGHPO_FIELD_NUMBER: _ClassVar[int]
    IGFHLKHKGAI_FIELD_NUMBER: _ClassVar[int]
    IFGGHINCLPA_FIELD_NUMBER: _ClassVar[int]
    EDFGADDMMJD_FIELD_NUMBER: _ClassVar[int]
    EOJICCEHGAL_FIELD_NUMBER: _ClassVar[int]
    OBKMDJGFBFA_FIELD_NUMBER: _ClassVar[int]
    GJLFOGBBHPD_FIELD_NUMBER: _ClassVar[int]
    EBHEDMCBBPO_FIELD_NUMBER: _ClassVar[int]
    MCGLLLFCJOB_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    NPDFBDOGHPO: _containers.RepeatedScalarFieldContainer[int]
    IGFHLKHKGAI: _containers.ScalarMap[int, int]
    IFGGHINCLPA: _containers.RepeatedScalarFieldContainer[int]
    EDFGADDMMJD: _containers.RepeatedScalarFieldContainer[int]
    EOJICCEHGAL: int
    OBKMDJGFBFA: int
    GJLFOGBBHPD: int
    EBHEDMCBBPO: int
    MCGLLLFCJOB: int
    EJNINFFFKJP: int
    def __init__(self, NPDFBDOGHPO: _Optional[_Iterable[int]] = ..., IGFHLKHKGAI: _Optional[_Mapping[int, int]] = ..., IFGGHINCLPA: _Optional[_Iterable[int]] = ..., EDFGADDMMJD: _Optional[_Iterable[int]] = ..., EOJICCEHGAL: _Optional[int] = ..., OBKMDJGFBFA: _Optional[int] = ..., GJLFOGBBHPD: _Optional[int] = ..., EBHEDMCBBPO: _Optional[int] = ..., MCGLLLFCJOB: _Optional[int] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
