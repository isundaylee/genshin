from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ChangeTeamNameRsp(_message.Message):
    __slots__ = ("team_id", "retcode", "team_name")
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    TEAM_NAME_FIELD_NUMBER: _ClassVar[int]
    team_id: int
    retcode: int
    team_name: str
    def __init__(self, team_id: _Optional[int] = ..., retcode: _Optional[int] = ..., team_name: _Optional[str] = ...) -> None: ...
