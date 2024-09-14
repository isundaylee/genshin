from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerCookArgsReq(_message.Message):
    __slots__ = ("recipe_id", "assist_avatar")
    RECIPE_ID_FIELD_NUMBER: _ClassVar[int]
    ASSIST_AVATAR_FIELD_NUMBER: _ClassVar[int]
    recipe_id: int
    assist_avatar: int
    def __init__(self, recipe_id: _Optional[int] = ..., assist_avatar: _Optional[int] = ...) -> None: ...
