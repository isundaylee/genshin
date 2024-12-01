from genshin.packet.proto import GEGKOBEIJDA_pb2 as _GEGKOBEIJDA_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AAFIOOGBAAG(_message.Message):
    __slots__ = ("GHFLOBGMGNC", "avatar_id", "BNFFIGFAIAO", "IMIOGMDOKCB")
    GHFLOBGMGNC_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    BNFFIGFAIAO_FIELD_NUMBER: _ClassVar[int]
    IMIOGMDOKCB_FIELD_NUMBER: _ClassVar[int]
    GHFLOBGMGNC: _containers.RepeatedCompositeFieldContainer[_GEGKOBEIJDA_pb2.GEGKOBEIJDA]
    avatar_id: int
    BNFFIGFAIAO: bool
    IMIOGMDOKCB: int
    def __init__(self, GHFLOBGMGNC: _Optional[_Iterable[_Union[_GEGKOBEIJDA_pb2.GEGKOBEIJDA, _Mapping]]] = ..., avatar_id: _Optional[int] = ..., BNFFIGFAIAO: bool = ..., IMIOGMDOKCB: _Optional[int] = ...) -> None: ...
