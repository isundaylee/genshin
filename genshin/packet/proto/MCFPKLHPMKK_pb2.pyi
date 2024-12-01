from genshin.packet.proto import EFEGIIMAOMI_pb2 as _EFEGIIMAOMI_pb2
from genshin.packet.proto import NNHFMCJOGPO_pb2 as _NNHFMCJOGPO_pb2
from genshin.packet.proto import HMBFCHKMEGD_pb2 as _HMBFCHKMEGD_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MCFPKLHPMKK(_message.Message):
    __slots__ = ("HDCJFKPPLFC", "DKDAKPFICJC", "OOFABEHBCBH", "EJNINFFFKJP")
    HDCJFKPPLFC_FIELD_NUMBER: _ClassVar[int]
    DKDAKPFICJC_FIELD_NUMBER: _ClassVar[int]
    OOFABEHBCBH_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    HDCJFKPPLFC: _containers.RepeatedCompositeFieldContainer[_EFEGIIMAOMI_pb2.EFEGIIMAOMI]
    DKDAKPFICJC: _containers.RepeatedCompositeFieldContainer[_NNHFMCJOGPO_pb2.NNHFMCJOGPO]
    OOFABEHBCBH: _HMBFCHKMEGD_pb2.HMBFCHKMEGD
    EJNINFFFKJP: int
    def __init__(self, HDCJFKPPLFC: _Optional[_Iterable[_Union[_EFEGIIMAOMI_pb2.EFEGIIMAOMI, _Mapping]]] = ..., DKDAKPFICJC: _Optional[_Iterable[_Union[_NNHFMCJOGPO_pb2.NNHFMCJOGPO, _Mapping]]] = ..., OOFABEHBCBH: _Optional[_Union[_HMBFCHKMEGD_pb2.HMBFCHKMEGD, str]] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
