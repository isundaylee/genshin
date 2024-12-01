from genshin.packet.proto import GOOOCKGEEFH_pb2 as _GOOOCKGEEFH_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LAMEAODOJID(_message.Message):
    __slots__ = ("avatar_list", "POKHDGJNLMF", "BGHKLCFCJCP", "FMOONPCGHDB")
    AVATAR_LIST_FIELD_NUMBER: _ClassVar[int]
    POKHDGJNLMF_FIELD_NUMBER: _ClassVar[int]
    BGHKLCFCJCP_FIELD_NUMBER: _ClassVar[int]
    FMOONPCGHDB_FIELD_NUMBER: _ClassVar[int]
    avatar_list: _containers.RepeatedCompositeFieldContainer[_GOOOCKGEEFH_pb2.GOOOCKGEEFH]
    POKHDGJNLMF: int
    BGHKLCFCJCP: int
    FMOONPCGHDB: int
    def __init__(self, avatar_list: _Optional[_Iterable[_Union[_GOOOCKGEEFH_pb2.GOOOCKGEEFH, _Mapping]]] = ..., POKHDGJNLMF: _Optional[int] = ..., BGHKLCFCJCP: _Optional[int] = ..., FMOONPCGHDB: _Optional[int] = ...) -> None: ...
