from genshin.packet.proto import KDEHCGJAGFJ_pb2 as _KDEHCGJAGFJ_pb2
from genshin.packet.proto import AHDCNHCIBNM_pb2 as _AHDCNHCIBNM_pb2
from genshin.packet.proto import LJLCAFOPOBK_pb2 as _LJLCAFOPOBK_pb2
from genshin.packet.proto import MAKGDPBEJIN_pb2 as _MAKGDPBEJIN_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class INOGIAJEMDE(_message.Message):
    __slots__ = ("DNAFLMMFFJN", "EDJNMLOINPA", "EHHEIAHALEL", "ANGHAMJLGIH", "EICGAABFBDO", "ECIFINMNLND", "BJLKIHFOKOF", "IGBDOEBPPHO")
    DNAFLMMFFJN_FIELD_NUMBER: _ClassVar[int]
    EDJNMLOINPA_FIELD_NUMBER: _ClassVar[int]
    EHHEIAHALEL_FIELD_NUMBER: _ClassVar[int]
    ANGHAMJLGIH_FIELD_NUMBER: _ClassVar[int]
    EICGAABFBDO_FIELD_NUMBER: _ClassVar[int]
    ECIFINMNLND_FIELD_NUMBER: _ClassVar[int]
    BJLKIHFOKOF_FIELD_NUMBER: _ClassVar[int]
    IGBDOEBPPHO_FIELD_NUMBER: _ClassVar[int]
    DNAFLMMFFJN: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    EDJNMLOINPA: _AHDCNHCIBNM_pb2.AHDCNHCIBNM
    EHHEIAHALEL: _LJLCAFOPOBK_pb2.LJLCAFOPOBK
    ANGHAMJLGIH: _containers.RepeatedCompositeFieldContainer[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ]
    EICGAABFBDO: _AHDCNHCIBNM_pb2.AHDCNHCIBNM
    ECIFINMNLND: int
    BJLKIHFOKOF: _MAKGDPBEJIN_pb2.MAKGDPBEJIN
    IGBDOEBPPHO: int
    def __init__(self, DNAFLMMFFJN: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., EDJNMLOINPA: _Optional[_Union[_AHDCNHCIBNM_pb2.AHDCNHCIBNM, _Mapping]] = ..., EHHEIAHALEL: _Optional[_Union[_LJLCAFOPOBK_pb2.LJLCAFOPOBK, _Mapping]] = ..., ANGHAMJLGIH: _Optional[_Iterable[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]]] = ..., EICGAABFBDO: _Optional[_Union[_AHDCNHCIBNM_pb2.AHDCNHCIBNM, _Mapping]] = ..., ECIFINMNLND: _Optional[int] = ..., BJLKIHFOKOF: _Optional[_Union[_MAKGDPBEJIN_pb2.MAKGDPBEJIN, str]] = ..., IGBDOEBPPHO: _Optional[int] = ...) -> None: ...
