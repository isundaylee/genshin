from genshin.packet.proto import KDEHCGJAGFJ_pb2 as _KDEHCGJAGFJ_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HOPFEEIPGJP(_message.Message):
    __slots__ = ("FGFLJIAEMLJ", "GJEBAJAJPII", "guid", "HLKDDNGCKJN")
    FGFLJIAEMLJ_FIELD_NUMBER: _ClassVar[int]
    GJEBAJAJPII_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    HLKDDNGCKJN_FIELD_NUMBER: _ClassVar[int]
    FGFLJIAEMLJ: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    GJEBAJAJPII: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    guid: int
    HLKDDNGCKJN: int
    def __init__(self, FGFLJIAEMLJ: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., GJEBAJAJPII: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., guid: _Optional[int] = ..., HLKDDNGCKJN: _Optional[int] = ...) -> None: ...