from genshin.packet.proto import RoutePoint_pb2 as _RoutePoint_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Route(_message.Message):
    __slots__ = ("route_points", "route_type")
    ROUTE_POINTS_FIELD_NUMBER: _ClassVar[int]
    ROUTE_TYPE_FIELD_NUMBER: _ClassVar[int]
    route_points: _containers.RepeatedCompositeFieldContainer[_RoutePoint_pb2.RoutePoint]
    route_type: int
    def __init__(self, route_points: _Optional[_Iterable[_Union[_RoutePoint_pb2.RoutePoint, _Mapping]]] = ..., route_type: _Optional[int] = ...) -> None: ...
