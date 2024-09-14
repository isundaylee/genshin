from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HomeChangeEditModeReq(_message.Message):
    __slots__ = ("is_enter_edit_mode",)
    IS_ENTER_EDIT_MODE_FIELD_NUMBER: _ClassVar[int]
    is_enter_edit_mode: bool
    def __init__(self, is_enter_edit_mode: bool = ...) -> None: ...
