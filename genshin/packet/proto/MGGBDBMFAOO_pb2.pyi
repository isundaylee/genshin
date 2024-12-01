from genshin.packet.proto import CGHBPGPBEMP_pb2 as _CGHBPGPBEMP_pb2
from genshin.packet.proto import MBIMHNFDGHN_pb2 as _MBIMHNFDGHN_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MGGBDBMFAOO(_message.Message):
    __slots__ = ("NFEMCDJECDB", "OMNBFGPNDKK", "BELACGKAHLM")
    NFEMCDJECDB_FIELD_NUMBER: _ClassVar[int]
    OMNBFGPNDKK_FIELD_NUMBER: _ClassVar[int]
    BELACGKAHLM_FIELD_NUMBER: _ClassVar[int]
    NFEMCDJECDB: bytes
    OMNBFGPNDKK: _CGHBPGPBEMP_pb2.CGHBPGPBEMP
    BELACGKAHLM: _MBIMHNFDGHN_pb2.MBIMHNFDGHN
    def __init__(self, NFEMCDJECDB: _Optional[bytes] = ..., OMNBFGPNDKK: _Optional[_Union[_CGHBPGPBEMP_pb2.CGHBPGPBEMP, str]] = ..., BELACGKAHLM: _Optional[_Union[_MBIMHNFDGHN_pb2.MBIMHNFDGHN, str]] = ...) -> None: ...
