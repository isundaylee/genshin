from genshin.packet.proto import GPIDAGCKPFO_pb2 as _GPIDAGCKPFO_pb2
from genshin.packet.proto import NAJEPFPOEDA_pb2 as _NAJEPFPOEDA_pb2
from genshin.packet.proto import JOKPHKNIFID_pb2 as _JOKPHKNIFID_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BCBDFLGIOCC(_message.Message):
    __slots__ = ("HBDGGIDECMD", "EDDADHKHEBI", "DBAIDABICMG", "KGMFMFGLLKA", "IHIDIODDKFB", "instanced_modifier_id", "instanced_ability_id", "KOFHAGBKGPD")
    HBDGGIDECMD_FIELD_NUMBER: _ClassVar[int]
    EDDADHKHEBI_FIELD_NUMBER: _ClassVar[int]
    DBAIDABICMG_FIELD_NUMBER: _ClassVar[int]
    KGMFMFGLLKA_FIELD_NUMBER: _ClassVar[int]
    IHIDIODDKFB_FIELD_NUMBER: _ClassVar[int]
    INSTANCED_MODIFIER_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCED_ABILITY_ID_FIELD_NUMBER: _ClassVar[int]
    KOFHAGBKGPD_FIELD_NUMBER: _ClassVar[int]
    HBDGGIDECMD: _containers.RepeatedScalarFieldContainer[int]
    EDDADHKHEBI: _GPIDAGCKPFO_pb2.GPIDAGCKPFO
    DBAIDABICMG: _NAJEPFPOEDA_pb2.NAJEPFPOEDA
    KGMFMFGLLKA: _containers.RepeatedCompositeFieldContainer[_JOKPHKNIFID_pb2.JOKPHKNIFID]
    IHIDIODDKFB: bool
    instanced_modifier_id: int
    instanced_ability_id: int
    KOFHAGBKGPD: int
    def __init__(self, HBDGGIDECMD: _Optional[_Iterable[int]] = ..., EDDADHKHEBI: _Optional[_Union[_GPIDAGCKPFO_pb2.GPIDAGCKPFO, _Mapping]] = ..., DBAIDABICMG: _Optional[_Union[_NAJEPFPOEDA_pb2.NAJEPFPOEDA, _Mapping]] = ..., KGMFMFGLLKA: _Optional[_Iterable[_Union[_JOKPHKNIFID_pb2.JOKPHKNIFID, _Mapping]]] = ..., IHIDIODDKFB: bool = ..., instanced_modifier_id: _Optional[int] = ..., instanced_ability_id: _Optional[int] = ..., KOFHAGBKGPD: _Optional[int] = ...) -> None: ...
