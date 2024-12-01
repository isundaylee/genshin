from genshin.packet.proto import HGMNLAGDFDC_pb2 as _HGMNLAGDFDC_pb2
from genshin.packet.proto import KBDGJPCLCHJ_pb2 as _KBDGJPCLCHJ_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MLMKBICHNOG(_message.Message):
    __slots__ = ("KABODNMEGEK", "PDHEKMEMBLG", "OMHFBICMGIA", "GHIHAIDBACF", "NEKECFNAHOM", "BAADLABMPDJ", "GOEGMOIBFCL", "LIBNHFHEFBF", "AEKAGEEBAAA", "HPMGHMCEDDP")
    KABODNMEGEK_FIELD_NUMBER: _ClassVar[int]
    PDHEKMEMBLG_FIELD_NUMBER: _ClassVar[int]
    OMHFBICMGIA_FIELD_NUMBER: _ClassVar[int]
    GHIHAIDBACF_FIELD_NUMBER: _ClassVar[int]
    NEKECFNAHOM_FIELD_NUMBER: _ClassVar[int]
    BAADLABMPDJ_FIELD_NUMBER: _ClassVar[int]
    GOEGMOIBFCL_FIELD_NUMBER: _ClassVar[int]
    LIBNHFHEFBF_FIELD_NUMBER: _ClassVar[int]
    AEKAGEEBAAA_FIELD_NUMBER: _ClassVar[int]
    HPMGHMCEDDP_FIELD_NUMBER: _ClassVar[int]
    KABODNMEGEK: _containers.RepeatedCompositeFieldContainer[_HGMNLAGDFDC_pb2.HGMNLAGDFDC]
    PDHEKMEMBLG: _containers.RepeatedScalarFieldContainer[int]
    OMHFBICMGIA: _KBDGJPCLCHJ_pb2.KBDGJPCLCHJ
    GHIHAIDBACF: _KBDGJPCLCHJ_pb2.KBDGJPCLCHJ
    NEKECFNAHOM: int
    BAADLABMPDJ: int
    GOEGMOIBFCL: int
    LIBNHFHEFBF: int
    AEKAGEEBAAA: int
    HPMGHMCEDDP: int
    def __init__(self, KABODNMEGEK: _Optional[_Iterable[_Union[_HGMNLAGDFDC_pb2.HGMNLAGDFDC, _Mapping]]] = ..., PDHEKMEMBLG: _Optional[_Iterable[int]] = ..., OMHFBICMGIA: _Optional[_Union[_KBDGJPCLCHJ_pb2.KBDGJPCLCHJ, _Mapping]] = ..., GHIHAIDBACF: _Optional[_Union[_KBDGJPCLCHJ_pb2.KBDGJPCLCHJ, _Mapping]] = ..., NEKECFNAHOM: _Optional[int] = ..., BAADLABMPDJ: _Optional[int] = ..., GOEGMOIBFCL: _Optional[int] = ..., LIBNHFHEFBF: _Optional[int] = ..., AEKAGEEBAAA: _Optional[int] = ..., HPMGHMCEDDP: _Optional[int] = ...) -> None: ...
