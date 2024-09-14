from genshin.packet.proto import ScenePlayerInfo_pb2 as _ScenePlayerInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScenePlayerInfoNotify(_message.Message):
    __slots__ = ("player_info_list",)
    PLAYER_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    player_info_list: _containers.RepeatedCompositeFieldContainer[_ScenePlayerInfo_pb2.ScenePlayerInfo]
    def __init__(self, player_info_list: _Optional[_Iterable[_Union[_ScenePlayerInfo_pb2.ScenePlayerInfo, _Mapping]]] = ...) -> None: ...
