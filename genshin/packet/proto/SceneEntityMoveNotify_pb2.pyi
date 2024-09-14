from genshin.packet.proto import MotionInfo_pb2 as _MotionInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SceneEntityMoveNotify(_message.Message):
    __slots__ = ("motion_info", "entity_id", "reliable_seq", "scene_time")
    MOTION_INFO_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    RELIABLE_SEQ_FIELD_NUMBER: _ClassVar[int]
    SCENE_TIME_FIELD_NUMBER: _ClassVar[int]
    motion_info: _MotionInfo_pb2.MotionInfo
    entity_id: int
    reliable_seq: int
    scene_time: int
    def __init__(self, motion_info: _Optional[_Union[_MotionInfo_pb2.MotionInfo, _Mapping]] = ..., entity_id: _Optional[int] = ..., reliable_seq: _Optional[int] = ..., scene_time: _Optional[int] = ...) -> None: ...
