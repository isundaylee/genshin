from genshin.packet.proto import NMCEGCNOBKI_pb2 as _NMCEGCNOBKI_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JBNLGHJJKMO(_message.Message):
    __slots__ = ("FINAHGLFHAG", "JABGACILLEC", "bonus_info", "LKOFKODPMGO", "DNBEFLJLAMB", "EJLGMDFFMOO")
    FINAHGLFHAG_FIELD_NUMBER: _ClassVar[int]
    JABGACILLEC_FIELD_NUMBER: _ClassVar[int]
    BONUS_INFO_FIELD_NUMBER: _ClassVar[int]
    LKOFKODPMGO_FIELD_NUMBER: _ClassVar[int]
    DNBEFLJLAMB_FIELD_NUMBER: _ClassVar[int]
    EJLGMDFFMOO_FIELD_NUMBER: _ClassVar[int]
    FINAHGLFHAG: int
    JABGACILLEC: int
    bonus_info: _NMCEGCNOBKI_pb2.NMCEGCNOBKI
    LKOFKODPMGO: int
    DNBEFLJLAMB: int
    EJLGMDFFMOO: bool
    def __init__(self, FINAHGLFHAG: _Optional[int] = ..., JABGACILLEC: _Optional[int] = ..., bonus_info: _Optional[_Union[_NMCEGCNOBKI_pb2.NMCEGCNOBKI, _Mapping]] = ..., LKOFKODPMGO: _Optional[int] = ..., DNBEFLJLAMB: _Optional[int] = ..., EJLGMDFFMOO: bool = ...) -> None: ...
