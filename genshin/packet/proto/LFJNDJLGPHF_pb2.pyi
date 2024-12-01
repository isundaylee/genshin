from genshin.packet.proto import COANHIFNGHK_pb2 as _COANHIFNGHK_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LFJNDJLGPHF(_message.Message):
    __slots__ = ("AMPBNDIACMI", "NKANJIJNIMC", "IBCOIOKMGGE", "AGOPLLENLAO", "MBDFAMEKCKB", "resin_card", "LJBNCMIDOBM", "MANAANIBALB")
    AMPBNDIACMI_FIELD_NUMBER: _ClassVar[int]
    NKANJIJNIMC_FIELD_NUMBER: _ClassVar[int]
    IBCOIOKMGGE_FIELD_NUMBER: _ClassVar[int]
    AGOPLLENLAO_FIELD_NUMBER: _ClassVar[int]
    MBDFAMEKCKB_FIELD_NUMBER: _ClassVar[int]
    RESIN_CARD_FIELD_NUMBER: _ClassVar[int]
    LJBNCMIDOBM_FIELD_NUMBER: _ClassVar[int]
    MANAANIBALB_FIELD_NUMBER: _ClassVar[int]
    AMPBNDIACMI: str
    NKANJIJNIMC: str
    IBCOIOKMGGE: int
    AGOPLLENLAO: int
    MBDFAMEKCKB: int
    resin_card: _COANHIFNGHK_pb2.COANHIFNGHK
    LJBNCMIDOBM: int
    MANAANIBALB: int
    def __init__(self, AMPBNDIACMI: _Optional[str] = ..., NKANJIJNIMC: _Optional[str] = ..., IBCOIOKMGGE: _Optional[int] = ..., AGOPLLENLAO: _Optional[int] = ..., MBDFAMEKCKB: _Optional[int] = ..., resin_card: _Optional[_Union[_COANHIFNGHK_pb2.COANHIFNGHK, _Mapping]] = ..., LJBNCMIDOBM: _Optional[int] = ..., MANAANIBALB: _Optional[int] = ...) -> None: ...
