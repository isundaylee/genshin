from genshin.packet.proto import DCNJGOKKPPC_pb2 as _DCNJGOKKPPC_pb2
from genshin.packet.proto import NIJKANKIBLA_pb2 as _NIJKANKIBLA_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BEOBFJDMCCJ(_message.Message):
    __slots__ = ("DLMMBBMOFAC", "AKGOOIIBCOM", "BMMBMCLKGMO")
    DLMMBBMOFAC_FIELD_NUMBER: _ClassVar[int]
    AKGOOIIBCOM_FIELD_NUMBER: _ClassVar[int]
    BMMBMCLKGMO_FIELD_NUMBER: _ClassVar[int]
    DLMMBBMOFAC: _DCNJGOKKPPC_pb2.DCNJGOKKPPC
    AKGOOIIBCOM: _NIJKANKIBLA_pb2.NIJKANKIBLA
    BMMBMCLKGMO: int
    def __init__(self, DLMMBBMOFAC: _Optional[_Union[_DCNJGOKKPPC_pb2.DCNJGOKKPPC, _Mapping]] = ..., AKGOOIIBCOM: _Optional[_Union[_NIJKANKIBLA_pb2.NIJKANKIBLA, _Mapping]] = ..., BMMBMCLKGMO: _Optional[int] = ...) -> None: ...
