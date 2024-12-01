from genshin.packet.proto import PCNOMCDHBIA_pb2 as _PCNOMCDHBIA_pb2
from genshin.packet.proto import KIAPPNBMOBO_pb2 as _KIAPPNBMOBO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FDLJMDJJNKD(_message.Message):
    __slots__ = ("AEBMEKGCEFP", "CFPCDOLPJBF", "JHOMLEHHIFK", "MGHAICHPPCK")
    AEBMEKGCEFP_FIELD_NUMBER: _ClassVar[int]
    CFPCDOLPJBF_FIELD_NUMBER: _ClassVar[int]
    JHOMLEHHIFK_FIELD_NUMBER: _ClassVar[int]
    MGHAICHPPCK_FIELD_NUMBER: _ClassVar[int]
    AEBMEKGCEFP: _containers.RepeatedCompositeFieldContainer[_PCNOMCDHBIA_pb2.PCNOMCDHBIA]
    CFPCDOLPJBF: _containers.RepeatedScalarFieldContainer[int]
    JHOMLEHHIFK: _containers.RepeatedCompositeFieldContainer[_KIAPPNBMOBO_pb2.KIAPPNBMOBO]
    MGHAICHPPCK: bool
    def __init__(self, AEBMEKGCEFP: _Optional[_Iterable[_Union[_PCNOMCDHBIA_pb2.PCNOMCDHBIA, _Mapping]]] = ..., CFPCDOLPJBF: _Optional[_Iterable[int]] = ..., JHOMLEHHIFK: _Optional[_Iterable[_Union[_KIAPPNBMOBO_pb2.KIAPPNBMOBO, _Mapping]]] = ..., MGHAICHPPCK: bool = ...) -> None: ...
