from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerCookReq(_message.Message):
    __slots__ = ("qte_quality", "cook_count", "recipe_id", "assist_avatar")
    QTE_QUALITY_FIELD_NUMBER: _ClassVar[int]
    COOK_COUNT_FIELD_NUMBER: _ClassVar[int]
    RECIPE_ID_FIELD_NUMBER: _ClassVar[int]
    ASSIST_AVATAR_FIELD_NUMBER: _ClassVar[int]
    qte_quality: int
    cook_count: int
    recipe_id: int
    assist_avatar: int
    def __init__(self, qte_quality: _Optional[int] = ..., cook_count: _Optional[int] = ..., recipe_id: _Optional[int] = ..., assist_avatar: _Optional[int] = ...) -> None: ...
