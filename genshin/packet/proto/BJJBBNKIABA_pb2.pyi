from genshin.packet.proto import GDHBFFBPIIJ_pb2 as _GDHBFFBPIIJ_pb2
from genshin.packet.proto import MBIMHNFDGHN_pb2 as _MBIMHNFDGHN_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BJJBBNKIABA(_message.Message):
    __slots__ = ("GGPKAKOCHAI", "BELACGKAHLM", "AGIDBEEINDE", "FFEKMFFDNAP")
    GGPKAKOCHAI_FIELD_NUMBER: _ClassVar[int]
    BELACGKAHLM_FIELD_NUMBER: _ClassVar[int]
    AGIDBEEINDE_FIELD_NUMBER: _ClassVar[int]
    FFEKMFFDNAP_FIELD_NUMBER: _ClassVar[int]
    GGPKAKOCHAI: _GDHBFFBPIIJ_pb2.GDHBFFBPIIJ
    BELACGKAHLM: _MBIMHNFDGHN_pb2.MBIMHNFDGHN
    AGIDBEEINDE: int
    FFEKMFFDNAP: bool
    def __init__(self, GGPKAKOCHAI: _Optional[_Union[_GDHBFFBPIIJ_pb2.GDHBFFBPIIJ, _Mapping]] = ..., BELACGKAHLM: _Optional[_Union[_MBIMHNFDGHN_pb2.MBIMHNFDGHN, str]] = ..., AGIDBEEINDE: _Optional[int] = ..., FFEKMFFDNAP: bool = ...) -> None: ...
