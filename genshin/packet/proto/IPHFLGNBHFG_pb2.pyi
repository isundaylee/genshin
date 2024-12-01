from genshin.packet.proto import ELCBGECGEON_pb2 as _ELCBGECGEON_pb2
from genshin.packet.proto import BLPMIJEPGLF_pb2 as _BLPMIJEPGLF_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IPHFLGNBHFG(_message.Message):
    __slots__ = ("HPODKDCCIKJ", "KCKEPCMLIHI", "PGDGNMGCEKM", "MPFLDFDOGAI")
    HPODKDCCIKJ_FIELD_NUMBER: _ClassVar[int]
    KCKEPCMLIHI_FIELD_NUMBER: _ClassVar[int]
    PGDGNMGCEKM_FIELD_NUMBER: _ClassVar[int]
    MPFLDFDOGAI_FIELD_NUMBER: _ClassVar[int]
    HPODKDCCIKJ: _ELCBGECGEON_pb2.ELCBGECGEON
    KCKEPCMLIHI: _containers.RepeatedCompositeFieldContainer[_BLPMIJEPGLF_pb2.BLPMIJEPGLF]
    PGDGNMGCEKM: bool
    MPFLDFDOGAI: bool
    def __init__(self, HPODKDCCIKJ: _Optional[_Union[_ELCBGECGEON_pb2.ELCBGECGEON, _Mapping]] = ..., KCKEPCMLIHI: _Optional[_Iterable[_Union[_BLPMIJEPGLF_pb2.BLPMIJEPGLF, _Mapping]]] = ..., PGDGNMGCEKM: bool = ..., MPFLDFDOGAI: bool = ...) -> None: ...
