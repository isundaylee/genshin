from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CookRecipeData(_message.Message):
    __slots__ = ("recipe_id", "proficiency")
    RECIPE_ID_FIELD_NUMBER: _ClassVar[int]
    PROFICIENCY_FIELD_NUMBER: _ClassVar[int]
    recipe_id: int
    proficiency: int
    def __init__(self, recipe_id: _Optional[int] = ..., proficiency: _Optional[int] = ...) -> None: ...
