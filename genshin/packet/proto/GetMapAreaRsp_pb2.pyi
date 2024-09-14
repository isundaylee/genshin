from genshin.packet.proto import MapAreaInfo_pb2 as _MapAreaInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetMapAreaRsp(_message.Message):
    __slots__ = ("retcode", "map_area_info_list")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    MAP_AREA_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    map_area_info_list: _containers.RepeatedCompositeFieldContainer[_MapAreaInfo_pb2.MapAreaInfo]
    def __init__(self, retcode: _Optional[int] = ..., map_area_info_list: _Optional[_Iterable[_Union[_MapAreaInfo_pb2.MapAreaInfo, _Mapping]]] = ...) -> None: ...
