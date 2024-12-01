from genshin.packet.proto import BBIKBHKDNPI_pb2 as _BBIKBHKDNPI_pb2
from genshin.packet.proto import DDGPFNOPLFF_pb2 as _DDGPFNOPLFF_pb2
from genshin.packet.proto import HEBABGNPNLK_pb2 as _HEBABGNPNLK_pb2
from genshin.packet.proto import EHHKCFAFJFD_pb2 as _EHHKCFAFJFD_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ADELHEACCBC(_message.Message):
    __slots__ = ("OAMEBDNHEDB", "HOBAIDKKPLG", "ELBCGLMHDIL", "LPCDPIIMLPO", "JIECNLEMKBD", "GIANJMCBAEC")
    OAMEBDNHEDB_FIELD_NUMBER: _ClassVar[int]
    HOBAIDKKPLG_FIELD_NUMBER: _ClassVar[int]
    ELBCGLMHDIL_FIELD_NUMBER: _ClassVar[int]
    LPCDPIIMLPO_FIELD_NUMBER: _ClassVar[int]
    JIECNLEMKBD_FIELD_NUMBER: _ClassVar[int]
    GIANJMCBAEC_FIELD_NUMBER: _ClassVar[int]
    OAMEBDNHEDB: _BBIKBHKDNPI_pb2.BBIKBHKDNPI
    HOBAIDKKPLG: _containers.RepeatedScalarFieldContainer[int]
    ELBCGLMHDIL: _containers.RepeatedCompositeFieldContainer[_DDGPFNOPLFF_pb2.DDGPFNOPLFF]
    LPCDPIIMLPO: _containers.RepeatedCompositeFieldContainer[_HEBABGNPNLK_pb2.HEBABGNPNLK]
    JIECNLEMKBD: _containers.RepeatedCompositeFieldContainer[_EHHKCFAFJFD_pb2.EHHKCFAFJFD]
    GIANJMCBAEC: bool
    def __init__(self, OAMEBDNHEDB: _Optional[_Union[_BBIKBHKDNPI_pb2.BBIKBHKDNPI, _Mapping]] = ..., HOBAIDKKPLG: _Optional[_Iterable[int]] = ..., ELBCGLMHDIL: _Optional[_Iterable[_Union[_DDGPFNOPLFF_pb2.DDGPFNOPLFF, _Mapping]]] = ..., LPCDPIIMLPO: _Optional[_Iterable[_Union[_HEBABGNPNLK_pb2.HEBABGNPNLK, _Mapping]]] = ..., JIECNLEMKBD: _Optional[_Iterable[_Union[_EHHKCFAFJFD_pb2.EHHKCFAFJFD, _Mapping]]] = ..., GIANJMCBAEC: bool = ...) -> None: ...
