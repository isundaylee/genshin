from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HomeSceneJumpRsp(_message.Message):
    __slots__ = ("is_enter_room_scene", "retcode")
    IS_ENTER_ROOM_SCENE_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    is_enter_room_scene: bool
    retcode: int
    def __init__(self, is_enter_room_scene: bool = ..., retcode: _Optional[int] = ...) -> None: ...
