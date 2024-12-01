from genshin.packet.proto import NIJKANKIBLA_pb2 as _NIJKANKIBLA_pb2
from genshin.packet.proto import DCHLOBNGOMN_pb2 as _DCHLOBNGOMN_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GONNEBEHPCE(_message.Message):
    __slots__ = ("AKGOOIIBCOM", "PIIJCNNIECO")
    AKGOOIIBCOM_FIELD_NUMBER: _ClassVar[int]
    PIIJCNNIECO_FIELD_NUMBER: _ClassVar[int]
    AKGOOIIBCOM: _NIJKANKIBLA_pb2.NIJKANKIBLA
    PIIJCNNIECO: _containers.RepeatedCompositeFieldContainer[_DCHLOBNGOMN_pb2.DCHLOBNGOMN]
    def __init__(self, AKGOOIIBCOM: _Optional[_Union[_NIJKANKIBLA_pb2.NIJKANKIBLA, _Mapping]] = ..., PIIJCNNIECO: _Optional[_Iterable[_Union[_DCHLOBNGOMN_pb2.DCHLOBNGOMN, _Mapping]]] = ...) -> None: ...
