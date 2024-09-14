from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from genshin.packet.proto import HomeMarkPointNPCData_pb2 as _HomeMarkPointNPCData_pb2
from genshin.packet.proto import HomeMarkPointSuiteData_pb2 as _HomeMarkPointSuiteData_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomeMarkPointFurnitureData(_message.Message):
    __slots__ = ("guid", "furniture_id", "furniture_type", "pos", "npc_data", "suite_data")
    GUID_FIELD_NUMBER: _ClassVar[int]
    FURNITURE_ID_FIELD_NUMBER: _ClassVar[int]
    FURNITURE_TYPE_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    NPC_DATA_FIELD_NUMBER: _ClassVar[int]
    SUITE_DATA_FIELD_NUMBER: _ClassVar[int]
    guid: int
    furniture_id: int
    furniture_type: int
    pos: _Vector_pb2.Vector
    npc_data: _HomeMarkPointNPCData_pb2.HomeMarkPointNPCData
    suite_data: _HomeMarkPointSuiteData_pb2.HomeMarkPointSuiteData
    def __init__(self, guid: _Optional[int] = ..., furniture_id: _Optional[int] = ..., furniture_type: _Optional[int] = ..., pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., npc_data: _Optional[_Union[_HomeMarkPointNPCData_pb2.HomeMarkPointNPCData, _Mapping]] = ..., suite_data: _Optional[_Union[_HomeMarkPointSuiteData_pb2.HomeMarkPointSuiteData, _Mapping]] = ...) -> None: ...
