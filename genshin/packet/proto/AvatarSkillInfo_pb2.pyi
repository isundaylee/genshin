from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarSkillInfo(_message.Message):
    __slots__ = ("pass_cd_time", "full_cd_time_list", "max_charge_count")
    PASS_CD_TIME_FIELD_NUMBER: _ClassVar[int]
    FULL_CD_TIME_LIST_FIELD_NUMBER: _ClassVar[int]
    MAX_CHARGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    pass_cd_time: int
    full_cd_time_list: _containers.RepeatedScalarFieldContainer[int]
    max_charge_count: int
    def __init__(self, pass_cd_time: _Optional[int] = ..., full_cd_time_list: _Optional[_Iterable[int]] = ..., max_charge_count: _Optional[int] = ...) -> None: ...
