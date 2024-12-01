from genshin.packet.proto import OLODDMHDDGC_pb2 as _OLODDMHDDGC_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AEFFGHNMPOH(_message.Message):
    __slots__ = ("NKGEKOMLLNG", "IMIOGMDOKCB", "JPLLDOBLMGD")
    NKGEKOMLLNG_FIELD_NUMBER: _ClassVar[int]
    IMIOGMDOKCB_FIELD_NUMBER: _ClassVar[int]
    JPLLDOBLMGD_FIELD_NUMBER: _ClassVar[int]
    NKGEKOMLLNG: int
    IMIOGMDOKCB: _OLODDMHDDGC_pb2.OLODDMHDDGC
    JPLLDOBLMGD: int
    def __init__(self, NKGEKOMLLNG: _Optional[int] = ..., IMIOGMDOKCB: _Optional[_Union[_OLODDMHDDGC_pb2.OLODDMHDDGC, str]] = ..., JPLLDOBLMGD: _Optional[int] = ...) -> None: ...
