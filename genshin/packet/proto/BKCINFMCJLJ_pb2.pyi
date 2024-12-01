from genshin.packet.proto import MFGKDAPGLBG_pb2 as _MFGKDAPGLBG_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BKCINFMCJLJ(_message.Message):
    __slots__ = ("BAHEJMIPPJI", "HLNHPDEBKEK", "GFLLBCGNOKJ", "GINEMCIFFNB", "GLMJFMIJHFG")
    BAHEJMIPPJI_FIELD_NUMBER: _ClassVar[int]
    HLNHPDEBKEK_FIELD_NUMBER: _ClassVar[int]
    GFLLBCGNOKJ_FIELD_NUMBER: _ClassVar[int]
    GINEMCIFFNB_FIELD_NUMBER: _ClassVar[int]
    GLMJFMIJHFG_FIELD_NUMBER: _ClassVar[int]
    BAHEJMIPPJI: _containers.RepeatedCompositeFieldContainer[_MFGKDAPGLBG_pb2.MFGKDAPGLBG]
    HLNHPDEBKEK: _containers.RepeatedScalarFieldContainer[int]
    GFLLBCGNOKJ: _containers.RepeatedScalarFieldContainer[int]
    GINEMCIFFNB: int
    GLMJFMIJHFG: int
    def __init__(self, BAHEJMIPPJI: _Optional[_Iterable[_Union[_MFGKDAPGLBG_pb2.MFGKDAPGLBG, _Mapping]]] = ..., HLNHPDEBKEK: _Optional[_Iterable[int]] = ..., GFLLBCGNOKJ: _Optional[_Iterable[int]] = ..., GINEMCIFFNB: _Optional[int] = ..., GLMJFMIJHFG: _Optional[int] = ...) -> None: ...
