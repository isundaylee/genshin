from genshin.packet.proto import MapMarkPoint_pb2 as _MapMarkPoint_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MarkMapReq(_message.Message):
    __slots__ = ("mark", "old", "op")
    class Operation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPERATION_ADD: _ClassVar[MarkMapReq.Operation]
        OPERATION_MOD: _ClassVar[MarkMapReq.Operation]
        OPERATION_DEL: _ClassVar[MarkMapReq.Operation]
        OPERATION_GET: _ClassVar[MarkMapReq.Operation]
    OPERATION_ADD: MarkMapReq.Operation
    OPERATION_MOD: MarkMapReq.Operation
    OPERATION_DEL: MarkMapReq.Operation
    OPERATION_GET: MarkMapReq.Operation
    MARK_FIELD_NUMBER: _ClassVar[int]
    OLD_FIELD_NUMBER: _ClassVar[int]
    OP_FIELD_NUMBER: _ClassVar[int]
    mark: _MapMarkPoint_pb2.MapMarkPoint
    old: _MapMarkPoint_pb2.MapMarkPoint
    op: MarkMapReq.Operation
    def __init__(self, mark: _Optional[_Union[_MapMarkPoint_pb2.MapMarkPoint, _Mapping]] = ..., old: _Optional[_Union[_MapMarkPoint_pb2.MapMarkPoint, _Mapping]] = ..., op: _Optional[_Union[MarkMapReq.Operation, str]] = ...) -> None: ...
