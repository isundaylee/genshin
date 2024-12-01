from genshin.packet.proto import IOEOEIMKMJD_pb2 as _IOEOEIMKMJD_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MDDPOFCADGC(_message.Message):
    __slots__ = ("AGDKNOHOOPG", "NLJEJPGCPCI", "JHCCPFIPJPM", "IMIOGMDOKCB")
    AGDKNOHOOPG_FIELD_NUMBER: _ClassVar[int]
    NLJEJPGCPCI_FIELD_NUMBER: _ClassVar[int]
    JHCCPFIPJPM_FIELD_NUMBER: _ClassVar[int]
    IMIOGMDOKCB_FIELD_NUMBER: _ClassVar[int]
    AGDKNOHOOPG: int
    NLJEJPGCPCI: float
    JHCCPFIPJPM: float
    IMIOGMDOKCB: _IOEOEIMKMJD_pb2.IOEOEIMKMJD
    def __init__(self, AGDKNOHOOPG: _Optional[int] = ..., NLJEJPGCPCI: _Optional[float] = ..., JHCCPFIPJPM: _Optional[float] = ..., IMIOGMDOKCB: _Optional[_Union[_IOEOEIMKMJD_pb2.IOEOEIMKMJD, str]] = ...) -> None: ...
