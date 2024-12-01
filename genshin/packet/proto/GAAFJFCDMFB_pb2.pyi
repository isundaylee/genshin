from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GAAFJFCDMFB(_message.Message):
    __slots__ = ("PNGLGNLNBNM", "NKHOOCJMIGN", "JOFKNLDPGCH", "MDANMNCEIGO", "KAMDFFPLFAJ")
    class PNGLGNLNBNMEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    PNGLGNLNBNM_FIELD_NUMBER: _ClassVar[int]
    NKHOOCJMIGN_FIELD_NUMBER: _ClassVar[int]
    JOFKNLDPGCH_FIELD_NUMBER: _ClassVar[int]
    MDANMNCEIGO_FIELD_NUMBER: _ClassVar[int]
    KAMDFFPLFAJ_FIELD_NUMBER: _ClassVar[int]
    PNGLGNLNBNM: _containers.ScalarMap[int, str]
    NKHOOCJMIGN: float
    JOFKNLDPGCH: int
    MDANMNCEIGO: int
    KAMDFFPLFAJ: int
    def __init__(self, PNGLGNLNBNM: _Optional[_Mapping[int, str]] = ..., NKHOOCJMIGN: _Optional[float] = ..., JOFKNLDPGCH: _Optional[int] = ..., MDANMNCEIGO: _Optional[int] = ..., KAMDFFPLFAJ: _Optional[int] = ...) -> None: ...
