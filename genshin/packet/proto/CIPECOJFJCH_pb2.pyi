from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CIPECOJFJCH(_message.Message):
    __slots__ = ("HBKGBNKKCBG", "NCCPPHNNPBF", "DNBEFLJLAMB")
    class HBKGBNKKCBGEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    HBKGBNKKCBG_FIELD_NUMBER: _ClassVar[int]
    NCCPPHNNPBF_FIELD_NUMBER: _ClassVar[int]
    DNBEFLJLAMB_FIELD_NUMBER: _ClassVar[int]
    HBKGBNKKCBG: _containers.ScalarMap[int, int]
    NCCPPHNNPBF: int
    DNBEFLJLAMB: int
    def __init__(self, HBKGBNKKCBG: _Optional[_Mapping[int, int]] = ..., NCCPPHNNPBF: _Optional[int] = ..., DNBEFLJLAMB: _Optional[int] = ...) -> None: ...
