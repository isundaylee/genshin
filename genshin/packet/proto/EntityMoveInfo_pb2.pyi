from genshin.packet.proto import MotionInfo_pb2 as _MotionInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EntityMoveInfo(_message.Message):
    __slots__ = ("entity_id", "motion_info", "scene_time", "reliable_seq", "is_reliable")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    MOTION_INFO_FIELD_NUMBER: _ClassVar[int]
    SCENE_TIME_FIELD_NUMBER: _ClassVar[int]
    RELIABLE_SEQ_FIELD_NUMBER: _ClassVar[int]
    IS_RELIABLE_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    motion_info: _MotionInfo_pb2.MotionInfo
    scene_time: int
    reliable_seq: int
    is_reliable: bool
    def __init__(self, entity_id: _Optional[int] = ..., motion_info: _Optional[_Union[_MotionInfo_pb2.MotionInfo, _Mapping]] = ..., scene_time: _Optional[int] = ..., reliable_seq: _Optional[int] = ..., is_reliable: bool = ...) -> None: ...
