from genshin.packet.proto import HFHJKHOPLMN_pb2 as _HFHJKHOPLMN_pb2
from genshin.packet.proto import OLHEKLKENDN_pb2 as _OLHEKLKENDN_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MNFELHIEBKP(_message.Message):
    __slots__ = ("NGDJFLNNFIH", "JAHPPELNEDF", "FGAEINCCKDK", "KLGLHAIOHNA", "CEBBLOPIJEC", "LJJBHMHMJFI", "ODCMKOFFKKL", "IGLNPCKDMPJ", "IEMNNDFMMKJ")
    class NGDJFLNNFIHEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    NGDJFLNNFIH_FIELD_NUMBER: _ClassVar[int]
    JAHPPELNEDF_FIELD_NUMBER: _ClassVar[int]
    FGAEINCCKDK_FIELD_NUMBER: _ClassVar[int]
    KLGLHAIOHNA_FIELD_NUMBER: _ClassVar[int]
    CEBBLOPIJEC_FIELD_NUMBER: _ClassVar[int]
    LJJBHMHMJFI_FIELD_NUMBER: _ClassVar[int]
    ODCMKOFFKKL_FIELD_NUMBER: _ClassVar[int]
    IGLNPCKDMPJ_FIELD_NUMBER: _ClassVar[int]
    IEMNNDFMMKJ_FIELD_NUMBER: _ClassVar[int]
    NGDJFLNNFIH: _containers.ScalarMap[int, int]
    JAHPPELNEDF: _containers.RepeatedCompositeFieldContainer[_HFHJKHOPLMN_pb2.HFHJKHOPLMN]
    FGAEINCCKDK: _OLHEKLKENDN_pb2.OLHEKLKENDN
    KLGLHAIOHNA: int
    CEBBLOPIJEC: int
    LJJBHMHMJFI: int
    ODCMKOFFKKL: int
    IGLNPCKDMPJ: int
    IEMNNDFMMKJ: float
    def __init__(self, NGDJFLNNFIH: _Optional[_Mapping[int, int]] = ..., JAHPPELNEDF: _Optional[_Iterable[_Union[_HFHJKHOPLMN_pb2.HFHJKHOPLMN, _Mapping]]] = ..., FGAEINCCKDK: _Optional[_Union[_OLHEKLKENDN_pb2.OLHEKLKENDN, _Mapping]] = ..., KLGLHAIOHNA: _Optional[int] = ..., CEBBLOPIJEC: _Optional[int] = ..., LJJBHMHMJFI: _Optional[int] = ..., ODCMKOFFKKL: _Optional[int] = ..., IGLNPCKDMPJ: _Optional[int] = ..., IEMNNDFMMKJ: _Optional[float] = ...) -> None: ...
