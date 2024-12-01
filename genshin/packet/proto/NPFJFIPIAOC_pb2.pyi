from genshin.packet.proto import EKOEOPHMBJO_pb2 as _EKOEOPHMBJO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NPFJFIPIAOC(_message.Message):
    __slots__ = ("JMODOCBICJF", "ILFDMJIMGEI", "HLOCCMMEDJL", "KFHDNEDJJNC", "JJAGBKHDLPF")
    JMODOCBICJF_FIELD_NUMBER: _ClassVar[int]
    ILFDMJIMGEI_FIELD_NUMBER: _ClassVar[int]
    HLOCCMMEDJL_FIELD_NUMBER: _ClassVar[int]
    KFHDNEDJJNC_FIELD_NUMBER: _ClassVar[int]
    JJAGBKHDLPF_FIELD_NUMBER: _ClassVar[int]
    JMODOCBICJF: _containers.RepeatedCompositeFieldContainer[_EKOEOPHMBJO_pb2.EKOEOPHMBJO]
    ILFDMJIMGEI: int
    HLOCCMMEDJL: int
    KFHDNEDJJNC: int
    JJAGBKHDLPF: int
    def __init__(self, JMODOCBICJF: _Optional[_Iterable[_Union[_EKOEOPHMBJO_pb2.EKOEOPHMBJO, _Mapping]]] = ..., ILFDMJIMGEI: _Optional[int] = ..., HLOCCMMEDJL: _Optional[int] = ..., KFHDNEDJJNC: _Optional[int] = ..., JJAGBKHDLPF: _Optional[int] = ...) -> None: ...
