from genshin.packet.proto import MKBMDCGMIEO_pb2 as _MKBMDCGMIEO_pb2
from genshin.packet.proto import PGANMGPELLD_pb2 as _PGANMGPELLD_pb2
from genshin.packet.proto import HEKGHBFOMII_pb2 as _HEKGHBFOMII_pb2
from genshin.packet.proto import KNDFJAGILPI_pb2 as _KNDFJAGILPI_pb2
from genshin.packet.proto import MMCBILLJLMK_pb2 as _MMCBILLJLMK_pb2
from genshin.packet.proto import PBDBFHJJLPB_pb2 as _PBDBFHJJLPB_pb2
from genshin.packet.proto import KAMDLKCMHIE_pb2 as _KAMDLKCMHIE_pb2
from genshin.packet.proto import GBJBJKBNEKE_pb2 as _GBJBJKBNEKE_pb2
from genshin.packet.proto import HNAICNEALFH_pb2 as _HNAICNEALFH_pb2
from genshin.packet.proto import EBLCBLOFAHH_pb2 as _EBLCBLOFAHH_pb2
from genshin.packet.proto import BECBKBINEBD_pb2 as _BECBKBINEBD_pb2
from genshin.packet.proto import NLOBHEMPBEM_pb2 as _NLOBHEMPBEM_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EPJOPBFFLFL(_message.Message):
    __slots__ = ("MALLFFAJNBM", "OAOPAOOMIPB", "OEBNEEAGHIN", "PHCIDGFOBBA", "EGFCEEDEEIK", "PCHJNHFOIEM", "LOOGLCJLADB", "OMFEHMJIBEF", "NLGCBMLFLLE", "OHANFELAMAE", "DJKOIAMLECB", "JDPOHCKAOAH", "JAHPPELNEDF", "NEGCKMBALPM", "AAEHPGKINOP", "IGCFEKLJNMJ", "FBNLOHMDNHD", "KONANKACIEM", "OGAHNCEGFOL", "BFPLMLGJBJP", "HKEGEBJNJJD", "CGJMPOCGLJC", "OOIPGFEDJMN")
    class OHANFELAMAEEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _HNAICNEALFH_pb2.HNAICNEALFH
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_HNAICNEALFH_pb2.HNAICNEALFH, _Mapping]] = ...) -> None: ...
    MALLFFAJNBM_FIELD_NUMBER: _ClassVar[int]
    OAOPAOOMIPB_FIELD_NUMBER: _ClassVar[int]
    OEBNEEAGHIN_FIELD_NUMBER: _ClassVar[int]
    PHCIDGFOBBA_FIELD_NUMBER: _ClassVar[int]
    EGFCEEDEEIK_FIELD_NUMBER: _ClassVar[int]
    PCHJNHFOIEM_FIELD_NUMBER: _ClassVar[int]
    LOOGLCJLADB_FIELD_NUMBER: _ClassVar[int]
    OMFEHMJIBEF_FIELD_NUMBER: _ClassVar[int]
    NLGCBMLFLLE_FIELD_NUMBER: _ClassVar[int]
    OHANFELAMAE_FIELD_NUMBER: _ClassVar[int]
    DJKOIAMLECB_FIELD_NUMBER: _ClassVar[int]
    JDPOHCKAOAH_FIELD_NUMBER: _ClassVar[int]
    JAHPPELNEDF_FIELD_NUMBER: _ClassVar[int]
    NEGCKMBALPM_FIELD_NUMBER: _ClassVar[int]
    AAEHPGKINOP_FIELD_NUMBER: _ClassVar[int]
    IGCFEKLJNMJ_FIELD_NUMBER: _ClassVar[int]
    FBNLOHMDNHD_FIELD_NUMBER: _ClassVar[int]
    KONANKACIEM_FIELD_NUMBER: _ClassVar[int]
    OGAHNCEGFOL_FIELD_NUMBER: _ClassVar[int]
    BFPLMLGJBJP_FIELD_NUMBER: _ClassVar[int]
    HKEGEBJNJJD_FIELD_NUMBER: _ClassVar[int]
    CGJMPOCGLJC_FIELD_NUMBER: _ClassVar[int]
    OOIPGFEDJMN_FIELD_NUMBER: _ClassVar[int]
    MALLFFAJNBM: _containers.RepeatedCompositeFieldContainer[_MKBMDCGMIEO_pb2.MKBMDCGMIEO]
    OAOPAOOMIPB: _containers.RepeatedScalarFieldContainer[int]
    OEBNEEAGHIN: _containers.RepeatedCompositeFieldContainer[_PGANMGPELLD_pb2.PGANMGPELLD]
    PHCIDGFOBBA: _HEKGHBFOMII_pb2.HEKGHBFOMII
    EGFCEEDEEIK: _containers.RepeatedCompositeFieldContainer[_KNDFJAGILPI_pb2.KNDFJAGILPI]
    PCHJNHFOIEM: _MMCBILLJLMK_pb2.MMCBILLJLMK
    LOOGLCJLADB: _containers.RepeatedCompositeFieldContainer[_PBDBFHJJLPB_pb2.PBDBFHJJLPB]
    OMFEHMJIBEF: _containers.RepeatedCompositeFieldContainer[_KAMDLKCMHIE_pb2.KAMDLKCMHIE]
    NLGCBMLFLLE: _containers.RepeatedCompositeFieldContainer[_GBJBJKBNEKE_pb2.GBJBJKBNEKE]
    OHANFELAMAE: _containers.MessageMap[int, _HNAICNEALFH_pb2.HNAICNEALFH]
    DJKOIAMLECB: _containers.RepeatedCompositeFieldContainer[_EBLCBLOFAHH_pb2.EBLCBLOFAHH]
    JDPOHCKAOAH: _containers.RepeatedScalarFieldContainer[int]
    JAHPPELNEDF: _containers.RepeatedCompositeFieldContainer[_MKBMDCGMIEO_pb2.MKBMDCGMIEO]
    NEGCKMBALPM: _containers.RepeatedCompositeFieldContainer[_BECBKBINEBD_pb2.BECBKBINEBD]
    AAEHPGKINOP: _containers.RepeatedCompositeFieldContainer[_EBLCBLOFAHH_pb2.EBLCBLOFAHH]
    IGCFEKLJNMJ: _NLOBHEMPBEM_pb2.NLOBHEMPBEM
    FBNLOHMDNHD: int
    KONANKACIEM: int
    OGAHNCEGFOL: bool
    BFPLMLGJBJP: int
    HKEGEBJNJJD: int
    CGJMPOCGLJC: int
    OOIPGFEDJMN: int
    def __init__(self, MALLFFAJNBM: _Optional[_Iterable[_Union[_MKBMDCGMIEO_pb2.MKBMDCGMIEO, _Mapping]]] = ..., OAOPAOOMIPB: _Optional[_Iterable[int]] = ..., OEBNEEAGHIN: _Optional[_Iterable[_Union[_PGANMGPELLD_pb2.PGANMGPELLD, _Mapping]]] = ..., PHCIDGFOBBA: _Optional[_Union[_HEKGHBFOMII_pb2.HEKGHBFOMII, _Mapping]] = ..., EGFCEEDEEIK: _Optional[_Iterable[_Union[_KNDFJAGILPI_pb2.KNDFJAGILPI, _Mapping]]] = ..., PCHJNHFOIEM: _Optional[_Union[_MMCBILLJLMK_pb2.MMCBILLJLMK, _Mapping]] = ..., LOOGLCJLADB: _Optional[_Iterable[_Union[_PBDBFHJJLPB_pb2.PBDBFHJJLPB, _Mapping]]] = ..., OMFEHMJIBEF: _Optional[_Iterable[_Union[_KAMDLKCMHIE_pb2.KAMDLKCMHIE, _Mapping]]] = ..., NLGCBMLFLLE: _Optional[_Iterable[_Union[_GBJBJKBNEKE_pb2.GBJBJKBNEKE, _Mapping]]] = ..., OHANFELAMAE: _Optional[_Mapping[int, _HNAICNEALFH_pb2.HNAICNEALFH]] = ..., DJKOIAMLECB: _Optional[_Iterable[_Union[_EBLCBLOFAHH_pb2.EBLCBLOFAHH, _Mapping]]] = ..., JDPOHCKAOAH: _Optional[_Iterable[int]] = ..., JAHPPELNEDF: _Optional[_Iterable[_Union[_MKBMDCGMIEO_pb2.MKBMDCGMIEO, _Mapping]]] = ..., NEGCKMBALPM: _Optional[_Iterable[_Union[_BECBKBINEBD_pb2.BECBKBINEBD, _Mapping]]] = ..., AAEHPGKINOP: _Optional[_Iterable[_Union[_EBLCBLOFAHH_pb2.EBLCBLOFAHH, _Mapping]]] = ..., IGCFEKLJNMJ: _Optional[_Union[_NLOBHEMPBEM_pb2.NLOBHEMPBEM, str]] = ..., FBNLOHMDNHD: _Optional[int] = ..., KONANKACIEM: _Optional[int] = ..., OGAHNCEGFOL: bool = ..., BFPLMLGJBJP: _Optional[int] = ..., HKEGEBJNJJD: _Optional[int] = ..., CGJMPOCGLJC: _Optional[int] = ..., OOIPGFEDJMN: _Optional[int] = ...) -> None: ...
