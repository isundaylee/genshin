from genshin.packet.proto import IGKLNNDNCMG_pb2 as _IGKLNNDNCMG_pb2
from genshin.packet.proto import OLNCPFJIEKM_pb2 as _OLNCPFJIEKM_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JENPNBFGAHG(_message.Message):
    __slots__ = ("CJENICJPFGE", "NOICHAJIBGA", "FOHBPEMHKNC", "EJNINFFFKJP")
    class CJENICJPFGEEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _IGKLNNDNCMG_pb2.IGKLNNDNCMG
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_IGKLNNDNCMG_pb2.IGKLNNDNCMG, _Mapping]] = ...) -> None: ...
    CJENICJPFGE_FIELD_NUMBER: _ClassVar[int]
    NOICHAJIBGA_FIELD_NUMBER: _ClassVar[int]
    FOHBPEMHKNC_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    CJENICJPFGE: _containers.MessageMap[int, _IGKLNNDNCMG_pb2.IGKLNNDNCMG]
    NOICHAJIBGA: _containers.RepeatedCompositeFieldContainer[_OLNCPFJIEKM_pb2.OLNCPFJIEKM]
    FOHBPEMHKNC: _containers.RepeatedScalarFieldContainer[int]
    EJNINFFFKJP: int
    def __init__(self, CJENICJPFGE: _Optional[_Mapping[int, _IGKLNNDNCMG_pb2.IGKLNNDNCMG]] = ..., NOICHAJIBGA: _Optional[_Iterable[_Union[_OLNCPFJIEKM_pb2.OLNCPFJIEKM, _Mapping]]] = ..., FOHBPEMHKNC: _Optional[_Iterable[int]] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
