from genshin.packet.proto import IPGDGIHPBEF_pb2 as _IPGDGIHPBEF_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OPGFGKJBNGE(_message.Message):
    __slots__ = ("LDMGHBOAEPN", "EJNINFFFKJP", "DNBEFLJLAMB")
    LDMGHBOAEPN_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    DNBEFLJLAMB_FIELD_NUMBER: _ClassVar[int]
    LDMGHBOAEPN: _containers.RepeatedCompositeFieldContainer[_IPGDGIHPBEF_pb2.IPGDGIHPBEF]
    EJNINFFFKJP: int
    DNBEFLJLAMB: int
    def __init__(self, LDMGHBOAEPN: _Optional[_Iterable[_Union[_IPGDGIHPBEF_pb2.IPGDGIHPBEF, _Mapping]]] = ..., EJNINFFFKJP: _Optional[int] = ..., DNBEFLJLAMB: _Optional[int] = ...) -> None: ...
