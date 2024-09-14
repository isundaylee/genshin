from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ChooseCurAvatarTeamRsp(_message.Message):
    __slots__ = ("cur_team_id", "retcode")
    CUR_TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    cur_team_id: int
    retcode: int
    def __init__(self, cur_team_id: _Optional[int] = ..., retcode: _Optional[int] = ...) -> None: ...
