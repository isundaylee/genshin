from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetSceneAreaReq(_message.Message):
    __slots__ = ("scene_id", "belong_uid")
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    BELONG_UID_FIELD_NUMBER: _ClassVar[int]
    scene_id: int
    belong_uid: int
    def __init__(self, scene_id: _Optional[int] = ..., belong_uid: _Optional[int] = ...) -> None: ...
