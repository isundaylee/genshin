from genshin.packet.proto import CBGGFCJFPLH_pb2 as _CBGGFCJFPLH_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PJEDOHKAKPG(_message.Message):
    __slots__ = ("GMCABIAOLJH", "JMCFOMABGHD", "JCJIOFHANOM", "GCGIPIGNPDA", "exp", "ODECBCEBGEF", "MLMBMLBPMCO", "AKBCICCACOK", "level")
    GMCABIAOLJH_FIELD_NUMBER: _ClassVar[int]
    JMCFOMABGHD_FIELD_NUMBER: _ClassVar[int]
    JCJIOFHANOM_FIELD_NUMBER: _ClassVar[int]
    GCGIPIGNPDA_FIELD_NUMBER: _ClassVar[int]
    EXP_FIELD_NUMBER: _ClassVar[int]
    ODECBCEBGEF_FIELD_NUMBER: _ClassVar[int]
    MLMBMLBPMCO_FIELD_NUMBER: _ClassVar[int]
    AKBCICCACOK_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    GMCABIAOLJH: str
    JMCFOMABGHD: _CBGGFCJFPLH_pb2.CBGGFCJFPLH
    JCJIOFHANOM: bool
    GCGIPIGNPDA: int
    exp: int
    ODECBCEBGEF: int
    MLMBMLBPMCO: int
    AKBCICCACOK: int
    level: int
    def __init__(self, GMCABIAOLJH: _Optional[str] = ..., JMCFOMABGHD: _Optional[_Union[_CBGGFCJFPLH_pb2.CBGGFCJFPLH, _Mapping]] = ..., JCJIOFHANOM: bool = ..., GCGIPIGNPDA: _Optional[int] = ..., exp: _Optional[int] = ..., ODECBCEBGEF: _Optional[int] = ..., MLMBMLBPMCO: _Optional[int] = ..., AKBCICCACOK: _Optional[int] = ..., level: _Optional[int] = ...) -> None: ...
