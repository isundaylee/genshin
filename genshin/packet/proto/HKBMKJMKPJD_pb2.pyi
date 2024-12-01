from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HKBMKJMKPJD(_message.Message):
    __slots__ = ("NGHJEEBKGEJ", "PIFMPAMGPAE", "MEJLFKPFPGK", "EJNINFFFKJP", "LLHJGGDNLFD", "AGHCICLCICK")
    class NGHJEEBKGEJEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class PIFMPAMGPAEEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    NGHJEEBKGEJ_FIELD_NUMBER: _ClassVar[int]
    PIFMPAMGPAE_FIELD_NUMBER: _ClassVar[int]
    MEJLFKPFPGK_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    LLHJGGDNLFD_FIELD_NUMBER: _ClassVar[int]
    AGHCICLCICK_FIELD_NUMBER: _ClassVar[int]
    NGHJEEBKGEJ: _containers.ScalarMap[int, int]
    PIFMPAMGPAE: _containers.ScalarMap[int, int]
    MEJLFKPFPGK: int
    EJNINFFFKJP: int
    LLHJGGDNLFD: int
    AGHCICLCICK: int
    def __init__(self, NGHJEEBKGEJ: _Optional[_Mapping[int, int]] = ..., PIFMPAMGPAE: _Optional[_Mapping[int, int]] = ..., MEJLFKPFPGK: _Optional[int] = ..., EJNINFFFKJP: _Optional[int] = ..., LLHJGGDNLFD: _Optional[int] = ..., AGHCICLCICK: _Optional[int] = ...) -> None: ...
