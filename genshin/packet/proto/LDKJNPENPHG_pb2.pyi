from genshin.packet.proto import EPLPHILHOHE_pb2 as _EPLPHILHOHE_pb2
from genshin.packet.proto import MBIMHNFDGHN_pb2 as _MBIMHNFDGHN_pb2
from genshin.packet.proto import FJKNAAMGEMM_pb2 as _FJKNAAMGEMM_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LDKJNPENPHG(_message.Message):
    __slots__ = ("FABFBKDGMJK", "KFJEADMAPLK", "LDKIINLHCOP", "AGIDBEEINDE", "BELACGKAHLM", "JPHBOKDMDAH", "DNOPMABMHMG", "OMNBFGPNDKK", "HNOGKEHFLHE")
    FABFBKDGMJK_FIELD_NUMBER: _ClassVar[int]
    KFJEADMAPLK_FIELD_NUMBER: _ClassVar[int]
    LDKIINLHCOP_FIELD_NUMBER: _ClassVar[int]
    AGIDBEEINDE_FIELD_NUMBER: _ClassVar[int]
    BELACGKAHLM_FIELD_NUMBER: _ClassVar[int]
    JPHBOKDMDAH_FIELD_NUMBER: _ClassVar[int]
    DNOPMABMHMG_FIELD_NUMBER: _ClassVar[int]
    OMNBFGPNDKK_FIELD_NUMBER: _ClassVar[int]
    HNOGKEHFLHE_FIELD_NUMBER: _ClassVar[int]
    FABFBKDGMJK: bytes
    KFJEADMAPLK: _EPLPHILHOHE_pb2.EPLPHILHOHE
    LDKIINLHCOP: bool
    AGIDBEEINDE: int
    BELACGKAHLM: _MBIMHNFDGHN_pb2.MBIMHNFDGHN
    JPHBOKDMDAH: int
    DNOPMABMHMG: float
    OMNBFGPNDKK: _FJKNAAMGEMM_pb2.FJKNAAMGEMM
    HNOGKEHFLHE: int
    def __init__(self, FABFBKDGMJK: _Optional[bytes] = ..., KFJEADMAPLK: _Optional[_Union[_EPLPHILHOHE_pb2.EPLPHILHOHE, _Mapping]] = ..., LDKIINLHCOP: bool = ..., AGIDBEEINDE: _Optional[int] = ..., BELACGKAHLM: _Optional[_Union[_MBIMHNFDGHN_pb2.MBIMHNFDGHN, str]] = ..., JPHBOKDMDAH: _Optional[int] = ..., DNOPMABMHMG: _Optional[float] = ..., OMNBFGPNDKK: _Optional[_Union[_FJKNAAMGEMM_pb2.FJKNAAMGEMM, str]] = ..., HNOGKEHFLHE: _Optional[int] = ...) -> None: ...
