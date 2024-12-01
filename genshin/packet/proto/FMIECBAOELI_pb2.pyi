from genshin.packet.proto import EAFHLMDCHKO_pb2 as _EAFHLMDCHKO_pb2
from genshin.packet.proto import MBIMHNFDGHN_pb2 as _MBIMHNFDGHN_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FMIECBAOELI(_message.Message):
    __slots__ = ("NIAKDCHEDCE", "BELACGKAHLM")
    NIAKDCHEDCE_FIELD_NUMBER: _ClassVar[int]
    BELACGKAHLM_FIELD_NUMBER: _ClassVar[int]
    NIAKDCHEDCE: _EAFHLMDCHKO_pb2.EAFHLMDCHKO
    BELACGKAHLM: _MBIMHNFDGHN_pb2.MBIMHNFDGHN
    def __init__(self, NIAKDCHEDCE: _Optional[_Union[_EAFHLMDCHKO_pb2.EAFHLMDCHKO, _Mapping]] = ..., BELACGKAHLM: _Optional[_Union[_MBIMHNFDGHN_pb2.MBIMHNFDGHN, str]] = ...) -> None: ...
