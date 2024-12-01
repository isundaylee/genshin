from genshin.packet.proto import MMGPMBAHFOM_pb2 as _MMGPMBAHFOM_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FHMMNELMNMD(_message.Message):
    __slots__ = ("KJHMPFCNAEE", "CGGMEDEICFL", "DIGPDMKMGAF", "level", "offering_pari_detail_data", "KCJGPLKNPCL", "PFKAFIIAPKN")
    class KJHMPFCNAEEEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    KJHMPFCNAEE_FIELD_NUMBER: _ClassVar[int]
    CGGMEDEICFL_FIELD_NUMBER: _ClassVar[int]
    DIGPDMKMGAF_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    OFFERING_PARI_DETAIL_DATA_FIELD_NUMBER: _ClassVar[int]
    KCJGPLKNPCL_FIELD_NUMBER: _ClassVar[int]
    PFKAFIIAPKN_FIELD_NUMBER: _ClassVar[int]
    KJHMPFCNAEE: _containers.ScalarMap[int, int]
    CGGMEDEICFL: _containers.RepeatedScalarFieldContainer[int]
    DIGPDMKMGAF: int
    level: int
    offering_pari_detail_data: _MMGPMBAHFOM_pb2.MMGPMBAHFOM
    KCJGPLKNPCL: bool
    PFKAFIIAPKN: bool
    def __init__(self, KJHMPFCNAEE: _Optional[_Mapping[int, int]] = ..., CGGMEDEICFL: _Optional[_Iterable[int]] = ..., DIGPDMKMGAF: _Optional[int] = ..., level: _Optional[int] = ..., offering_pari_detail_data: _Optional[_Union[_MMGPMBAHFOM_pb2.MMGPMBAHFOM, _Mapping]] = ..., KCJGPLKNPCL: bool = ..., PFKAFIIAPKN: bool = ...) -> None: ...
