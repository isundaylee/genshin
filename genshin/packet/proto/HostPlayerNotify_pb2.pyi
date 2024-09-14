from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HostPlayerNotify(_message.Message):
    __slots__ = ("host_uid", "host_peer_id")
    HOST_UID_FIELD_NUMBER: _ClassVar[int]
    HOST_PEER_ID_FIELD_NUMBER: _ClassVar[int]
    host_uid: int
    host_peer_id: int
    def __init__(self, host_uid: _Optional[int] = ..., host_peer_id: _Optional[int] = ...) -> None: ...
