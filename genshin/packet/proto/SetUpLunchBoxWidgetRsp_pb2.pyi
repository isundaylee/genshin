from genshin.packet.proto import LunchBoxData_pb2 as _LunchBoxData_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetUpLunchBoxWidgetRsp(_message.Message):
    __slots__ = ("retcode", "lunch_box_data")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    LUNCH_BOX_DATA_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    lunch_box_data: _LunchBoxData_pb2.LunchBoxData
    def __init__(self, retcode: _Optional[int] = ..., lunch_box_data: _Optional[_Union[_LunchBoxData_pb2.LunchBoxData, _Mapping]] = ...) -> None: ...
