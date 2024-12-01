from genshin.packet.proto import KDEHCGJAGFJ_pb2 as _KDEHCGJAGFJ_pb2
from genshin.packet.proto import DAFPGOBFFLB_pb2 as _DAFPGOBFFLB_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LKIAMJCJLAK(_message.Message):
    __slots__ = ("GJEBAJAJPII", "BJLLGBAPJKP", "EFKNDDJEPLJ", "type")
    GJEBAJAJPII_FIELD_NUMBER: _ClassVar[int]
    BJLLGBAPJKP_FIELD_NUMBER: _ClassVar[int]
    EFKNDDJEPLJ_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    GJEBAJAJPII: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    BJLLGBAPJKP: int
    EFKNDDJEPLJ: int
    type: _DAFPGOBFFLB_pb2.DAFPGOBFFLB
    def __init__(self, GJEBAJAJPII: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., BJLLGBAPJKP: _Optional[int] = ..., EFKNDDJEPLJ: _Optional[int] = ..., type: _Optional[_Union[_DAFPGOBFFLB_pb2.DAFPGOBFFLB, str]] = ...) -> None: ...
