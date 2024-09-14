from genshin.packet.proto import DailyTaskInfo_pb2 as _DailyTaskInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WorldOwnerDailyTaskNotify(_message.Message):
    __slots__ = ("filter_city_id", "finished_daily_task_num", "task_list")
    FILTER_CITY_ID_FIELD_NUMBER: _ClassVar[int]
    FINISHED_DAILY_TASK_NUM_FIELD_NUMBER: _ClassVar[int]
    TASK_LIST_FIELD_NUMBER: _ClassVar[int]
    filter_city_id: int
    finished_daily_task_num: int
    task_list: _containers.RepeatedCompositeFieldContainer[_DailyTaskInfo_pb2.DailyTaskInfo]
    def __init__(self, filter_city_id: _Optional[int] = ..., finished_daily_task_num: _Optional[int] = ..., task_list: _Optional[_Iterable[_Union[_DailyTaskInfo_pb2.DailyTaskInfo, _Mapping]]] = ...) -> None: ...
