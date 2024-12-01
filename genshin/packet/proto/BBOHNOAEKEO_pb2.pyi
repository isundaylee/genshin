from genshin.packet.proto import ALKBANNMCBH_pb2 as _ALKBANNMCBH_pb2
from genshin.packet.proto import PAGIAOELFBI_pb2 as _PAGIAOELFBI_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BBOHNOAEKEO(_message.Message):
    __slots__ = ("KIINDLKBNPD", "EIMCFAMHHBJ", "FCPANCMAOIE", "type")
    KIINDLKBNPD_FIELD_NUMBER: _ClassVar[int]
    EIMCFAMHHBJ_FIELD_NUMBER: _ClassVar[int]
    FCPANCMAOIE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    KIINDLKBNPD: _containers.RepeatedCompositeFieldContainer[_ALKBANNMCBH_pb2.ALKBANNMCBH]
    EIMCFAMHHBJ: _PAGIAOELFBI_pb2.PAGIAOELFBI
    FCPANCMAOIE: int
    type: int
    def __init__(self, KIINDLKBNPD: _Optional[_Iterable[_Union[_ALKBANNMCBH_pb2.ALKBANNMCBH, _Mapping]]] = ..., EIMCFAMHHBJ: _Optional[_Union[_PAGIAOELFBI_pb2.PAGIAOELFBI, _Mapping]] = ..., FCPANCMAOIE: _Optional[int] = ..., type: _Optional[int] = ...) -> None: ...
