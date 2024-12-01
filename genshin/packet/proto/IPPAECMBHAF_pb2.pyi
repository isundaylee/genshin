from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class IPPAECMBHAF(_message.Message):
    __slots__ = ("online_id", "xbox_user_id", "target_uid", "psn_id", "JFBLHMGJIBH")
    ONLINE_ID_FIELD_NUMBER: _ClassVar[int]
    XBOX_USER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_UID_FIELD_NUMBER: _ClassVar[int]
    PSN_ID_FIELD_NUMBER: _ClassVar[int]
    JFBLHMGJIBH_FIELD_NUMBER: _ClassVar[int]
    online_id: str
    xbox_user_id: str
    target_uid: int
    psn_id: str
    JFBLHMGJIBH: bool
    def __init__(self, online_id: _Optional[str] = ..., xbox_user_id: _Optional[str] = ..., target_uid: _Optional[int] = ..., psn_id: _Optional[str] = ..., JFBLHMGJIBH: bool = ...) -> None: ...
