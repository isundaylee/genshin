from genshin.packet.proto import EALJLLMBDEA_pb2 as _EALJLLMBDEA_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DPPLPCHGCLJ(_message.Message):
    __slots__ = ("MCICEHMKGMG", "OPOOBJEOOKM", "LEHGMKPFFDC", "DMKAGPPKIKG")
    MCICEHMKGMG_FIELD_NUMBER: _ClassVar[int]
    OPOOBJEOOKM_FIELD_NUMBER: _ClassVar[int]
    LEHGMKPFFDC_FIELD_NUMBER: _ClassVar[int]
    DMKAGPPKIKG_FIELD_NUMBER: _ClassVar[int]
    MCICEHMKGMG: _containers.RepeatedScalarFieldContainer[int]
    OPOOBJEOOKM: _EALJLLMBDEA_pb2.EALJLLMBDEA
    LEHGMKPFFDC: int
    DMKAGPPKIKG: int
    def __init__(self, MCICEHMKGMG: _Optional[_Iterable[int]] = ..., OPOOBJEOOKM: _Optional[_Union[_EALJLLMBDEA_pb2.EALJLLMBDEA, str]] = ..., LEHGMKPFFDC: _Optional[int] = ..., DMKAGPPKIKG: _Optional[int] = ...) -> None: ...
