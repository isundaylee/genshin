from genshin.packet.proto import KNMPNCPBMMP_pb2 as _KNMPNCPBMMP_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DECPHDLMILB(_message.Message):
    __slots__ = ("HMLFALPADMC", "GKNIKFALMCC", "AGIDBEEINDE", "GLPDDOJKFBG", "KBNHDNPJJBH")
    HMLFALPADMC_FIELD_NUMBER: _ClassVar[int]
    GKNIKFALMCC_FIELD_NUMBER: _ClassVar[int]
    AGIDBEEINDE_FIELD_NUMBER: _ClassVar[int]
    GLPDDOJKFBG_FIELD_NUMBER: _ClassVar[int]
    KBNHDNPJJBH_FIELD_NUMBER: _ClassVar[int]
    HMLFALPADMC: _KNMPNCPBMMP_pb2.KNMPNCPBMMP
    GKNIKFALMCC: int
    AGIDBEEINDE: int
    GLPDDOJKFBG: int
    KBNHDNPJJBH: int
    def __init__(self, HMLFALPADMC: _Optional[_Union[_KNMPNCPBMMP_pb2.KNMPNCPBMMP, _Mapping]] = ..., GKNIKFALMCC: _Optional[int] = ..., AGIDBEEINDE: _Optional[int] = ..., GLPDDOJKFBG: _Optional[int] = ..., KBNHDNPJJBH: _Optional[int] = ...) -> None: ...
