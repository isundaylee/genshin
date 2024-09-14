from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerCookArgsRsp(_message.Message):
    __slots__ = ("qte_range_ratio", "retcode")
    QTE_RANGE_RATIO_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    qte_range_ratio: float
    retcode: int
    def __init__(self, qte_range_ratio: _Optional[float] = ..., retcode: _Optional[int] = ...) -> None: ...
