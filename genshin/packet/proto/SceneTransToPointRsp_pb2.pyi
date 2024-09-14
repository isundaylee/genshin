from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SceneTransToPointRsp(_message.Message):
    __slots__ = ("scene_id", "retcode", "point_id")
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    POINT_ID_FIELD_NUMBER: _ClassVar[int]
    scene_id: int
    retcode: int
    point_id: int
    def __init__(self, scene_id: _Optional[int] = ..., retcode: _Optional[int] = ..., point_id: _Optional[int] = ...) -> None: ...
