from genshin.packet.proto import PlayerWidgetInfo_pb2 as _PlayerWidgetInfo_pb2
from genshin.packet.proto import OnlinePlayerInfo_pb2 as _OnlinePlayerInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WorldPlayerInfoNotify(_message.Message):
    __slots__ = ("player_uid_list", "player_widget_info_list", "player_info_list")
    PLAYER_UID_LIST_FIELD_NUMBER: _ClassVar[int]
    PLAYER_WIDGET_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    PLAYER_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    player_uid_list: _containers.RepeatedScalarFieldContainer[int]
    player_widget_info_list: _containers.RepeatedCompositeFieldContainer[_PlayerWidgetInfo_pb2.PlayerWidgetInfo]
    player_info_list: _containers.RepeatedCompositeFieldContainer[_OnlinePlayerInfo_pb2.OnlinePlayerInfo]
    def __init__(self, player_uid_list: _Optional[_Iterable[int]] = ..., player_widget_info_list: _Optional[_Iterable[_Union[_PlayerWidgetInfo_pb2.PlayerWidgetInfo, _Mapping]]] = ..., player_info_list: _Optional[_Iterable[_Union[_OnlinePlayerInfo_pb2.OnlinePlayerInfo, _Mapping]]] = ...) -> None: ...
