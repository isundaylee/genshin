from genshin.packet.proto import FGJFCIGOBCN_pb2 as _FGJFCIGOBCN_pb2
from genshin.packet.proto import KDEHCGJAGFJ_pb2 as _KDEHCGJAGFJ_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OHAPEBODAPG(_message.Message):
    __slots__ = ("GBANJKINLGK", "GJEBAJAJPII", "FGFLJIAEMLJ", "OEGJAILDLBK", "guid")
    GBANJKINLGK_FIELD_NUMBER: _ClassVar[int]
    GJEBAJAJPII_FIELD_NUMBER: _ClassVar[int]
    FGFLJIAEMLJ_FIELD_NUMBER: _ClassVar[int]
    OEGJAILDLBK_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    GBANJKINLGK: _containers.RepeatedCompositeFieldContainer[_FGJFCIGOBCN_pb2.FGJFCIGOBCN]
    GJEBAJAJPII: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    FGFLJIAEMLJ: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    OEGJAILDLBK: int
    guid: int
    def __init__(self, GBANJKINLGK: _Optional[_Iterable[_Union[_FGJFCIGOBCN_pb2.FGJFCIGOBCN, _Mapping]]] = ..., GJEBAJAJPII: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., FGFLJIAEMLJ: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., OEGJAILDLBK: _Optional[int] = ..., guid: _Optional[int] = ...) -> None: ...
