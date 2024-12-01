from genshin.packet.proto import JICKPPDLOHC_pb2 as _JICKPPDLOHC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KIGCGPKHCNH(_message.Message):
    __slots__ = ("AMFBNEJGHMA", "DOKAGAGPMCA", "furniture_suite_id", "slot_id")
    AMFBNEJGHMA_FIELD_NUMBER: _ClassVar[int]
    DOKAGAGPMCA_FIELD_NUMBER: _ClassVar[int]
    FURNITURE_SUITE_ID_FIELD_NUMBER: _ClassVar[int]
    SLOT_ID_FIELD_NUMBER: _ClassVar[int]
    AMFBNEJGHMA: _containers.RepeatedCompositeFieldContainer[_JICKPPDLOHC_pb2.JICKPPDLOHC]
    DOKAGAGPMCA: _containers.RepeatedScalarFieldContainer[int]
    furniture_suite_id: int
    slot_id: int
    def __init__(self, AMFBNEJGHMA: _Optional[_Iterable[_Union[_JICKPPDLOHC_pb2.JICKPPDLOHC, _Mapping]]] = ..., DOKAGAGPMCA: _Optional[_Iterable[int]] = ..., furniture_suite_id: _Optional[int] = ..., slot_id: _Optional[int] = ...) -> None: ...
