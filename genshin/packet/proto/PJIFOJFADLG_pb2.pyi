from genshin.packet.proto import JNMHJONHLAG_pb2 as _JNMHJONHLAG_pb2
from genshin.packet.proto import JGCFLHEDIHI_pb2 as _JGCFLHEDIHI_pb2
from genshin.packet.proto import JNKEECKNOML_pb2 as _JNKEECKNOML_pb2
from genshin.packet.proto import CCACIDNDCCG_pb2 as _CCACIDNDCCG_pb2
from genshin.packet.proto import JLEPAAJFICN_pb2 as _JLEPAAJFICN_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PJIFOJFADLG(_message.Message):
    __slots__ = ("GMCBENMCOKN", "CBPAGDLIMIJ", "LJCDEEFBFML", "PMAPHNFNCPK", "EALJHPFDEHK", "EHAEACFBOOL", "HLKDDNGCKJN", "GHGOAAGEINH", "JBMEBKOANNI", "FMOIOMLDAJK", "GOPNNJPCJPL", "GNIDOHFPMJF", "BGOJIMJJCMD", "FDOGNIGLFLI", "fish_info", "fishtank_fish_info", "HPPJPFPAGMF", "HDHDDMPKLJH", "BNGPKPJNMCG", "OHCHPMIFDHG", "JFEKDNOGNKO", "KBNHDNPJJBH", "IAEOLKGPEOE", "AJDEBOBKBDE")
    class CBPAGDLIMIJEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    GMCBENMCOKN_FIELD_NUMBER: _ClassVar[int]
    CBPAGDLIMIJ_FIELD_NUMBER: _ClassVar[int]
    LJCDEEFBFML_FIELD_NUMBER: _ClassVar[int]
    PMAPHNFNCPK_FIELD_NUMBER: _ClassVar[int]
    EALJHPFDEHK_FIELD_NUMBER: _ClassVar[int]
    EHAEACFBOOL_FIELD_NUMBER: _ClassVar[int]
    HLKDDNGCKJN_FIELD_NUMBER: _ClassVar[int]
    GHGOAAGEINH_FIELD_NUMBER: _ClassVar[int]
    JBMEBKOANNI_FIELD_NUMBER: _ClassVar[int]
    FMOIOMLDAJK_FIELD_NUMBER: _ClassVar[int]
    GOPNNJPCJPL_FIELD_NUMBER: _ClassVar[int]
    GNIDOHFPMJF_FIELD_NUMBER: _ClassVar[int]
    BGOJIMJJCMD_FIELD_NUMBER: _ClassVar[int]
    FDOGNIGLFLI_FIELD_NUMBER: _ClassVar[int]
    FISH_INFO_FIELD_NUMBER: _ClassVar[int]
    FISHTANK_FISH_INFO_FIELD_NUMBER: _ClassVar[int]
    HPPJPFPAGMF_FIELD_NUMBER: _ClassVar[int]
    HDHDDMPKLJH_FIELD_NUMBER: _ClassVar[int]
    BNGPKPJNMCG_FIELD_NUMBER: _ClassVar[int]
    OHCHPMIFDHG_FIELD_NUMBER: _ClassVar[int]
    JFEKDNOGNKO_FIELD_NUMBER: _ClassVar[int]
    KBNHDNPJJBH_FIELD_NUMBER: _ClassVar[int]
    IAEOLKGPEOE_FIELD_NUMBER: _ClassVar[int]
    AJDEBOBKBDE_FIELD_NUMBER: _ClassVar[int]
    GMCBENMCOKN: _containers.RepeatedCompositeFieldContainer[_JNMHJONHLAG_pb2.JNMHJONHLAG]
    CBPAGDLIMIJ: _containers.ScalarMap[int, int]
    LJCDEEFBFML: _containers.RepeatedScalarFieldContainer[int]
    PMAPHNFNCPK: _JGCFLHEDIHI_pb2.JGCFLHEDIHI
    EALJHPFDEHK: int
    EHAEACFBOOL: int
    HLKDDNGCKJN: int
    GHGOAAGEINH: int
    JBMEBKOANNI: int
    FMOIOMLDAJK: int
    GOPNNJPCJPL: int
    GNIDOHFPMJF: bool
    BGOJIMJJCMD: bool
    FDOGNIGLFLI: int
    fish_info: _JNKEECKNOML_pb2.JNKEECKNOML
    fishtank_fish_info: _CCACIDNDCCG_pb2.CCACIDNDCCG
    HPPJPFPAGMF: int
    HDHDDMPKLJH: int
    BNGPKPJNMCG: _JLEPAAJFICN_pb2.JLEPAAJFICN
    OHCHPMIFDHG: int
    JFEKDNOGNKO: int
    KBNHDNPJJBH: int
    IAEOLKGPEOE: int
    AJDEBOBKBDE: int
    def __init__(self, GMCBENMCOKN: _Optional[_Iterable[_Union[_JNMHJONHLAG_pb2.JNMHJONHLAG, _Mapping]]] = ..., CBPAGDLIMIJ: _Optional[_Mapping[int, int]] = ..., LJCDEEFBFML: _Optional[_Iterable[int]] = ..., PMAPHNFNCPK: _Optional[_Union[_JGCFLHEDIHI_pb2.JGCFLHEDIHI, _Mapping]] = ..., EALJHPFDEHK: _Optional[int] = ..., EHAEACFBOOL: _Optional[int] = ..., HLKDDNGCKJN: _Optional[int] = ..., GHGOAAGEINH: _Optional[int] = ..., JBMEBKOANNI: _Optional[int] = ..., FMOIOMLDAJK: _Optional[int] = ..., GOPNNJPCJPL: _Optional[int] = ..., GNIDOHFPMJF: bool = ..., BGOJIMJJCMD: bool = ..., FDOGNIGLFLI: _Optional[int] = ..., fish_info: _Optional[_Union[_JNKEECKNOML_pb2.JNKEECKNOML, _Mapping]] = ..., fishtank_fish_info: _Optional[_Union[_CCACIDNDCCG_pb2.CCACIDNDCCG, _Mapping]] = ..., HPPJPFPAGMF: _Optional[int] = ..., HDHDDMPKLJH: _Optional[int] = ..., BNGPKPJNMCG: _Optional[_Union[_JLEPAAJFICN_pb2.JLEPAAJFICN, str]] = ..., OHCHPMIFDHG: _Optional[int] = ..., JFEKDNOGNKO: _Optional[int] = ..., KBNHDNPJJBH: _Optional[int] = ..., IAEOLKGPEOE: _Optional[int] = ..., AJDEBOBKBDE: _Optional[int] = ...) -> None: ...
