from genshin.packet.proto import CityInfo_pb2 as _CityInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetSceneAreaRsp(_message.Message):
    __slots__ = ("scene_id", "city_info_list", "retcode", "area_id_list")
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    CITY_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    AREA_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    scene_id: int
    city_info_list: _containers.RepeatedCompositeFieldContainer[_CityInfo_pb2.CityInfo]
    retcode: int
    area_id_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, scene_id: _Optional[int] = ..., city_info_list: _Optional[_Iterable[_Union[_CityInfo_pb2.CityInfo, _Mapping]]] = ..., retcode: _Optional[int] = ..., area_id_list: _Optional[_Iterable[int]] = ...) -> None: ...
