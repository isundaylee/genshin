from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class OHAPJPKEFKJ(_message.Message):
    __slots__ = ("mist_trial_avatar_id", "formal_avatar_guid")
    MIST_TRIAL_AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    FORMAL_AVATAR_GUID_FIELD_NUMBER: _ClassVar[int]
    mist_trial_avatar_id: int
    formal_avatar_guid: int
    def __init__(self, mist_trial_avatar_id: _Optional[int] = ..., formal_avatar_guid: _Optional[int] = ...) -> None: ...
