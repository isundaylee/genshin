from genshin.packet.proto import WidgetCreateLocationInfo_pb2 as _WidgetCreateLocationInfo_pb2
from genshin.packet.proto import WidgetCameraInfo_pb2 as _WidgetCameraInfo_pb2
from genshin.packet.proto import WidgetCreatorInfo_pb2 as _WidgetCreatorInfo_pb2
from genshin.packet.proto import WidgetThunderBirdFeatherInfo_pb2 as _WidgetThunderBirdFeatherInfo_pb2
from genshin.packet.proto import WidgetSorushInfo_pb2 as _WidgetSorushInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QuickUseWidgetReq(_message.Message):
    __slots__ = ("location_info", "camera_info", "creator_info", "thunder_bird_feather_info", "sorush_info", "EEJNPDEBBIK")
    LOCATION_INFO_FIELD_NUMBER: _ClassVar[int]
    CAMERA_INFO_FIELD_NUMBER: _ClassVar[int]
    CREATOR_INFO_FIELD_NUMBER: _ClassVar[int]
    THUNDER_BIRD_FEATHER_INFO_FIELD_NUMBER: _ClassVar[int]
    SORUSH_INFO_FIELD_NUMBER: _ClassVar[int]
    EEJNPDEBBIK_FIELD_NUMBER: _ClassVar[int]
    location_info: _WidgetCreateLocationInfo_pb2.WidgetCreateLocationInfo
    camera_info: _WidgetCameraInfo_pb2.WidgetCameraInfo
    creator_info: _WidgetCreatorInfo_pb2.WidgetCreatorInfo
    thunder_bird_feather_info: _WidgetThunderBirdFeatherInfo_pb2.WidgetThunderBirdFeatherInfo
    sorush_info: _WidgetSorushInfo_pb2.WidgetSorushInfo
    EEJNPDEBBIK: bool
    def __init__(self, location_info: _Optional[_Union[_WidgetCreateLocationInfo_pb2.WidgetCreateLocationInfo, _Mapping]] = ..., camera_info: _Optional[_Union[_WidgetCameraInfo_pb2.WidgetCameraInfo, _Mapping]] = ..., creator_info: _Optional[_Union[_WidgetCreatorInfo_pb2.WidgetCreatorInfo, _Mapping]] = ..., thunder_bird_feather_info: _Optional[_Union[_WidgetThunderBirdFeatherInfo_pb2.WidgetThunderBirdFeatherInfo, _Mapping]] = ..., sorush_info: _Optional[_Union[_WidgetSorushInfo_pb2.WidgetSorushInfo, _Mapping]] = ..., EEJNPDEBBIK: bool = ...) -> None: ...
