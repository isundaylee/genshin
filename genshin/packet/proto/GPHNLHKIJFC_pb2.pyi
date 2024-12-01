from genshin.packet.proto import BGDCPBEGANK_pb2 as _BGDCPBEGANK_pb2
from genshin.packet.proto import JLMIJCEGCOB_pb2 as _JLMIJCEGCOB_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GPHNLHKIJFC(_message.Message):
    __slots__ = ("NEFMGJIDAAK", "NAJKBNDADMA", "IPNGBHKJJFK", "GCNJNBMHDAM", "LDIILMAHHNG", "MBOLNFOFNGA")
    NEFMGJIDAAK_FIELD_NUMBER: _ClassVar[int]
    NAJKBNDADMA_FIELD_NUMBER: _ClassVar[int]
    IPNGBHKJJFK_FIELD_NUMBER: _ClassVar[int]
    GCNJNBMHDAM_FIELD_NUMBER: _ClassVar[int]
    LDIILMAHHNG_FIELD_NUMBER: _ClassVar[int]
    MBOLNFOFNGA_FIELD_NUMBER: _ClassVar[int]
    NEFMGJIDAAK: _containers.RepeatedCompositeFieldContainer[_BGDCPBEGANK_pb2.BGDCPBEGANK]
    NAJKBNDADMA: _JLMIJCEGCOB_pb2.JLMIJCEGCOB
    IPNGBHKJJFK: bool
    GCNJNBMHDAM: int
    LDIILMAHHNG: int
    MBOLNFOFNGA: int
    def __init__(self, NEFMGJIDAAK: _Optional[_Iterable[_Union[_BGDCPBEGANK_pb2.BGDCPBEGANK, _Mapping]]] = ..., NAJKBNDADMA: _Optional[_Union[_JLMIJCEGCOB_pb2.JLMIJCEGCOB, _Mapping]] = ..., IPNGBHKJJFK: bool = ..., GCNJNBMHDAM: _Optional[int] = ..., LDIILMAHHNG: _Optional[int] = ..., MBOLNFOFNGA: _Optional[int] = ...) -> None: ...
