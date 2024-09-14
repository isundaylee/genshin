from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from genshin.packet.proto import PathStatusType_pb2 as _PathStatusType_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ToTheMoonQueryPathRsp(_message.Message):
    __slots__ = ("level", "retcode", "corners", "query_status", "query_id", "index")
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    CORNERS_FIELD_NUMBER: _ClassVar[int]
    QUERY_STATUS_FIELD_NUMBER: _ClassVar[int]
    QUERY_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    level: _containers.RepeatedScalarFieldContainer[int]
    retcode: int
    corners: _containers.RepeatedCompositeFieldContainer[_Vector_pb2.Vector]
    query_status: _PathStatusType_pb2.PathStatusType
    query_id: int
    index: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, level: _Optional[_Iterable[int]] = ..., retcode: _Optional[int] = ..., corners: _Optional[_Iterable[_Union[_Vector_pb2.Vector, _Mapping]]] = ..., query_status: _Optional[_Union[_PathStatusType_pb2.PathStatusType, str]] = ..., query_id: _Optional[int] = ..., index: _Optional[_Iterable[int]] = ...) -> None: ...
