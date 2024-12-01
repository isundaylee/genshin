from genshin.packet.proto import DGIDDPPFFDJ_pb2 as _DGIDDPPFFDJ_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DHNBIHGAEJB(_message.Message):
    __slots__ = ("EEPDGHEJGPM", "FMFKLMJBPGA", "ANNCKMOHNLE")
    class EEPDGHEJGPMEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _DGIDDPPFFDJ_pb2.DGIDDPPFFDJ
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_DGIDDPPFFDJ_pb2.DGIDDPPFFDJ, _Mapping]] = ...) -> None: ...
    class FMFKLMJBPGAEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    EEPDGHEJGPM_FIELD_NUMBER: _ClassVar[int]
    FMFKLMJBPGA_FIELD_NUMBER: _ClassVar[int]
    ANNCKMOHNLE_FIELD_NUMBER: _ClassVar[int]
    EEPDGHEJGPM: _containers.MessageMap[int, _DGIDDPPFFDJ_pb2.DGIDDPPFFDJ]
    FMFKLMJBPGA: _containers.ScalarMap[int, int]
    ANNCKMOHNLE: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, EEPDGHEJGPM: _Optional[_Mapping[int, _DGIDDPPFFDJ_pb2.DGIDDPPFFDJ]] = ..., FMFKLMJBPGA: _Optional[_Mapping[int, int]] = ..., ANNCKMOHNLE: _Optional[_Iterable[int]] = ...) -> None: ...
