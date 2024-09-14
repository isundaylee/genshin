from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SceneInitFinishRsp(_message.Message):
    __slots__ = ("enter_scene_token", "retcode")
    ENTER_SCENE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    enter_scene_token: int
    retcode: int
    def __init__(self, enter_scene_token: _Optional[int] = ..., retcode: _Optional[int] = ...) -> None: ...
