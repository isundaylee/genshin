from genshin.packet.proto import OLHEKLKENDN_pb2 as _OLHEKLKENDN_pb2
from genshin.packet.proto import PICCFJIDMML_pb2 as _PICCFJIDMML_pb2
from genshin.packet.proto import NLOBHEMPBEM_pb2 as _NLOBHEMPBEM_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CLCLPFGGOGM(_message.Message):
    __slots__ = ("FEHBKKPDBDI", "KABODNMEGEK", "JKNHPFOBGJB", "PJBBBIDPAJH", "KONANKACIEM", "IGCFEKLJNMJ", "NEKECFNAHOM")
    FEHBKKPDBDI_FIELD_NUMBER: _ClassVar[int]
    KABODNMEGEK_FIELD_NUMBER: _ClassVar[int]
    JKNHPFOBGJB_FIELD_NUMBER: _ClassVar[int]
    PJBBBIDPAJH_FIELD_NUMBER: _ClassVar[int]
    KONANKACIEM_FIELD_NUMBER: _ClassVar[int]
    IGCFEKLJNMJ_FIELD_NUMBER: _ClassVar[int]
    NEKECFNAHOM_FIELD_NUMBER: _ClassVar[int]
    FEHBKKPDBDI: _containers.RepeatedScalarFieldContainer[int]
    KABODNMEGEK: _containers.RepeatedCompositeFieldContainer[_OLHEKLKENDN_pb2.OLHEKLKENDN]
    JKNHPFOBGJB: _PICCFJIDMML_pb2.PICCFJIDMML
    PJBBBIDPAJH: int
    KONANKACIEM: int
    IGCFEKLJNMJ: _NLOBHEMPBEM_pb2.NLOBHEMPBEM
    NEKECFNAHOM: int
    def __init__(self, FEHBKKPDBDI: _Optional[_Iterable[int]] = ..., KABODNMEGEK: _Optional[_Iterable[_Union[_OLHEKLKENDN_pb2.OLHEKLKENDN, _Mapping]]] = ..., JKNHPFOBGJB: _Optional[_Union[_PICCFJIDMML_pb2.PICCFJIDMML, _Mapping]] = ..., PJBBBIDPAJH: _Optional[int] = ..., KONANKACIEM: _Optional[int] = ..., IGCFEKLJNMJ: _Optional[_Union[_NLOBHEMPBEM_pb2.NLOBHEMPBEM, str]] = ..., NEKECFNAHOM: _Optional[int] = ...) -> None: ...
