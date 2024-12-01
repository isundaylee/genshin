from genshin.packet.proto import BMKEDDJHKNE_pb2 as _BMKEDDJHKNE_pb2
from genshin.packet.proto import HOBLMOAGLLH_pb2 as _HOBLMOAGLLH_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EKCPFLJAEHC(_message.Message):
    __slots__ = ("FGFDLMIJBII", "CIFJLBPHIJG", "FADINCNPBMD", "KNGJHMLLCNP", "DMCCAJMCFPA", "AOEGKKAJEAN")
    FGFDLMIJBII_FIELD_NUMBER: _ClassVar[int]
    CIFJLBPHIJG_FIELD_NUMBER: _ClassVar[int]
    FADINCNPBMD_FIELD_NUMBER: _ClassVar[int]
    KNGJHMLLCNP_FIELD_NUMBER: _ClassVar[int]
    DMCCAJMCFPA_FIELD_NUMBER: _ClassVar[int]
    AOEGKKAJEAN_FIELD_NUMBER: _ClassVar[int]
    FGFDLMIJBII: _containers.RepeatedCompositeFieldContainer[_BMKEDDJHKNE_pb2.BMKEDDJHKNE]
    CIFJLBPHIJG: _containers.RepeatedCompositeFieldContainer[_HOBLMOAGLLH_pb2.HOBLMOAGLLH]
    FADINCNPBMD: bool
    KNGJHMLLCNP: int
    DMCCAJMCFPA: int
    AOEGKKAJEAN: int
    def __init__(self, FGFDLMIJBII: _Optional[_Iterable[_Union[_BMKEDDJHKNE_pb2.BMKEDDJHKNE, _Mapping]]] = ..., CIFJLBPHIJG: _Optional[_Iterable[_Union[_HOBLMOAGLLH_pb2.HOBLMOAGLLH, _Mapping]]] = ..., FADINCNPBMD: bool = ..., KNGJHMLLCNP: _Optional[int] = ..., DMCCAJMCFPA: _Optional[int] = ..., AOEGKKAJEAN: _Optional[int] = ...) -> None: ...
