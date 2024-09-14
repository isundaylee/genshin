from genshin.packet.proto import LunchBoxData_pb2 as _LunchBoxData_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetUpLunchBoxWidgetReq(_message.Message):
    __slots__ = ("lunch_box_data",)
    LUNCH_BOX_DATA_FIELD_NUMBER: _ClassVar[int]
    lunch_box_data: _LunchBoxData_pb2.LunchBoxData
    def __init__(self, lunch_box_data: _Optional[_Union[_LunchBoxData_pb2.LunchBoxData, _Mapping]] = ...) -> None: ...
