from genshin.packet.proto import WidgetCreateLocationInfo_pb2 as _WidgetCreateLocationInfo_pb2
from genshin.packet.proto import WidgetCreatorOpType_pb2 as _WidgetCreatorOpType_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WidgetCreatorInfo(_message.Message):
    __slots__ = ("location_info", "entity_id", "op_type")
    LOCATION_INFO_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    OP_TYPE_FIELD_NUMBER: _ClassVar[int]
    location_info: _WidgetCreateLocationInfo_pb2.WidgetCreateLocationInfo
    entity_id: int
    op_type: _WidgetCreatorOpType_pb2.WidgetCreatorOpType
    def __init__(self, location_info: _Optional[_Union[_WidgetCreateLocationInfo_pb2.WidgetCreateLocationInfo, _Mapping]] = ..., entity_id: _Optional[int] = ..., op_type: _Optional[_Union[_WidgetCreatorOpType_pb2.WidgetCreatorOpType, str]] = ...) -> None: ...
