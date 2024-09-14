from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ChooseCurAvatarTeamReq(_message.Message):
    __slots__ = ("team_id",)
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    team_id: int
    def __init__(self, team_id: _Optional[int] = ...) -> None: ...
