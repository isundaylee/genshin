from genshin.packet.proto import OnlinePlayerInfo_pb2 as _OnlinePlayerInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScenePlayerInfo(_message.Message):
    __slots__ = ("online_player_info", "is_connected", "scene_id", "name", "peer_id", "uid")
    ONLINE_PLAYER_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PEER_ID_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    online_player_info: _OnlinePlayerInfo_pb2.OnlinePlayerInfo
    is_connected: bool
    scene_id: int
    name: str
    peer_id: int
    uid: int
    def __init__(self, online_player_info: _Optional[_Union[_OnlinePlayerInfo_pb2.OnlinePlayerInfo, _Mapping]] = ..., is_connected: bool = ..., scene_id: _Optional[int] = ..., name: _Optional[str] = ..., peer_id: _Optional[int] = ..., uid: _Optional[int] = ...) -> None: ...
