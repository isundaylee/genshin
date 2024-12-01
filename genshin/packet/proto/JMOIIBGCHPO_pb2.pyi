from genshin.packet.proto import MEENBHFDNGJ_pb2 as _MEENBHFDNGJ_pb2
from genshin.packet.proto import DDIAKFFCPDH_pb2 as _DDIAKFFCPDH_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JMOIIBGCHPO(_message.Message):
    __slots__ = ("CKNAFCGJELM", "HAPPCAHNNJI", "PKHPCJOGDBB", "IPBOJDIJFKE", "EPFPAMGGPHK", "LNGHHDIABNK", "JPCFCAMDOOJ", "DFIDINDBNGM", "NKGDGKCIDJJ", "KFDINLFHFMK", "EAIPGEMKNPO", "OAJOOBGHAGM", "PHHAEFNLMGG", "OKBKPBLOPLN", "KHIHKMMNCMO", "EACCPEFBMMJ")
    class HAPPCAHNNJIEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _MEENBHFDNGJ_pb2.MEENBHFDNGJ
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_MEENBHFDNGJ_pb2.MEENBHFDNGJ, _Mapping]] = ...) -> None: ...
    CKNAFCGJELM_FIELD_NUMBER: _ClassVar[int]
    HAPPCAHNNJI_FIELD_NUMBER: _ClassVar[int]
    PKHPCJOGDBB_FIELD_NUMBER: _ClassVar[int]
    IPBOJDIJFKE_FIELD_NUMBER: _ClassVar[int]
    EPFPAMGGPHK_FIELD_NUMBER: _ClassVar[int]
    LNGHHDIABNK_FIELD_NUMBER: _ClassVar[int]
    JPCFCAMDOOJ_FIELD_NUMBER: _ClassVar[int]
    DFIDINDBNGM_FIELD_NUMBER: _ClassVar[int]
    NKGDGKCIDJJ_FIELD_NUMBER: _ClassVar[int]
    KFDINLFHFMK_FIELD_NUMBER: _ClassVar[int]
    EAIPGEMKNPO_FIELD_NUMBER: _ClassVar[int]
    OAJOOBGHAGM_FIELD_NUMBER: _ClassVar[int]
    PHHAEFNLMGG_FIELD_NUMBER: _ClassVar[int]
    OKBKPBLOPLN_FIELD_NUMBER: _ClassVar[int]
    KHIHKMMNCMO_FIELD_NUMBER: _ClassVar[int]
    EACCPEFBMMJ_FIELD_NUMBER: _ClassVar[int]
    CKNAFCGJELM: _containers.RepeatedScalarFieldContainer[int]
    HAPPCAHNNJI: _containers.MessageMap[int, _MEENBHFDNGJ_pb2.MEENBHFDNGJ]
    PKHPCJOGDBB: _containers.RepeatedCompositeFieldContainer[_DDIAKFFCPDH_pb2.DDIAKFFCPDH]
    IPBOJDIJFKE: _containers.RepeatedScalarFieldContainer[int]
    EPFPAMGGPHK: _containers.RepeatedScalarFieldContainer[int]
    LNGHHDIABNK: float
    JPCFCAMDOOJ: int
    DFIDINDBNGM: int
    NKGDGKCIDJJ: int
    KFDINLFHFMK: int
    EAIPGEMKNPO: int
    OAJOOBGHAGM: int
    PHHAEFNLMGG: bool
    OKBKPBLOPLN: bool
    KHIHKMMNCMO: int
    EACCPEFBMMJ: int
    def __init__(self, CKNAFCGJELM: _Optional[_Iterable[int]] = ..., HAPPCAHNNJI: _Optional[_Mapping[int, _MEENBHFDNGJ_pb2.MEENBHFDNGJ]] = ..., PKHPCJOGDBB: _Optional[_Iterable[_Union[_DDIAKFFCPDH_pb2.DDIAKFFCPDH, _Mapping]]] = ..., IPBOJDIJFKE: _Optional[_Iterable[int]] = ..., EPFPAMGGPHK: _Optional[_Iterable[int]] = ..., LNGHHDIABNK: _Optional[float] = ..., JPCFCAMDOOJ: _Optional[int] = ..., DFIDINDBNGM: _Optional[int] = ..., NKGDGKCIDJJ: _Optional[int] = ..., KFDINLFHFMK: _Optional[int] = ..., EAIPGEMKNPO: _Optional[int] = ..., OAJOOBGHAGM: _Optional[int] = ..., PHHAEFNLMGG: bool = ..., OKBKPBLOPLN: bool = ..., KHIHKMMNCMO: _Optional[int] = ..., EACCPEFBMMJ: _Optional[int] = ...) -> None: ...
