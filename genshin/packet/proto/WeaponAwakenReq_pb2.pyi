from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WeaponAwakenReq(_message.Message):
    __slots__ = ("target_weapon_guid", "NEHLGIOLBJA", "HICOIODAHGK")
    TARGET_WEAPON_GUID_FIELD_NUMBER: _ClassVar[int]
    NEHLGIOLBJA_FIELD_NUMBER: _ClassVar[int]
    HICOIODAHGK_FIELD_NUMBER: _ClassVar[int]
    target_weapon_guid: int
    NEHLGIOLBJA: int
    HICOIODAHGK: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, target_weapon_guid: _Optional[int] = ..., NEHLGIOLBJA: _Optional[int] = ..., HICOIODAHGK: _Optional[_Iterable[int]] = ...) -> None: ...
