from genshin.packet.proto import OnlinePlayerInfo_pb2 as _OnlinePlayerInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerApplyEnterHomeNotify(_message.Message):
    __slots__ = ("src_player_info", "src_app_id")
    SRC_PLAYER_INFO_FIELD_NUMBER: _ClassVar[int]
    SRC_APP_ID_FIELD_NUMBER: _ClassVar[int]
    src_player_info: _OnlinePlayerInfo_pb2.OnlinePlayerInfo
    src_app_id: int
    def __init__(self, src_player_info: _Optional[_Union[_OnlinePlayerInfo_pb2.OnlinePlayerInfo, _Mapping]] = ..., src_app_id: _Optional[int] = ...) -> None: ...
