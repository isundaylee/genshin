from genshin.packet.proto import CountDownDelete_pb2 as _CountDownDelete_pb2
from genshin.packet.proto import DateTimeDelete_pb2 as _DateTimeDelete_pb2
from genshin.packet.proto import DelayWeekCountDownDelete_pb2 as _DelayWeekCountDownDelete_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MaterialDeleteInfo(_message.Message):
    __slots__ = ("delete_time_num_map", "count_down_delete", "date_delete", "delay_week_count_down_delete")
    DELETE_TIME_NUM_MAP_FIELD_NUMBER: _ClassVar[int]
    COUNT_DOWN_DELETE_FIELD_NUMBER: _ClassVar[int]
    DATE_DELETE_FIELD_NUMBER: _ClassVar[int]
    DELAY_WEEK_COUNT_DOWN_DELETE_FIELD_NUMBER: _ClassVar[int]
    delete_time_num_map: bool
    count_down_delete: _CountDownDelete_pb2.CountDownDelete
    date_delete: _DateTimeDelete_pb2.DateTimeDelete
    delay_week_count_down_delete: _DelayWeekCountDownDelete_pb2.DelayWeekCountDownDelete
    def __init__(self, delete_time_num_map: bool = ..., count_down_delete: _Optional[_Union[_CountDownDelete_pb2.CountDownDelete, _Mapping]] = ..., date_delete: _Optional[_Union[_DateTimeDelete_pb2.DateTimeDelete, _Mapping]] = ..., delay_week_count_down_delete: _Optional[_Union[_DelayWeekCountDownDelete_pb2.DelayWeekCountDownDelete, _Mapping]] = ...) -> None: ...
