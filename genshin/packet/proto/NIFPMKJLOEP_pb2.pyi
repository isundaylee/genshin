from genshin.packet.proto import HKPGNGDDOCL_pb2 as _HKPGNGDDOCL_pb2
from genshin.packet.proto import OMBEIFNNEDF_pb2 as _OMBEIFNNEDF_pb2
from genshin.packet.proto import LJCNGNGDGPH_pb2 as _LJCNGNGDGPH_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NIFPMKJLOEP(_message.Message):
    __slots__ = ("EAKIHPFACDD", "AGCILNPMBLB", "KOCMCNGDDJG", "OLDJACGPADP")
    EAKIHPFACDD_FIELD_NUMBER: _ClassVar[int]
    AGCILNPMBLB_FIELD_NUMBER: _ClassVar[int]
    KOCMCNGDDJG_FIELD_NUMBER: _ClassVar[int]
    OLDJACGPADP_FIELD_NUMBER: _ClassVar[int]
    EAKIHPFACDD: _HKPGNGDDOCL_pb2.HKPGNGDDOCL
    AGCILNPMBLB: _containers.RepeatedCompositeFieldContainer[_OMBEIFNNEDF_pb2.OMBEIFNNEDF]
    KOCMCNGDDJG: _LJCNGNGDGPH_pb2.LJCNGNGDGPH
    OLDJACGPADP: _LJCNGNGDGPH_pb2.LJCNGNGDGPH
    def __init__(self, EAKIHPFACDD: _Optional[_Union[_HKPGNGDDOCL_pb2.HKPGNGDDOCL, _Mapping]] = ..., AGCILNPMBLB: _Optional[_Iterable[_Union[_OMBEIFNNEDF_pb2.OMBEIFNNEDF, _Mapping]]] = ..., KOCMCNGDDJG: _Optional[_Union[_LJCNGNGDGPH_pb2.LJCNGNGDGPH, str]] = ..., OLDJACGPADP: _Optional[_Union[_LJCNGNGDGPH_pb2.LJCNGNGDGPH, str]] = ...) -> None: ...
