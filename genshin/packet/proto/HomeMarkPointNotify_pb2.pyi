from genshin.packet.proto import HomeMarkPointSceneData_pb2 as _HomeMarkPointSceneData_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomeMarkPointNotify(_message.Message):
    __slots__ = ("mark_point_data_list",)
    MARK_POINT_DATA_LIST_FIELD_NUMBER: _ClassVar[int]
    mark_point_data_list: _containers.RepeatedCompositeFieldContainer[_HomeMarkPointSceneData_pb2.HomeMarkPointSceneData]
    def __init__(self, mark_point_data_list: _Optional[_Iterable[_Union[_HomeMarkPointSceneData_pb2.HomeMarkPointSceneData, _Mapping]]] = ...) -> None: ...
