from genshin.packet.proto import HGNOGAMJLAF_pb2 as _HGNOGAMJLAF_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MJPKECMOIGA(_message.Message):
    __slots__ = ("MNIMPFAJKLB", "CBCIAPKMJHE", "BMEOIBCMLBI", "PIEIMACPKOL")
    class MNIMPFAJKLBEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    MNIMPFAJKLB_FIELD_NUMBER: _ClassVar[int]
    CBCIAPKMJHE_FIELD_NUMBER: _ClassVar[int]
    BMEOIBCMLBI_FIELD_NUMBER: _ClassVar[int]
    PIEIMACPKOL_FIELD_NUMBER: _ClassVar[int]
    MNIMPFAJKLB: _containers.ScalarMap[int, int]
    CBCIAPKMJHE: _containers.RepeatedCompositeFieldContainer[_HGNOGAMJLAF_pb2.HGNOGAMJLAF]
    BMEOIBCMLBI: int
    PIEIMACPKOL: int
    def __init__(self, MNIMPFAJKLB: _Optional[_Mapping[int, int]] = ..., CBCIAPKMJHE: _Optional[_Iterable[_Union[_HGNOGAMJLAF_pb2.HGNOGAMJLAF, _Mapping]]] = ..., BMEOIBCMLBI: _Optional[int] = ..., PIEIMACPKOL: _Optional[int] = ...) -> None: ...
