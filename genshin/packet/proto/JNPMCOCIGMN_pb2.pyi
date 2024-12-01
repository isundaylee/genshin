from genshin.packet.proto import IGNBAHODBEE_pb2 as _IGNBAHODBEE_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JNPMCOCIGMN(_message.Message):
    __slots__ = ("CBDKNDMEJJB", "DOPJDKEDCBN", "EJNINFFFKJP")
    CBDKNDMEJJB_FIELD_NUMBER: _ClassVar[int]
    DOPJDKEDCBN_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    CBDKNDMEJJB: _containers.RepeatedScalarFieldContainer[int]
    DOPJDKEDCBN: _containers.RepeatedCompositeFieldContainer[_IGNBAHODBEE_pb2.IGNBAHODBEE]
    EJNINFFFKJP: int
    def __init__(self, CBDKNDMEJJB: _Optional[_Iterable[int]] = ..., DOPJDKEDCBN: _Optional[_Iterable[_Union[_IGNBAHODBEE_pb2.IGNBAHODBEE, _Mapping]]] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
