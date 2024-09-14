from genshin.packet.proto import WidgetCreateLocationInfo_pb2 as _WidgetCreateLocationInfo_pb2
from genshin.packet.proto import WidgetCreatorInfo_pb2 as _WidgetCreatorInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WidgetDoBagReq(_message.Message):
    __slots__ = ("material_id", "location_info", "widget_creator_info")
    MATERIAL_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_INFO_FIELD_NUMBER: _ClassVar[int]
    WIDGET_CREATOR_INFO_FIELD_NUMBER: _ClassVar[int]
    material_id: int
    location_info: _WidgetCreateLocationInfo_pb2.WidgetCreateLocationInfo
    widget_creator_info: _WidgetCreatorInfo_pb2.WidgetCreatorInfo
    def __init__(self, material_id: _Optional[int] = ..., location_info: _Optional[_Union[_WidgetCreateLocationInfo_pb2.WidgetCreateLocationInfo, _Mapping]] = ..., widget_creator_info: _Optional[_Union[_WidgetCreatorInfo_pb2.WidgetCreatorInfo, _Mapping]] = ...) -> None: ...
