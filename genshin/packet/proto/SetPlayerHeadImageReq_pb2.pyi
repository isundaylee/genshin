from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetPlayerHeadImageReq(_message.Message):
    __slots__ = ("head_image_id",)
    HEAD_IMAGE_ID_FIELD_NUMBER: _ClassVar[int]
    head_image_id: int
    def __init__(self, head_image_id: _Optional[int] = ...) -> None: ...
