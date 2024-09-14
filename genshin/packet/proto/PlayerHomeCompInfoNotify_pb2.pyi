from genshin.packet.proto import PlayerHomeCompInfo_pb2 as _PlayerHomeCompInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerHomeCompInfoNotify(_message.Message):
    __slots__ = ("comp_info",)
    COMP_INFO_FIELD_NUMBER: _ClassVar[int]
    comp_info: _PlayerHomeCompInfo_pb2.PlayerHomeCompInfo
    def __init__(self, comp_info: _Optional[_Union[_PlayerHomeCompInfo_pb2.PlayerHomeCompInfo, _Mapping]] = ...) -> None: ...
