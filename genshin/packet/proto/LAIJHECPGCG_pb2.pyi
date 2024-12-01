from genshin.packet.proto import BGGJCFHPHBK_pb2 as _BGGJCFHPHBK_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LAIJHECPGCG(_message.Message):
    __slots__ = ("MGDCKPANEDK", "DNBEFLJLAMB", "EJNINFFFKJP")
    MGDCKPANEDK_FIELD_NUMBER: _ClassVar[int]
    DNBEFLJLAMB_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    MGDCKPANEDK: _containers.RepeatedCompositeFieldContainer[_BGGJCFHPHBK_pb2.BGGJCFHPHBK]
    DNBEFLJLAMB: int
    EJNINFFFKJP: int
    def __init__(self, MGDCKPANEDK: _Optional[_Iterable[_Union[_BGGJCFHPHBK_pb2.BGGJCFHPHBK, _Mapping]]] = ..., DNBEFLJLAMB: _Optional[int] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
