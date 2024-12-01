from genshin.packet.proto import AHFCCKGEIJD_pb2 as _AHFCCKGEIJD_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FNLOEBIAJIE(_message.Message):
    __slots__ = ("LBKDGOEFEBC", "CPMEFHEEOAH", "AEEDOAGEHPP", "GGIGCLLHEFM", "AJCGKKPCCGD", "text", "icon", "system_hint", "NCCPPHNNPBF", "BKAMPGBBBFP")
    LBKDGOEFEBC_FIELD_NUMBER: _ClassVar[int]
    CPMEFHEEOAH_FIELD_NUMBER: _ClassVar[int]
    AEEDOAGEHPP_FIELD_NUMBER: _ClassVar[int]
    GGIGCLLHEFM_FIELD_NUMBER: _ClassVar[int]
    AJCGKKPCCGD_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_HINT_FIELD_NUMBER: _ClassVar[int]
    NCCPPHNNPBF_FIELD_NUMBER: _ClassVar[int]
    BKAMPGBBBFP_FIELD_NUMBER: _ClassVar[int]
    LBKDGOEFEBC: str
    CPMEFHEEOAH: int
    AEEDOAGEHPP: int
    GGIGCLLHEFM: int
    AJCGKKPCCGD: int
    text: str
    icon: int
    system_hint: _AHFCCKGEIJD_pb2.AHFCCKGEIJD
    NCCPPHNNPBF: int
    BKAMPGBBBFP: bool
    def __init__(self, LBKDGOEFEBC: _Optional[str] = ..., CPMEFHEEOAH: _Optional[int] = ..., AEEDOAGEHPP: _Optional[int] = ..., GGIGCLLHEFM: _Optional[int] = ..., AJCGKKPCCGD: _Optional[int] = ..., text: _Optional[str] = ..., icon: _Optional[int] = ..., system_hint: _Optional[_Union[_AHFCCKGEIJD_pb2.AHFCCKGEIJD, _Mapping]] = ..., NCCPPHNNPBF: _Optional[int] = ..., BKAMPGBBBFP: bool = ...) -> None: ...
