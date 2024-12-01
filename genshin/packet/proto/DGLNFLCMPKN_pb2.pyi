from genshin.packet.proto import BINOOCJMLCB_pb2 as _BINOOCJMLCB_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DGLNFLCMPKN(_message.Message):
    __slots__ = ("FAPMPNADDDF", "AMLNLDNJJID", "LCDDIDLJEDN", "EFKNDDJEPLJ", "CEJABHLHHAC")
    FAPMPNADDDF_FIELD_NUMBER: _ClassVar[int]
    AMLNLDNJJID_FIELD_NUMBER: _ClassVar[int]
    LCDDIDLJEDN_FIELD_NUMBER: _ClassVar[int]
    EFKNDDJEPLJ_FIELD_NUMBER: _ClassVar[int]
    CEJABHLHHAC_FIELD_NUMBER: _ClassVar[int]
    FAPMPNADDDF: _containers.RepeatedScalarFieldContainer[int]
    AMLNLDNJJID: _containers.RepeatedScalarFieldContainer[int]
    LCDDIDLJEDN: int
    EFKNDDJEPLJ: int
    CEJABHLHHAC: _BINOOCJMLCB_pb2.BINOOCJMLCB
    def __init__(self, FAPMPNADDDF: _Optional[_Iterable[int]] = ..., AMLNLDNJJID: _Optional[_Iterable[int]] = ..., LCDDIDLJEDN: _Optional[int] = ..., EFKNDDJEPLJ: _Optional[int] = ..., CEJABHLHHAC: _Optional[_Union[_BINOOCJMLCB_pb2.BINOOCJMLCB, str]] = ...) -> None: ...
