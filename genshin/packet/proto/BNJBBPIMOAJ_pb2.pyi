from genshin.packet.proto import ENEBCPJJPHN_pb2 as _ENEBCPJJPHN_pb2
from genshin.packet.proto import OLHEKLKENDN_pb2 as _OLHEKLKENDN_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BNJBBPIMOAJ(_message.Message):
    __slots__ = ("PDHEKMEMBLG", "JJMKPFHJKGK", "KABODNMEGEK")
    PDHEKMEMBLG_FIELD_NUMBER: _ClassVar[int]
    JJMKPFHJKGK_FIELD_NUMBER: _ClassVar[int]
    KABODNMEGEK_FIELD_NUMBER: _ClassVar[int]
    PDHEKMEMBLG: _containers.RepeatedScalarFieldContainer[int]
    JJMKPFHJKGK: _containers.RepeatedCompositeFieldContainer[_ENEBCPJJPHN_pb2.ENEBCPJJPHN]
    KABODNMEGEK: _containers.RepeatedCompositeFieldContainer[_OLHEKLKENDN_pb2.OLHEKLKENDN]
    def __init__(self, PDHEKMEMBLG: _Optional[_Iterable[int]] = ..., JJMKPFHJKGK: _Optional[_Iterable[_Union[_ENEBCPJJPHN_pb2.ENEBCPJJPHN, _Mapping]]] = ..., KABODNMEGEK: _Optional[_Iterable[_Union[_OLHEKLKENDN_pb2.OLHEKLKENDN, _Mapping]]] = ...) -> None: ...
