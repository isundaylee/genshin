from genshin.packet.proto import KDEHCGJAGFJ_pb2 as _KDEHCGJAGFJ_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PKGOCLIMOIG(_message.Message):
    __slots__ = ("GJEBAJAJPII", "FGFLJIAEMLJ", "FMOIOMLDAJK", "guid")
    GJEBAJAJPII_FIELD_NUMBER: _ClassVar[int]
    FGFLJIAEMLJ_FIELD_NUMBER: _ClassVar[int]
    FMOIOMLDAJK_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    GJEBAJAJPII: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    FGFLJIAEMLJ: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    FMOIOMLDAJK: int
    guid: int
    def __init__(self, GJEBAJAJPII: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., FGFLJIAEMLJ: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., FMOIOMLDAJK: _Optional[int] = ..., guid: _Optional[int] = ...) -> None: ...
