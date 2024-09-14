from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HomeSaveArrangementNoChangeReq(_message.Message):
    __slots__ = ("scene_id",)
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    scene_id: int
    def __init__(self, scene_id: _Optional[int] = ...) -> None: ...
