from genshin.packet.proto import LockedPersonallineData_pb2 as _LockedPersonallineData_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PersonalLineAllDataRsp(_message.Message):
    __slots__ = ("can_be_unlocked_personal_line_list", "retcode", "cur_finished_daily_task_count", "legendary_key_count", "ongoing_personal_line_list", "locked_personal_line_list")
    CAN_BE_UNLOCKED_PERSONAL_LINE_LIST_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    CUR_FINISHED_DAILY_TASK_COUNT_FIELD_NUMBER: _ClassVar[int]
    LEGENDARY_KEY_COUNT_FIELD_NUMBER: _ClassVar[int]
    ONGOING_PERSONAL_LINE_LIST_FIELD_NUMBER: _ClassVar[int]
    LOCKED_PERSONAL_LINE_LIST_FIELD_NUMBER: _ClassVar[int]
    can_be_unlocked_personal_line_list: _containers.RepeatedScalarFieldContainer[int]
    retcode: int
    cur_finished_daily_task_count: int
    legendary_key_count: int
    ongoing_personal_line_list: _containers.RepeatedScalarFieldContainer[int]
    locked_personal_line_list: _containers.RepeatedCompositeFieldContainer[_LockedPersonallineData_pb2.LockedPersonallineData]
    def __init__(self, can_be_unlocked_personal_line_list: _Optional[_Iterable[int]] = ..., retcode: _Optional[int] = ..., cur_finished_daily_task_count: _Optional[int] = ..., legendary_key_count: _Optional[int] = ..., ongoing_personal_line_list: _Optional[_Iterable[int]] = ..., locked_personal_line_list: _Optional[_Iterable[_Union[_LockedPersonallineData_pb2.LockedPersonallineData, _Mapping]]] = ...) -> None: ...
