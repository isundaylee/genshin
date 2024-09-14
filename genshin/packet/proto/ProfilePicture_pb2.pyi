from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ProfilePicture(_message.Message):
    __slots__ = ("avatar_id", "costume_id", "head_image_id")
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    COSTUME_ID_FIELD_NUMBER: _ClassVar[int]
    HEAD_IMAGE_ID_FIELD_NUMBER: _ClassVar[int]
    avatar_id: int
    costume_id: int
    head_image_id: int
    def __init__(self, avatar_id: _Optional[int] = ..., costume_id: _Optional[int] = ..., head_image_id: _Optional[int] = ...) -> None: ...
