from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DelBackupAvatarTeamRsp(_message.Message):
    __slots__ = ("retcode", "backup_avatar_team_id")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_AVATAR_TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    backup_avatar_team_id: int
    def __init__(self, retcode: _Optional[int] = ..., backup_avatar_team_id: _Optional[int] = ...) -> None: ...
