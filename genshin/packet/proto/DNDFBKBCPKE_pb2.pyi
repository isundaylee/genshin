from genshin.packet.proto import DPDMGOJJJLE_pb2 as _DPDMGOJJJLE_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DNDFBKBCPKE(_message.Message):
    __slots__ = ("JHIOHAJFMGE", "OPAAEJNKKEL", "MOEKHDPGIHJ", "EJNINFFFKJP")
    JHIOHAJFMGE_FIELD_NUMBER: _ClassVar[int]
    OPAAEJNKKEL_FIELD_NUMBER: _ClassVar[int]
    MOEKHDPGIHJ_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    JHIOHAJFMGE: _containers.RepeatedScalarFieldContainer[int]
    OPAAEJNKKEL: _containers.RepeatedScalarFieldContainer[int]
    MOEKHDPGIHJ: _containers.RepeatedCompositeFieldContainer[_DPDMGOJJJLE_pb2.DPDMGOJJJLE]
    EJNINFFFKJP: int
    def __init__(self, JHIOHAJFMGE: _Optional[_Iterable[int]] = ..., OPAAEJNKKEL: _Optional[_Iterable[int]] = ..., MOEKHDPGIHJ: _Optional[_Iterable[_Union[_DPDMGOJJJLE_pb2.DPDMGOJJJLE, _Mapping]]] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
