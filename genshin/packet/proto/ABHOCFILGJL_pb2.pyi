from genshin.packet.proto import EMEAJKNIEFA_pb2 as _EMEAJKNIEFA_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ABHOCFILGJL(_message.Message):
    __slots__ = ("IPFOIMLFPIK", "CDJJOHNDCHN", "ECCKEBKEIOG", "MGMGOLJINMN", "NGHBFMBJGCL", "KKLADHFCBFJ", "AIPKCNHFDFN", "BEGLAPFGFAF", "PNNMIHFHFNK", "NMGAMKNNOJD", "GPCDKNKNMNL")
    class IPFOIMLFPIKEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class CDJJOHNDCHNEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    IPFOIMLFPIK_FIELD_NUMBER: _ClassVar[int]
    CDJJOHNDCHN_FIELD_NUMBER: _ClassVar[int]
    ECCKEBKEIOG_FIELD_NUMBER: _ClassVar[int]
    MGMGOLJINMN_FIELD_NUMBER: _ClassVar[int]
    NGHBFMBJGCL_FIELD_NUMBER: _ClassVar[int]
    KKLADHFCBFJ_FIELD_NUMBER: _ClassVar[int]
    AIPKCNHFDFN_FIELD_NUMBER: _ClassVar[int]
    BEGLAPFGFAF_FIELD_NUMBER: _ClassVar[int]
    PNNMIHFHFNK_FIELD_NUMBER: _ClassVar[int]
    NMGAMKNNOJD_FIELD_NUMBER: _ClassVar[int]
    GPCDKNKNMNL_FIELD_NUMBER: _ClassVar[int]
    IPFOIMLFPIK: _containers.ScalarMap[int, int]
    CDJJOHNDCHN: _containers.ScalarMap[int, int]
    ECCKEBKEIOG: _containers.RepeatedScalarFieldContainer[int]
    MGMGOLJINMN: _containers.RepeatedCompositeFieldContainer[_EMEAJKNIEFA_pb2.EMEAJKNIEFA]
    NGHBFMBJGCL: int
    KKLADHFCBFJ: int
    AIPKCNHFDFN: int
    BEGLAPFGFAF: int
    PNNMIHFHFNK: int
    NMGAMKNNOJD: int
    GPCDKNKNMNL: int
    def __init__(self, IPFOIMLFPIK: _Optional[_Mapping[int, int]] = ..., CDJJOHNDCHN: _Optional[_Mapping[int, int]] = ..., ECCKEBKEIOG: _Optional[_Iterable[int]] = ..., MGMGOLJINMN: _Optional[_Iterable[_Union[_EMEAJKNIEFA_pb2.EMEAJKNIEFA, _Mapping]]] = ..., NGHBFMBJGCL: _Optional[int] = ..., KKLADHFCBFJ: _Optional[int] = ..., AIPKCNHFDFN: _Optional[int] = ..., BEGLAPFGFAF: _Optional[int] = ..., PNNMIHFHFNK: _Optional[int] = ..., NMGAMKNNOJD: _Optional[int] = ..., GPCDKNKNMNL: _Optional[int] = ...) -> None: ...
