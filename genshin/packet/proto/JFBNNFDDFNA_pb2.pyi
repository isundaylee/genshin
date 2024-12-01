from genshin.packet.proto import HHFJEBHLGHH_pb2 as _HHFJEBHLGHH_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JFBNNFDDFNA(_message.Message):
    __slots__ = ("LNHADDHLHKI", "EJNINFFFKJP", "avatar_id", "BNFFIGFAIAO", "IMIOGMDOKCB")
    LNHADDHLHKI_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    BNFFIGFAIAO_FIELD_NUMBER: _ClassVar[int]
    IMIOGMDOKCB_FIELD_NUMBER: _ClassVar[int]
    LNHADDHLHKI: _containers.RepeatedCompositeFieldContainer[_HHFJEBHLGHH_pb2.HHFJEBHLGHH]
    EJNINFFFKJP: int
    avatar_id: int
    BNFFIGFAIAO: bool
    IMIOGMDOKCB: int
    def __init__(self, LNHADDHLHKI: _Optional[_Iterable[_Union[_HHFJEBHLGHH_pb2.HHFJEBHLGHH, _Mapping]]] = ..., EJNINFFFKJP: _Optional[int] = ..., avatar_id: _Optional[int] = ..., BNFFIGFAIAO: bool = ..., IMIOGMDOKCB: _Optional[int] = ...) -> None: ...
