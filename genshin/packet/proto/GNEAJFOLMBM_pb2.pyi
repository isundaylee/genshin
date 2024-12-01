from genshin.packet.proto import KHBDLLKPLFG_pb2 as _KHBDLLKPLFG_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GNEAJFOLMBM(_message.Message):
    __slots__ = ("avatar_type", "MONEJDBPOLB", "MEJLFKPFPGK")
    AVATAR_TYPE_FIELD_NUMBER: _ClassVar[int]
    MONEJDBPOLB_FIELD_NUMBER: _ClassVar[int]
    MEJLFKPFPGK_FIELD_NUMBER: _ClassVar[int]
    avatar_type: _KHBDLLKPLFG_pb2.KHBDLLKPLFG
    MONEJDBPOLB: int
    MEJLFKPFPGK: int
    def __init__(self, avatar_type: _Optional[_Union[_KHBDLLKPLFG_pb2.KHBDLLKPLFG, str]] = ..., MONEJDBPOLB: _Optional[int] = ..., MEJLFKPFPGK: _Optional[int] = ...) -> None: ...
