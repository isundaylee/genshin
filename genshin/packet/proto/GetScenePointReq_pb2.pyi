from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetScenePointReq(_message.Message):
    __slots__ = ("is_new_player", "belong_uid", "scene_id")
    IS_NEW_PLAYER_FIELD_NUMBER: _ClassVar[int]
    BELONG_UID_FIELD_NUMBER: _ClassVar[int]
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    is_new_player: bool
    belong_uid: int
    scene_id: int
    def __init__(self, is_new_player: bool = ..., belong_uid: _Optional[int] = ..., scene_id: _Optional[int] = ...) -> None: ...
