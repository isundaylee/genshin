from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EnterScenePeerNotify(_message.Message):
    __slots__ = ("enter_scene_token", "dest_scene_id", "peer_id", "host_peer_id")
    ENTER_SCENE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    DEST_SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    PEER_ID_FIELD_NUMBER: _ClassVar[int]
    HOST_PEER_ID_FIELD_NUMBER: _ClassVar[int]
    enter_scene_token: int
    dest_scene_id: int
    peer_id: int
    host_peer_id: int
    def __init__(self, enter_scene_token: _Optional[int] = ..., dest_scene_id: _Optional[int] = ..., peer_id: _Optional[int] = ..., host_peer_id: _Optional[int] = ...) -> None: ...
