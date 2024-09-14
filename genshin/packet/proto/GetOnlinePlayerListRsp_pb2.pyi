from genshin.packet.proto import OnlinePlayerInfo_pb2 as _OnlinePlayerInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetOnlinePlayerListRsp(_message.Message):
    __slots__ = ("param", "player_info_list", "retcode")
    PARAM_FIELD_NUMBER: _ClassVar[int]
    PLAYER_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    param: int
    player_info_list: _containers.RepeatedCompositeFieldContainer[_OnlinePlayerInfo_pb2.OnlinePlayerInfo]
    retcode: int
    def __init__(self, param: _Optional[int] = ..., player_info_list: _Optional[_Iterable[_Union[_OnlinePlayerInfo_pb2.OnlinePlayerInfo, _Mapping]]] = ..., retcode: _Optional[int] = ...) -> None: ...
