from genshin.packet.proto import EPHALEJPIKM_pb2 as _EPHALEJPIKM_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PKBDLALMJML(_message.Message):
    __slots__ = ("KBGFIGBANGK", "MBBKAENBCKD", "FGLOHNKKPPG", "IIGDIKAKPCC", "PINGABDELME")
    KBGFIGBANGK_FIELD_NUMBER: _ClassVar[int]
    MBBKAENBCKD_FIELD_NUMBER: _ClassVar[int]
    FGLOHNKKPPG_FIELD_NUMBER: _ClassVar[int]
    IIGDIKAKPCC_FIELD_NUMBER: _ClassVar[int]
    PINGABDELME_FIELD_NUMBER: _ClassVar[int]
    KBGFIGBANGK: _containers.RepeatedScalarFieldContainer[int]
    MBBKAENBCKD: int
    FGLOHNKKPPG: bool
    IIGDIKAKPCC: _EPHALEJPIKM_pb2.EPHALEJPIKM
    PINGABDELME: int
    def __init__(self, KBGFIGBANGK: _Optional[_Iterable[int]] = ..., MBBKAENBCKD: _Optional[int] = ..., FGLOHNKKPPG: bool = ..., IIGDIKAKPCC: _Optional[_Union[_EPHALEJPIKM_pb2.EPHALEJPIKM, str]] = ..., PINGABDELME: _Optional[int] = ...) -> None: ...
