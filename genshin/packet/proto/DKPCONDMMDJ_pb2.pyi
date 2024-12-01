from genshin.packet.proto import MDKCMCIMNDG_pb2 as _MDKCMCIMNDG_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DKPCONDMMDJ(_message.Message):
    __slots__ = ("PGIBHCHLPDN", "KNGJHMLLCNP", "CKPHCAGONKG", "HCJFDJHILAM", "KAFHPLFLKNJ")
    PGIBHCHLPDN_FIELD_NUMBER: _ClassVar[int]
    KNGJHMLLCNP_FIELD_NUMBER: _ClassVar[int]
    CKPHCAGONKG_FIELD_NUMBER: _ClassVar[int]
    HCJFDJHILAM_FIELD_NUMBER: _ClassVar[int]
    KAFHPLFLKNJ_FIELD_NUMBER: _ClassVar[int]
    PGIBHCHLPDN: _containers.RepeatedCompositeFieldContainer[_MDKCMCIMNDG_pb2.MDKCMCIMNDG]
    KNGJHMLLCNP: int
    CKPHCAGONKG: int
    HCJFDJHILAM: bool
    KAFHPLFLKNJ: int
    def __init__(self, PGIBHCHLPDN: _Optional[_Iterable[_Union[_MDKCMCIMNDG_pb2.MDKCMCIMNDG, _Mapping]]] = ..., KNGJHMLLCNP: _Optional[int] = ..., CKPHCAGONKG: _Optional[int] = ..., HCJFDJHILAM: bool = ..., KAFHPLFLKNJ: _Optional[int] = ...) -> None: ...
