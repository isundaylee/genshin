from genshin.packet.proto import KMJJCHGBLHB_pb2 as _KMJJCHGBLHB_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FOFBDKCPIDC(_message.Message):
    __slots__ = ("AKAFECACNJL", "FAPDAMIMCMH", "OEEDNMALMIF")
    AKAFECACNJL_FIELD_NUMBER: _ClassVar[int]
    FAPDAMIMCMH_FIELD_NUMBER: _ClassVar[int]
    OEEDNMALMIF_FIELD_NUMBER: _ClassVar[int]
    AKAFECACNJL: _containers.RepeatedCompositeFieldContainer[_KMJJCHGBLHB_pb2.KMJJCHGBLHB]
    FAPDAMIMCMH: bool
    OEEDNMALMIF: bool
    def __init__(self, AKAFECACNJL: _Optional[_Iterable[_Union[_KMJJCHGBLHB_pb2.KMJJCHGBLHB, _Mapping]]] = ..., FAPDAMIMCMH: bool = ..., OEEDNMALMIF: bool = ...) -> None: ...
