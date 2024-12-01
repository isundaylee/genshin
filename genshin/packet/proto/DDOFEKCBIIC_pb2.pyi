from genshin.packet.proto import CHOMFEMEHNL_pb2 as _CHOMFEMEHNL_pb2
from genshin.packet.proto import CBMCENPMIHI_pb2 as _CBMCENPMIHI_pb2
from genshin.packet.proto import CDFINADPJAP_pb2 as _CDFINADPJAP_pb2
from genshin.packet.proto import IGCDEHPIIFM_pb2 as _IGCDEHPIIFM_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DDOFEKCBIIC(_message.Message):
    __slots__ = ("MJDAOHHPPPC", "ALGJNHEGPNI", "PCIBMJMPABH", "MKIFGEHEBLD", "KAPJLOMCDNG", "GGDBALONGIN", "PJGKHFMLCIN", "MLGFPGIDGNO", "KNFOKPOMCCK", "PMJLLLFOPHK", "IKPEPKAHABM", "GHJAFBKDIDN", "DBFGJNBBDKC", "DIJCHGHPAEE", "PKHKGDHGHPA")
    class MJDAOHHPPPCEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    MJDAOHHPPPC_FIELD_NUMBER: _ClassVar[int]
    ALGJNHEGPNI_FIELD_NUMBER: _ClassVar[int]
    PCIBMJMPABH_FIELD_NUMBER: _ClassVar[int]
    MKIFGEHEBLD_FIELD_NUMBER: _ClassVar[int]
    KAPJLOMCDNG_FIELD_NUMBER: _ClassVar[int]
    GGDBALONGIN_FIELD_NUMBER: _ClassVar[int]
    PJGKHFMLCIN_FIELD_NUMBER: _ClassVar[int]
    MLGFPGIDGNO_FIELD_NUMBER: _ClassVar[int]
    KNFOKPOMCCK_FIELD_NUMBER: _ClassVar[int]
    PMJLLLFOPHK_FIELD_NUMBER: _ClassVar[int]
    IKPEPKAHABM_FIELD_NUMBER: _ClassVar[int]
    GHJAFBKDIDN_FIELD_NUMBER: _ClassVar[int]
    DBFGJNBBDKC_FIELD_NUMBER: _ClassVar[int]
    DIJCHGHPAEE_FIELD_NUMBER: _ClassVar[int]
    PKHKGDHGHPA_FIELD_NUMBER: _ClassVar[int]
    MJDAOHHPPPC: _containers.ScalarMap[int, int]
    ALGJNHEGPNI: _containers.RepeatedScalarFieldContainer[int]
    PCIBMJMPABH: _containers.RepeatedCompositeFieldContainer[_CHOMFEMEHNL_pb2.CHOMFEMEHNL]
    MKIFGEHEBLD: _containers.RepeatedCompositeFieldContainer[_CBMCENPMIHI_pb2.CBMCENPMIHI]
    KAPJLOMCDNG: _CDFINADPJAP_pb2.CDFINADPJAP
    GGDBALONGIN: _containers.RepeatedCompositeFieldContainer[_IGCDEHPIIFM_pb2.IGCDEHPIIFM]
    PJGKHFMLCIN: int
    MLGFPGIDGNO: int
    KNFOKPOMCCK: bool
    PMJLLLFOPHK: bool
    IKPEPKAHABM: bool
    GHJAFBKDIDN: bool
    DBFGJNBBDKC: int
    DIJCHGHPAEE: int
    PKHKGDHGHPA: int
    def __init__(self, MJDAOHHPPPC: _Optional[_Mapping[int, int]] = ..., ALGJNHEGPNI: _Optional[_Iterable[int]] = ..., PCIBMJMPABH: _Optional[_Iterable[_Union[_CHOMFEMEHNL_pb2.CHOMFEMEHNL, _Mapping]]] = ..., MKIFGEHEBLD: _Optional[_Iterable[_Union[_CBMCENPMIHI_pb2.CBMCENPMIHI, _Mapping]]] = ..., KAPJLOMCDNG: _Optional[_Union[_CDFINADPJAP_pb2.CDFINADPJAP, _Mapping]] = ..., GGDBALONGIN: _Optional[_Iterable[_Union[_IGCDEHPIIFM_pb2.IGCDEHPIIFM, _Mapping]]] = ..., PJGKHFMLCIN: _Optional[int] = ..., MLGFPGIDGNO: _Optional[int] = ..., KNFOKPOMCCK: bool = ..., PMJLLLFOPHK: bool = ..., IKPEPKAHABM: bool = ..., GHJAFBKDIDN: bool = ..., DBFGJNBBDKC: _Optional[int] = ..., DIJCHGHPAEE: _Optional[int] = ..., PKHKGDHGHPA: _Optional[int] = ...) -> None: ...
