from genshin.packet.proto import FoundationStatus_pb2 as _FoundationStatus_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FoundationInfo(_message.Message):
    __slots__ = ("status", "uid_list", "current_building_id", "locked_by_uid")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UID_LIST_FIELD_NUMBER: _ClassVar[int]
    CURRENT_BUILDING_ID_FIELD_NUMBER: _ClassVar[int]
    LOCKED_BY_UID_FIELD_NUMBER: _ClassVar[int]
    status: _FoundationStatus_pb2.FoundationStatus
    uid_list: _containers.RepeatedScalarFieldContainer[int]
    current_building_id: int
    locked_by_uid: int
    def __init__(self, status: _Optional[_Union[_FoundationStatus_pb2.FoundationStatus, str]] = ..., uid_list: _Optional[_Iterable[int]] = ..., current_building_id: _Optional[int] = ..., locked_by_uid: _Optional[int] = ...) -> None: ...
