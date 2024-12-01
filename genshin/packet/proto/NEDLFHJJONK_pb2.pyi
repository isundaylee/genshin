from genshin.packet.proto import IJPADIGMNPH_pb2 as _IJPADIGMNPH_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NEDLFHJJONK(_message.Message):
    __slots__ = ("HPOECKEKAFA", "FFOBIONLMOJ", "IGBDOEBPPHO", "CCKJPDCHOBJ", "KLMMAMBHJDM")
    HPOECKEKAFA_FIELD_NUMBER: _ClassVar[int]
    FFOBIONLMOJ_FIELD_NUMBER: _ClassVar[int]
    IGBDOEBPPHO_FIELD_NUMBER: _ClassVar[int]
    CCKJPDCHOBJ_FIELD_NUMBER: _ClassVar[int]
    KLMMAMBHJDM_FIELD_NUMBER: _ClassVar[int]
    HPOECKEKAFA: _IJPADIGMNPH_pb2.IJPADIGMNPH
    FFOBIONLMOJ: int
    IGBDOEBPPHO: int
    CCKJPDCHOBJ: float
    KLMMAMBHJDM: int
    def __init__(self, HPOECKEKAFA: _Optional[_Union[_IJPADIGMNPH_pb2.IJPADIGMNPH, _Mapping]] = ..., FFOBIONLMOJ: _Optional[int] = ..., IGBDOEBPPHO: _Optional[int] = ..., CCKJPDCHOBJ: _Optional[float] = ..., KLMMAMBHJDM: _Optional[int] = ...) -> None: ...
