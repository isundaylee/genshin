from genshin.packet.proto import KDEHCGJAGFJ_pb2 as _KDEHCGJAGFJ_pb2
from genshin.packet.proto import MBIMHNFDGHN_pb2 as _MBIMHNFDGHN_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ANGJECDGBOI(_message.Message):
    __slots__ = ("HKNMIKEOPCC", "AGIDBEEINDE", "BELACGKAHLM")
    HKNMIKEOPCC_FIELD_NUMBER: _ClassVar[int]
    AGIDBEEINDE_FIELD_NUMBER: _ClassVar[int]
    BELACGKAHLM_FIELD_NUMBER: _ClassVar[int]
    HKNMIKEOPCC: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    AGIDBEEINDE: int
    BELACGKAHLM: _MBIMHNFDGHN_pb2.MBIMHNFDGHN
    def __init__(self, HKNMIKEOPCC: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., AGIDBEEINDE: _Optional[int] = ..., BELACGKAHLM: _Optional[_Union[_MBIMHNFDGHN_pb2.MBIMHNFDGHN, str]] = ...) -> None: ...
