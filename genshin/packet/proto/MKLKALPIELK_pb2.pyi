from genshin.packet.proto import KDEHCGJAGFJ_pb2 as _KDEHCGJAGFJ_pb2
from genshin.packet.proto import MBIMHNFDGHN_pb2 as _MBIMHNFDGHN_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MKLKALPIELK(_message.Message):
    __slots__ = ("PGAKCCIKEBE", "BELACGKAHLM", "AGIDBEEINDE")
    PGAKCCIKEBE_FIELD_NUMBER: _ClassVar[int]
    BELACGKAHLM_FIELD_NUMBER: _ClassVar[int]
    AGIDBEEINDE_FIELD_NUMBER: _ClassVar[int]
    PGAKCCIKEBE: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    BELACGKAHLM: _MBIMHNFDGHN_pb2.MBIMHNFDGHN
    AGIDBEEINDE: int
    def __init__(self, PGAKCCIKEBE: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., BELACGKAHLM: _Optional[_Union[_MBIMHNFDGHN_pb2.MBIMHNFDGHN, str]] = ..., AGIDBEEINDE: _Optional[int] = ...) -> None: ...
