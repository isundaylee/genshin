from genshin.packet.proto import EKPKCPDKCDO_pb2 as _EKPKCPDKCDO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class COPFHIOLNHG(_message.Message):
    __slots__ = ("MECGJHBEJMK", "NPFELIFMOBA", "crucible_info", "DMCCAJMCFPA", "EAEKNFBGKPA", "LJBCGMADOLK", "AEHJBEELKOO")
    MECGJHBEJMK_FIELD_NUMBER: _ClassVar[int]
    NPFELIFMOBA_FIELD_NUMBER: _ClassVar[int]
    CRUCIBLE_INFO_FIELD_NUMBER: _ClassVar[int]
    DMCCAJMCFPA_FIELD_NUMBER: _ClassVar[int]
    EAEKNFBGKPA_FIELD_NUMBER: _ClassVar[int]
    LJBCGMADOLK_FIELD_NUMBER: _ClassVar[int]
    AEHJBEELKOO_FIELD_NUMBER: _ClassVar[int]
    MECGJHBEJMK: _containers.RepeatedScalarFieldContainer[int]
    NPFELIFMOBA: int
    crucible_info: _EKPKCPDKCDO_pb2.EKPKCPDKCDO
    DMCCAJMCFPA: int
    EAEKNFBGKPA: int
    LJBCGMADOLK: int
    AEHJBEELKOO: int
    def __init__(self, MECGJHBEJMK: _Optional[_Iterable[int]] = ..., NPFELIFMOBA: _Optional[int] = ..., crucible_info: _Optional[_Union[_EKPKCPDKCDO_pb2.EKPKCPDKCDO, _Mapping]] = ..., DMCCAJMCFPA: _Optional[int] = ..., EAEKNFBGKPA: _Optional[int] = ..., LJBCGMADOLK: _Optional[int] = ..., AEHJBEELKOO: _Optional[int] = ...) -> None: ...
