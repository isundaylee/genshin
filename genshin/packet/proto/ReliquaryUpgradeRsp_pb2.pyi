from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ReliquaryUpgradeRsp(_message.Message):
    __slots__ = ("target_reliquary_guid", "retcode", "power_up_rate", "cur_level", "old_level", "cur_append_prop_list", "old_append_prop_list")
    TARGET_RELIQUARY_GUID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    POWER_UP_RATE_FIELD_NUMBER: _ClassVar[int]
    CUR_LEVEL_FIELD_NUMBER: _ClassVar[int]
    OLD_LEVEL_FIELD_NUMBER: _ClassVar[int]
    CUR_APPEND_PROP_LIST_FIELD_NUMBER: _ClassVar[int]
    OLD_APPEND_PROP_LIST_FIELD_NUMBER: _ClassVar[int]
    target_reliquary_guid: int
    retcode: int
    power_up_rate: int
    cur_level: int
    old_level: int
    cur_append_prop_list: _containers.RepeatedScalarFieldContainer[int]
    old_append_prop_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, target_reliquary_guid: _Optional[int] = ..., retcode: _Optional[int] = ..., power_up_rate: _Optional[int] = ..., cur_level: _Optional[int] = ..., old_level: _Optional[int] = ..., cur_append_prop_list: _Optional[_Iterable[int]] = ..., old_append_prop_list: _Optional[_Iterable[int]] = ...) -> None: ...
