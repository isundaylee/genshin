from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MGAFPFOIMEJ(_message.Message):
    __slots__ = ("costume_id", "avatar_id", "NCCPPHNNPBF")
    COSTUME_ID_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    NCCPPHNNPBF_FIELD_NUMBER: _ClassVar[int]
    costume_id: int
    avatar_id: int
    NCCPPHNNPBF: int
    def __init__(self, costume_id: _Optional[int] = ..., avatar_id: _Optional[int] = ..., NCCPPHNNPBF: _Optional[int] = ...) -> None: ...
