from genshin.packet.proto import LNCNFMEIOLI_pb2 as _LNCNFMEIOLI_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JJMPCHMGGGF(_message.Message):
    __slots__ = ("DKOAGLJAAFA", "KNGJHMLLCNP", "FADINCNPBMD", "AGIDBEEINDE", "ODCMKOFFKKL", "DMCCAJMCFPA")
    DKOAGLJAAFA_FIELD_NUMBER: _ClassVar[int]
    KNGJHMLLCNP_FIELD_NUMBER: _ClassVar[int]
    FADINCNPBMD_FIELD_NUMBER: _ClassVar[int]
    AGIDBEEINDE_FIELD_NUMBER: _ClassVar[int]
    ODCMKOFFKKL_FIELD_NUMBER: _ClassVar[int]
    DMCCAJMCFPA_FIELD_NUMBER: _ClassVar[int]
    DKOAGLJAAFA: _containers.RepeatedCompositeFieldContainer[_LNCNFMEIOLI_pb2.LNCNFMEIOLI]
    KNGJHMLLCNP: int
    FADINCNPBMD: bool
    AGIDBEEINDE: int
    ODCMKOFFKKL: int
    DMCCAJMCFPA: int
    def __init__(self, DKOAGLJAAFA: _Optional[_Iterable[_Union[_LNCNFMEIOLI_pb2.LNCNFMEIOLI, _Mapping]]] = ..., KNGJHMLLCNP: _Optional[int] = ..., FADINCNPBMD: bool = ..., AGIDBEEINDE: _Optional[int] = ..., ODCMKOFFKKL: _Optional[int] = ..., DMCCAJMCFPA: _Optional[int] = ...) -> None: ...
