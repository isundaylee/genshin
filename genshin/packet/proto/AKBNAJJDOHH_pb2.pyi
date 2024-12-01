from genshin.packet.proto import HFHJKHOPLMN_pb2 as _HFHJKHOPLMN_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AKBNAJJDOHH(_message.Message):
    __slots__ = ("KOGMMCNPJLL", "MEIKGBOLDGH", "AEKAGEEBAAA", "FADINCNPBMD", "PIEAPGEPMLF", "PALEKJJHCMJ")
    KOGMMCNPJLL_FIELD_NUMBER: _ClassVar[int]
    MEIKGBOLDGH_FIELD_NUMBER: _ClassVar[int]
    AEKAGEEBAAA_FIELD_NUMBER: _ClassVar[int]
    FADINCNPBMD_FIELD_NUMBER: _ClassVar[int]
    PIEAPGEPMLF_FIELD_NUMBER: _ClassVar[int]
    PALEKJJHCMJ_FIELD_NUMBER: _ClassVar[int]
    KOGMMCNPJLL: _containers.RepeatedScalarFieldContainer[int]
    MEIKGBOLDGH: _containers.RepeatedCompositeFieldContainer[_HFHJKHOPLMN_pb2.HFHJKHOPLMN]
    AEKAGEEBAAA: int
    FADINCNPBMD: bool
    PIEAPGEPMLF: int
    PALEKJJHCMJ: int
    def __init__(self, KOGMMCNPJLL: _Optional[_Iterable[int]] = ..., MEIKGBOLDGH: _Optional[_Iterable[_Union[_HFHJKHOPLMN_pb2.HFHJKHOPLMN, _Mapping]]] = ..., AEKAGEEBAAA: _Optional[int] = ..., FADINCNPBMD: bool = ..., PIEAPGEPMLF: _Optional[int] = ..., PALEKJJHCMJ: _Optional[int] = ...) -> None: ...
