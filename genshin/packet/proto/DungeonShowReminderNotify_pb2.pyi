from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonShowReminderNotify(_message.Message):
    __slots__ = ("reminder_id",)
    REMINDER_ID_FIELD_NUMBER: _ClassVar[int]
    reminder_id: int
    def __init__(self, reminder_id: _Optional[int] = ...) -> None: ...
