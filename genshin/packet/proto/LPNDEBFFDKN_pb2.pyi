from genshin.packet.proto import BPNPAPAAHGN_pb2 as _BPNPAPAAHGN_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LPNDEBFFDKN(_message.Message):
    __slots__ = ("EOAGPBCCFMM", "EJNINFFFKJP", "KLMDAPCLGAP")
    EOAGPBCCFMM_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    KLMDAPCLGAP_FIELD_NUMBER: _ClassVar[int]
    EOAGPBCCFMM: _containers.RepeatedCompositeFieldContainer[_BPNPAPAAHGN_pb2.BPNPAPAAHGN]
    EJNINFFFKJP: int
    KLMDAPCLGAP: int
    def __init__(self, EOAGPBCCFMM: _Optional[_Iterable[_Union[_BPNPAPAAHGN_pb2.BPNPAPAAHGN, _Mapping]]] = ..., EJNINFFFKJP: _Optional[int] = ..., KLMDAPCLGAP: _Optional[int] = ...) -> None: ...
