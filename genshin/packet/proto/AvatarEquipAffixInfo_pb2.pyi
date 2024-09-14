from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarEquipAffixInfo(_message.Message):
    __slots__ = ("equip_affix_id", "left_cd_time")
    EQUIP_AFFIX_ID_FIELD_NUMBER: _ClassVar[int]
    LEFT_CD_TIME_FIELD_NUMBER: _ClassVar[int]
    equip_affix_id: int
    left_cd_time: int
    def __init__(self, equip_affix_id: _Optional[int] = ..., left_cd_time: _Optional[int] = ...) -> None: ...
