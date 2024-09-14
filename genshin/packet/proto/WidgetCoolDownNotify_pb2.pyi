from genshin.packet.proto import WidgetCoolDownData_pb2 as _WidgetCoolDownData_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WidgetCoolDownNotify(_message.Message):
    __slots__ = ("group_cool_down_data_list", "normal_cool_down_data_list")
    GROUP_COOL_DOWN_DATA_LIST_FIELD_NUMBER: _ClassVar[int]
    NORMAL_COOL_DOWN_DATA_LIST_FIELD_NUMBER: _ClassVar[int]
    group_cool_down_data_list: _containers.RepeatedCompositeFieldContainer[_WidgetCoolDownData_pb2.WidgetCoolDownData]
    normal_cool_down_data_list: _containers.RepeatedCompositeFieldContainer[_WidgetCoolDownData_pb2.WidgetCoolDownData]
    def __init__(self, group_cool_down_data_list: _Optional[_Iterable[_Union[_WidgetCoolDownData_pb2.WidgetCoolDownData, _Mapping]]] = ..., normal_cool_down_data_list: _Optional[_Iterable[_Union[_WidgetCoolDownData_pb2.WidgetCoolDownData, _Mapping]]] = ...) -> None: ...
