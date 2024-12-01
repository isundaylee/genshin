from genshin.packet.proto import JCJCMAIBCAO_pb2 as _JCJCMAIBCAO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NNKAFLNDIBF(_message.Message):
    __slots__ = ("LAGEEOHCMNG", "LBOJANOKNPA", "PPJMHPBHOKF")
    class PPJMHPBHOKFEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    LAGEEOHCMNG_FIELD_NUMBER: _ClassVar[int]
    LBOJANOKNPA_FIELD_NUMBER: _ClassVar[int]
    PPJMHPBHOKF_FIELD_NUMBER: _ClassVar[int]
    LAGEEOHCMNG: _containers.RepeatedCompositeFieldContainer[_JCJCMAIBCAO_pb2.JCJCMAIBCAO]
    LBOJANOKNPA: _containers.RepeatedScalarFieldContainer[int]
    PPJMHPBHOKF: _containers.ScalarMap[int, int]
    def __init__(self, LAGEEOHCMNG: _Optional[_Iterable[_Union[_JCJCMAIBCAO_pb2.JCJCMAIBCAO, _Mapping]]] = ..., LBOJANOKNPA: _Optional[_Iterable[int]] = ..., PPJMHPBHOKF: _Optional[_Mapping[int, int]] = ...) -> None: ...
