from genshin.packet.proto import OnlinePlayerInfo_pb2 as _OnlinePlayerInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerApplyEnterMpNotify(_message.Message):
    __slots__ = ("src_app_id", "src_thread_index", "src_player_info")
    SRC_APP_ID_FIELD_NUMBER: _ClassVar[int]
    SRC_THREAD_INDEX_FIELD_NUMBER: _ClassVar[int]
    SRC_PLAYER_INFO_FIELD_NUMBER: _ClassVar[int]
    src_app_id: int
    src_thread_index: int
    src_player_info: _OnlinePlayerInfo_pb2.OnlinePlayerInfo
    def __init__(self, src_app_id: _Optional[int] = ..., src_thread_index: _Optional[int] = ..., src_player_info: _Optional[_Union[_OnlinePlayerInfo_pb2.OnlinePlayerInfo, _Mapping]] = ...) -> None: ...
