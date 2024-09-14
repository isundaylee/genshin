from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PSPlayerApplyEnterMpRsp(_message.Message):
    __slots__ = ("retcode", "target_psn_id", "param")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    TARGET_PSN_ID_FIELD_NUMBER: _ClassVar[int]
    PARAM_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    target_psn_id: str
    param: int
    def __init__(self, retcode: _Optional[int] = ..., target_psn_id: _Optional[str] = ..., param: _Optional[int] = ...) -> None: ...
