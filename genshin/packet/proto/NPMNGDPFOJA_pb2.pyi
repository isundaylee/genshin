from genshin.packet.proto import NGOFPEOLOPF_pb2 as _NGOFPEOLOPF_pb2
from genshin.packet.proto import MLOBECPAOCA_pb2 as _MLOBECPAOCA_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NPMNGDPFOJA(_message.Message):
    __slots__ = ("DJMCHFPIFLM", "NDDOBGMDGLA", "OFNOGJPGBNA", "EJNINFFFKJP")
    DJMCHFPIFLM_FIELD_NUMBER: _ClassVar[int]
    NDDOBGMDGLA_FIELD_NUMBER: _ClassVar[int]
    OFNOGJPGBNA_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    DJMCHFPIFLM: _containers.RepeatedCompositeFieldContainer[_NGOFPEOLOPF_pb2.NGOFPEOLOPF]
    NDDOBGMDGLA: _containers.RepeatedCompositeFieldContainer[_MLOBECPAOCA_pb2.MLOBECPAOCA]
    OFNOGJPGBNA: int
    EJNINFFFKJP: int
    def __init__(self, DJMCHFPIFLM: _Optional[_Iterable[_Union[_NGOFPEOLOPF_pb2.NGOFPEOLOPF, _Mapping]]] = ..., NDDOBGMDGLA: _Optional[_Iterable[_Union[_MLOBECPAOCA_pb2.MLOBECPAOCA, _Mapping]]] = ..., OFNOGJPGBNA: _Optional[int] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
