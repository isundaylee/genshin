from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class KCMBIPCNBDP(_message.Message):
    __slots__ = ("PAPPMADOEMA", "FINAHGLFHAG", "DNBEFLJLAMB")
    class PAPPMADOEMAEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    PAPPMADOEMA_FIELD_NUMBER: _ClassVar[int]
    FINAHGLFHAG_FIELD_NUMBER: _ClassVar[int]
    DNBEFLJLAMB_FIELD_NUMBER: _ClassVar[int]
    PAPPMADOEMA: _containers.ScalarMap[int, int]
    FINAHGLFHAG: int
    DNBEFLJLAMB: int
    def __init__(self, PAPPMADOEMA: _Optional[_Mapping[int, int]] = ..., FINAHGLFHAG: _Optional[int] = ..., DNBEFLJLAMB: _Optional[int] = ...) -> None: ...
