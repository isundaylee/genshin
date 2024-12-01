from genshin.packet.proto import NPPCJPHMHBM_pb2 as _NPPCJPHMHBM_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EEINAMGKPJK(_message.Message):
    __slots__ = ("MMDAIFBDGLJ", "NKCOLNAJDCA")
    MMDAIFBDGLJ_FIELD_NUMBER: _ClassVar[int]
    NKCOLNAJDCA_FIELD_NUMBER: _ClassVar[int]
    MMDAIFBDGLJ: _NPPCJPHMHBM_pb2.NPPCJPHMHBM
    NKCOLNAJDCA: int
    def __init__(self, MMDAIFBDGLJ: _Optional[_Union[_NPPCJPHMHBM_pb2.NPPCJPHMHBM, str]] = ..., NKCOLNAJDCA: _Optional[int] = ...) -> None: ...
