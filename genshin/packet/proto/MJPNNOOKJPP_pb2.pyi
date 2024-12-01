from genshin.packet.proto import EGMCILPCONK_pb2 as _EGMCILPCONK_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MJPNNOOKJPP(_message.Message):
    __slots__ = ("DAFBMPHNLMA", "ICEDEBJHCGF", "IIDNCNKMBAO", "PIHNDEGFMPH")
    DAFBMPHNLMA_FIELD_NUMBER: _ClassVar[int]
    ICEDEBJHCGF_FIELD_NUMBER: _ClassVar[int]
    IIDNCNKMBAO_FIELD_NUMBER: _ClassVar[int]
    PIHNDEGFMPH_FIELD_NUMBER: _ClassVar[int]
    DAFBMPHNLMA: int
    ICEDEBJHCGF: _EGMCILPCONK_pb2.EGMCILPCONK
    IIDNCNKMBAO: int
    PIHNDEGFMPH: int
    def __init__(self, DAFBMPHNLMA: _Optional[int] = ..., ICEDEBJHCGF: _Optional[_Union[_EGMCILPCONK_pb2.EGMCILPCONK, str]] = ..., IIDNCNKMBAO: _Optional[int] = ..., PIHNDEGFMPH: _Optional[int] = ...) -> None: ...
