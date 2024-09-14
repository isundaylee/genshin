from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TakeInvestigationRewardRsp(_message.Message):
    __slots__ = ("retcode", "id")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    id: int
    def __init__(self, retcode: _Optional[int] = ..., id: _Optional[int] = ...) -> None: ...
