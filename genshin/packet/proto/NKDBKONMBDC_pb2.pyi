from genshin.packet.proto import MFGKDAPGLBG_pb2 as _MFGKDAPGLBG_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NKDBKONMBDC(_message.Message):
    __slots__ = ("AIAJGGDJAKB", "ONLOCEPEPEA", "GPCGMMOBGHM", "GINEMCIFFNB", "KJJOLFAMIKC")
    AIAJGGDJAKB_FIELD_NUMBER: _ClassVar[int]
    ONLOCEPEPEA_FIELD_NUMBER: _ClassVar[int]
    GPCGMMOBGHM_FIELD_NUMBER: _ClassVar[int]
    GINEMCIFFNB_FIELD_NUMBER: _ClassVar[int]
    KJJOLFAMIKC_FIELD_NUMBER: _ClassVar[int]
    AIAJGGDJAKB: _containers.RepeatedScalarFieldContainer[int]
    ONLOCEPEPEA: _containers.RepeatedScalarFieldContainer[int]
    GPCGMMOBGHM: _containers.RepeatedCompositeFieldContainer[_MFGKDAPGLBG_pb2.MFGKDAPGLBG]
    GINEMCIFFNB: int
    KJJOLFAMIKC: int
    def __init__(self, AIAJGGDJAKB: _Optional[_Iterable[int]] = ..., ONLOCEPEPEA: _Optional[_Iterable[int]] = ..., GPCGMMOBGHM: _Optional[_Iterable[_Union[_MFGKDAPGLBG_pb2.MFGKDAPGLBG, _Mapping]]] = ..., GINEMCIFFNB: _Optional[int] = ..., KJJOLFAMIKC: _Optional[int] = ...) -> None: ...
