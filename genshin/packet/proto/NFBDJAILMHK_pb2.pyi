from genshin.packet.proto import OJPKAGFJMMM_pb2 as _OJPKAGFJMMM_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NFBDJAILMHK(_message.Message):
    __slots__ = ("BDEFOIGANGN", "EEMCCMNECKN", "EKHENCACHJM", "OKGALCDAPFD", "DMCCAJMCFPA")
    BDEFOIGANGN_FIELD_NUMBER: _ClassVar[int]
    EEMCCMNECKN_FIELD_NUMBER: _ClassVar[int]
    EKHENCACHJM_FIELD_NUMBER: _ClassVar[int]
    OKGALCDAPFD_FIELD_NUMBER: _ClassVar[int]
    DMCCAJMCFPA_FIELD_NUMBER: _ClassVar[int]
    BDEFOIGANGN: _containers.RepeatedCompositeFieldContainer[_OJPKAGFJMMM_pb2.OJPKAGFJMMM]
    EEMCCMNECKN: str
    EKHENCACHJM: bool
    OKGALCDAPFD: bool
    DMCCAJMCFPA: int
    def __init__(self, BDEFOIGANGN: _Optional[_Iterable[_Union[_OJPKAGFJMMM_pb2.OJPKAGFJMMM, _Mapping]]] = ..., EEMCCMNECKN: _Optional[str] = ..., EKHENCACHJM: bool = ..., OKGALCDAPFD: bool = ..., DMCCAJMCFPA: _Optional[int] = ...) -> None: ...
