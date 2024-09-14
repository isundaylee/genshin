from genshin.packet.proto import CityInfo_pb2 as _CityInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LevelupCityRsp(_message.Message):
    __slots__ = ("city_info", "scene_id", "retcode", "area_id")
    CITY_INFO_FIELD_NUMBER: _ClassVar[int]
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    AREA_ID_FIELD_NUMBER: _ClassVar[int]
    city_info: _CityInfo_pb2.CityInfo
    scene_id: int
    retcode: int
    area_id: int
    def __init__(self, city_info: _Optional[_Union[_CityInfo_pb2.CityInfo, _Mapping]] = ..., scene_id: _Optional[int] = ..., retcode: _Optional[int] = ..., area_id: _Optional[int] = ...) -> None: ...
