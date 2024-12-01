from genshin.packet.proto import AGFCMLMDKFD_pb2 as _AGFCMLMDKFD_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OEFKELJINLI(_message.Message):
    __slots__ = ("GIPGEPLIEGM", "PADGINLBCMN", "DLCBIJLGPAN", "OMFMLFAFIGA", "EFKPNBAOPAD", "KHKOBCEFBBJ", "BNBOHMBKNKE", "OPOOBJEOOKM", "OALIOHAMLGN", "LAOKDLOOJPJ")
    class GIPGEPLIEGMEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    GIPGEPLIEGM_FIELD_NUMBER: _ClassVar[int]
    PADGINLBCMN_FIELD_NUMBER: _ClassVar[int]
    DLCBIJLGPAN_FIELD_NUMBER: _ClassVar[int]
    OMFMLFAFIGA_FIELD_NUMBER: _ClassVar[int]
    EFKPNBAOPAD_FIELD_NUMBER: _ClassVar[int]
    KHKOBCEFBBJ_FIELD_NUMBER: _ClassVar[int]
    BNBOHMBKNKE_FIELD_NUMBER: _ClassVar[int]
    OPOOBJEOOKM_FIELD_NUMBER: _ClassVar[int]
    OALIOHAMLGN_FIELD_NUMBER: _ClassVar[int]
    LAOKDLOOJPJ_FIELD_NUMBER: _ClassVar[int]
    GIPGEPLIEGM: _containers.ScalarMap[int, int]
    PADGINLBCMN: int
    DLCBIJLGPAN: int
    OMFMLFAFIGA: int
    EFKPNBAOPAD: bool
    KHKOBCEFBBJ: bool
    BNBOHMBKNKE: int
    OPOOBJEOOKM: _AGFCMLMDKFD_pb2.AGFCMLMDKFD
    OALIOHAMLGN: int
    LAOKDLOOJPJ: int
    def __init__(self, GIPGEPLIEGM: _Optional[_Mapping[int, int]] = ..., PADGINLBCMN: _Optional[int] = ..., DLCBIJLGPAN: _Optional[int] = ..., OMFMLFAFIGA: _Optional[int] = ..., EFKPNBAOPAD: bool = ..., KHKOBCEFBBJ: bool = ..., BNBOHMBKNKE: _Optional[int] = ..., OPOOBJEOOKM: _Optional[_Union[_AGFCMLMDKFD_pb2.AGFCMLMDKFD, str]] = ..., OALIOHAMLGN: _Optional[int] = ..., LAOKDLOOJPJ: _Optional[int] = ...) -> None: ...
