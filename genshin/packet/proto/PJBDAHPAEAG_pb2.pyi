from genshin.packet.proto import MMHPCAJFFJG_pb2 as _MMHPCAJFFJG_pb2
from genshin.packet.proto import GDLFLFDGNGH_pb2 as _GDLFLFDGNGH_pb2
from genshin.packet.proto import NKFIFDHJBCC_pb2 as _NKFIFDHJBCC_pb2
from genshin.packet.proto import MEBCHBGNFFA_pb2 as _MEBCHBGNFFA_pb2
from genshin.packet.proto import DANPJHICHOM_pb2 as _DANPJHICHOM_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PJBDAHPAEAG(_message.Message):
    __slots__ = ("OHJNPJCKGEG", "CNONEIKAGEM", "HLGHFFFPNBB", "JFJKEDFAFPM", "ALCLFDJJCKO", "HOHOGGJOAOP", "FDEDHCEKMIP", "EAFDHPEENIM", "FNCCANHPBII", "PANJHFEHGLK", "GMCBMLCLAFD", "AMKNNJCJHCJ", "MMFHPEMPFNI", "NHHMOABAFHN", "APHAAHPDDJB", "MBILCOLCMMH", "KIPGKKMDAKN", "IOMJEPGMFBD", "GAMMCKBFPHM", "GHEJILPPKAL", "JJAFFHDCEFG", "PJLHHCIILFB", "DFHNPLKJGMF", "NGIOMIKNNCL", "MJBJNLOGJKA", "DHNKFDJHDBF", "PAKNLFOEBLB", "FPLLNPMLAIG", "OEENKBPDLCB", "DJCHBDAPKOB", "MFLNKIPGBHH", "EDMOCOCJPHH", "HANLNHAOFOM", "EJNINFFFKJP", "JJDJDFCEFCK", "IKCCNHPCMKL")
    class PANJHFEHGLKEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class GMCBMLCLAFDEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _NKFIFDHJBCC_pb2.NKFIFDHJBCC
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_NKFIFDHJBCC_pb2.NKFIFDHJBCC, _Mapping]] = ...) -> None: ...
    OHJNPJCKGEG_FIELD_NUMBER: _ClassVar[int]
    CNONEIKAGEM_FIELD_NUMBER: _ClassVar[int]
    HLGHFFFPNBB_FIELD_NUMBER: _ClassVar[int]
    JFJKEDFAFPM_FIELD_NUMBER: _ClassVar[int]
    ALCLFDJJCKO_FIELD_NUMBER: _ClassVar[int]
    HOHOGGJOAOP_FIELD_NUMBER: _ClassVar[int]
    FDEDHCEKMIP_FIELD_NUMBER: _ClassVar[int]
    EAFDHPEENIM_FIELD_NUMBER: _ClassVar[int]
    FNCCANHPBII_FIELD_NUMBER: _ClassVar[int]
    PANJHFEHGLK_FIELD_NUMBER: _ClassVar[int]
    GMCBMLCLAFD_FIELD_NUMBER: _ClassVar[int]
    AMKNNJCJHCJ_FIELD_NUMBER: _ClassVar[int]
    MMFHPEMPFNI_FIELD_NUMBER: _ClassVar[int]
    NHHMOABAFHN_FIELD_NUMBER: _ClassVar[int]
    APHAAHPDDJB_FIELD_NUMBER: _ClassVar[int]
    MBILCOLCMMH_FIELD_NUMBER: _ClassVar[int]
    KIPGKKMDAKN_FIELD_NUMBER: _ClassVar[int]
    IOMJEPGMFBD_FIELD_NUMBER: _ClassVar[int]
    GAMMCKBFPHM_FIELD_NUMBER: _ClassVar[int]
    GHEJILPPKAL_FIELD_NUMBER: _ClassVar[int]
    JJAFFHDCEFG_FIELD_NUMBER: _ClassVar[int]
    PJLHHCIILFB_FIELD_NUMBER: _ClassVar[int]
    DFHNPLKJGMF_FIELD_NUMBER: _ClassVar[int]
    NGIOMIKNNCL_FIELD_NUMBER: _ClassVar[int]
    MJBJNLOGJKA_FIELD_NUMBER: _ClassVar[int]
    DHNKFDJHDBF_FIELD_NUMBER: _ClassVar[int]
    PAKNLFOEBLB_FIELD_NUMBER: _ClassVar[int]
    FPLLNPMLAIG_FIELD_NUMBER: _ClassVar[int]
    OEENKBPDLCB_FIELD_NUMBER: _ClassVar[int]
    DJCHBDAPKOB_FIELD_NUMBER: _ClassVar[int]
    MFLNKIPGBHH_FIELD_NUMBER: _ClassVar[int]
    EDMOCOCJPHH_FIELD_NUMBER: _ClassVar[int]
    HANLNHAOFOM_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    JJDJDFCEFCK_FIELD_NUMBER: _ClassVar[int]
    IKCCNHPCMKL_FIELD_NUMBER: _ClassVar[int]
    OHJNPJCKGEG: str
    CNONEIKAGEM: _MMHPCAJFFJG_pb2.MMHPCAJFFJG
    HLGHFFFPNBB: str
    JFJKEDFAFPM: bytes
    ALCLFDJJCKO: _GDLFLFDGNGH_pb2.GDLFLFDGNGH
    HOHOGGJOAOP: str
    FDEDHCEKMIP: bytes
    EAFDHPEENIM: str
    FNCCANHPBII: str
    PANJHFEHGLK: _containers.ScalarMap[str, int]
    GMCBMLCLAFD: _containers.MessageMap[int, _NKFIFDHJBCC_pb2.NKFIFDHJBCC]
    AMKNNJCJHCJ: _containers.RepeatedCompositeFieldContainer[_MEBCHBGNFFA_pb2.MEBCHBGNFFA]
    MMFHPEMPFNI: _containers.RepeatedCompositeFieldContainer[_DANPJHICHOM_pb2.DANPJHICHOM]
    NHHMOABAFHN: str
    APHAAHPDDJB: str
    MBILCOLCMMH: _GDLFLFDGNGH_pb2.GDLFLFDGNGH
    KIPGKKMDAKN: str
    IOMJEPGMFBD: str
    GAMMCKBFPHM: str
    GHEJILPPKAL: int
    JJAFFHDCEFG: bool
    PJLHHCIILFB: bool
    DFHNPLKJGMF: bool
    NGIOMIKNNCL: bool
    MJBJNLOGJKA: bool
    DHNKFDJHDBF: bool
    PAKNLFOEBLB: int
    FPLLNPMLAIG: int
    OEENKBPDLCB: bool
    DJCHBDAPKOB: bool
    MFLNKIPGBHH: bool
    EDMOCOCJPHH: int
    HANLNHAOFOM: int
    EJNINFFFKJP: int
    JJDJDFCEFCK: int
    IKCCNHPCMKL: int
    def __init__(self, OHJNPJCKGEG: _Optional[str] = ..., CNONEIKAGEM: _Optional[_Union[_MMHPCAJFFJG_pb2.MMHPCAJFFJG, _Mapping]] = ..., HLGHFFFPNBB: _Optional[str] = ..., JFJKEDFAFPM: _Optional[bytes] = ..., ALCLFDJJCKO: _Optional[_Union[_GDLFLFDGNGH_pb2.GDLFLFDGNGH, _Mapping]] = ..., HOHOGGJOAOP: _Optional[str] = ..., FDEDHCEKMIP: _Optional[bytes] = ..., EAFDHPEENIM: _Optional[str] = ..., FNCCANHPBII: _Optional[str] = ..., PANJHFEHGLK: _Optional[_Mapping[str, int]] = ..., GMCBMLCLAFD: _Optional[_Mapping[int, _NKFIFDHJBCC_pb2.NKFIFDHJBCC]] = ..., AMKNNJCJHCJ: _Optional[_Iterable[_Union[_MEBCHBGNFFA_pb2.MEBCHBGNFFA, _Mapping]]] = ..., MMFHPEMPFNI: _Optional[_Iterable[_Union[_DANPJHICHOM_pb2.DANPJHICHOM, _Mapping]]] = ..., NHHMOABAFHN: _Optional[str] = ..., APHAAHPDDJB: _Optional[str] = ..., MBILCOLCMMH: _Optional[_Union[_GDLFLFDGNGH_pb2.GDLFLFDGNGH, _Mapping]] = ..., KIPGKKMDAKN: _Optional[str] = ..., IOMJEPGMFBD: _Optional[str] = ..., GAMMCKBFPHM: _Optional[str] = ..., GHEJILPPKAL: _Optional[int] = ..., JJAFFHDCEFG: bool = ..., PJLHHCIILFB: bool = ..., DFHNPLKJGMF: bool = ..., NGIOMIKNNCL: bool = ..., MJBJNLOGJKA: bool = ..., DHNKFDJHDBF: bool = ..., PAKNLFOEBLB: _Optional[int] = ..., FPLLNPMLAIG: _Optional[int] = ..., OEENKBPDLCB: bool = ..., DJCHBDAPKOB: bool = ..., MFLNKIPGBHH: bool = ..., EDMOCOCJPHH: _Optional[int] = ..., HANLNHAOFOM: _Optional[int] = ..., EJNINFFFKJP: _Optional[int] = ..., JJDJDFCEFCK: _Optional[int] = ..., IKCCNHPCMKL: _Optional[int] = ...) -> None: ...
