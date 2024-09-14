from genshin.packet.proto import PlayerDieOption_pb2 as _PlayerDieOption_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonDieOptionReq(_message.Message):
    __slots__ = ("is_quit_immediately", "die_option")
    IS_QUIT_IMMEDIATELY_FIELD_NUMBER: _ClassVar[int]
    DIE_OPTION_FIELD_NUMBER: _ClassVar[int]
    is_quit_immediately: bool
    die_option: _PlayerDieOption_pb2.PlayerDieOption
    def __init__(self, is_quit_immediately: bool = ..., die_option: _Optional[_Union[_PlayerDieOption_pb2.PlayerDieOption, str]] = ...) -> None: ...
