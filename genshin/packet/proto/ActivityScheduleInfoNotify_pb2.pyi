from genshin.packet.proto import ActivityScheduleInfo_pb2 as _ActivityScheduleInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActivityScheduleInfoNotify(_message.Message):
    __slots__ = ("remain_fly_sea_lamp_num", "activity_schedule_list")
    REMAIN_FLY_SEA_LAMP_NUM_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_SCHEDULE_LIST_FIELD_NUMBER: _ClassVar[int]
    remain_fly_sea_lamp_num: int
    activity_schedule_list: _containers.RepeatedCompositeFieldContainer[_ActivityScheduleInfo_pb2.ActivityScheduleInfo]
    def __init__(self, remain_fly_sea_lamp_num: _Optional[int] = ..., activity_schedule_list: _Optional[_Iterable[_Union[_ActivityScheduleInfo_pb2.ActivityScheduleInfo, _Mapping]]] = ...) -> None: ...
