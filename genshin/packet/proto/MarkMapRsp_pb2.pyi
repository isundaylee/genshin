from genshin.packet.proto import MapMarkPoint_pb2 as _MapMarkPoint_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MarkMapRsp(_message.Message):
    __slots__ = ("mark_list", "retcode")
    MARK_LIST_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    mark_list: _containers.RepeatedCompositeFieldContainer[_MapMarkPoint_pb2.MapMarkPoint]
    retcode: int
    def __init__(self, mark_list: _Optional[_Iterable[_Union[_MapMarkPoint_pb2.MapMarkPoint, _Mapping]]] = ..., retcode: _Optional[int] = ...) -> None: ...
