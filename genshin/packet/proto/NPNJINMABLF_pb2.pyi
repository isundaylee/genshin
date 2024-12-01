from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NPNJINMABLF(_message.Message):
    __slots__ = ("EEMKOELPGBA", "rent_avatar_id", "avatar_id", "trial_config_id")
    EEMKOELPGBA_FIELD_NUMBER: _ClassVar[int]
    RENT_AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    TRIAL_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    EEMKOELPGBA: bool
    rent_avatar_id: int
    avatar_id: int
    trial_config_id: int
    def __init__(self, EEMKOELPGBA: bool = ..., rent_avatar_id: _Optional[int] = ..., avatar_id: _Optional[int] = ..., trial_config_id: _Optional[int] = ...) -> None: ...
