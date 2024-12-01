from genshin.packet.proto import NDMDBGOJBGO_pb2 as _NDMDBGOJBGO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IIOLLKFCNED(_message.Message):
    __slots__ = ("OOCHMLBHNFH", "FOLOMOBDODM", "HFGHIMOABBE", "KJOGIDLLODK", "FMMAKJKIIDN", "JINLIBHHLND")
    class FOLOMOBDODMEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class KJOGIDLLODKEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    OOCHMLBHNFH_FIELD_NUMBER: _ClassVar[int]
    FOLOMOBDODM_FIELD_NUMBER: _ClassVar[int]
    HFGHIMOABBE_FIELD_NUMBER: _ClassVar[int]
    KJOGIDLLODK_FIELD_NUMBER: _ClassVar[int]
    FMMAKJKIIDN_FIELD_NUMBER: _ClassVar[int]
    JINLIBHHLND_FIELD_NUMBER: _ClassVar[int]
    OOCHMLBHNFH: _containers.RepeatedCompositeFieldContainer[_NDMDBGOJBGO_pb2.NDMDBGOJBGO]
    FOLOMOBDODM: _containers.ScalarMap[int, int]
    HFGHIMOABBE: _containers.RepeatedScalarFieldContainer[int]
    KJOGIDLLODK: _containers.ScalarMap[int, int]
    FMMAKJKIIDN: int
    JINLIBHHLND: int
    def __init__(self, OOCHMLBHNFH: _Optional[_Iterable[_Union[_NDMDBGOJBGO_pb2.NDMDBGOJBGO, _Mapping]]] = ..., FOLOMOBDODM: _Optional[_Mapping[int, int]] = ..., HFGHIMOABBE: _Optional[_Iterable[int]] = ..., KJOGIDLLODK: _Optional[_Mapping[int, int]] = ..., FMMAKJKIIDN: _Optional[int] = ..., JINLIBHHLND: _Optional[int] = ...) -> None: ...
