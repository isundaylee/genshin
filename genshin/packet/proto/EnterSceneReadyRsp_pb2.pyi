from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EnterSceneReadyRsp(_message.Message):
    __slots__ = ("retcode", "enter_scene_token")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    ENTER_SCENE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    enter_scene_token: int
    def __init__(self, retcode: _Optional[int] = ..., enter_scene_token: _Optional[int] = ...) -> None: ...
