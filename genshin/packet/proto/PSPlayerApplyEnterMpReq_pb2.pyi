from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PSPlayerApplyEnterMpReq(_message.Message):
    __slots__ = ("target_psn_id",)
    TARGET_PSN_ID_FIELD_NUMBER: _ClassVar[int]
    target_psn_id: str
    def __init__(self, target_psn_id: _Optional[str] = ...) -> None: ...
