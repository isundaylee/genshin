from genshin.packet.proto import AvatarExpeditionState_pb2 as _AvatarExpeditionState_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IGKLNNDNCMG(_message.Message):
    __slots__ = ("MIMEIGLBOPI", "CDBFPFOJBIJ", "PGIIOIBNKKE", "CCHOPBCADIG", "AEHJBEELKOO")
    MIMEIGLBOPI_FIELD_NUMBER: _ClassVar[int]
    CDBFPFOJBIJ_FIELD_NUMBER: _ClassVar[int]
    PGIIOIBNKKE_FIELD_NUMBER: _ClassVar[int]
    CCHOPBCADIG_FIELD_NUMBER: _ClassVar[int]
    AEHJBEELKOO_FIELD_NUMBER: _ClassVar[int]
    MIMEIGLBOPI: int
    CDBFPFOJBIJ: _AvatarExpeditionState_pb2.AvatarExpeditionState
    PGIIOIBNKKE: float
    CCHOPBCADIG: int
    AEHJBEELKOO: int
    def __init__(self, MIMEIGLBOPI: _Optional[int] = ..., CDBFPFOJBIJ: _Optional[_Union[_AvatarExpeditionState_pb2.AvatarExpeditionState, str]] = ..., PGIIOIBNKKE: _Optional[float] = ..., CCHOPBCADIG: _Optional[int] = ..., AEHJBEELKOO: _Optional[int] = ...) -> None: ...
