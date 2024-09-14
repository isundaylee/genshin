from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from genshin.packet.proto import PathStatusType_pb2 as _PathStatusType_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryPathRsp(_message.Message):
    __slots__ = ("corners", "query_id", "retcode", "query_status")
    CORNERS_FIELD_NUMBER: _ClassVar[int]
    QUERY_ID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    QUERY_STATUS_FIELD_NUMBER: _ClassVar[int]
    corners: _containers.RepeatedCompositeFieldContainer[_Vector_pb2.Vector]
    query_id: int
    retcode: int
    query_status: _PathStatusType_pb2.PathStatusType
    def __init__(self, corners: _Optional[_Iterable[_Union[_Vector_pb2.Vector, _Mapping]]] = ..., query_id: _Optional[int] = ..., retcode: _Optional[int] = ..., query_status: _Optional[_Union[_PathStatusType_pb2.PathStatusType, str]] = ...) -> None: ...
