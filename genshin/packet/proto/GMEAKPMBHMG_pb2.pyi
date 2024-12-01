from genshin.packet.proto import FABGOAPPDAO_pb2 as _FABGOAPPDAO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GMEAKPMBHMG(_message.Message):
    __slots__ = ("JLIJIJMOHHH", "FEBAIKFCOOB", "DNIDCKPPOKG", "PKGNLEECMJJ", "NNMFNFDLKAF", "AGIDBEEINDE", "OEEMPADNHAO", "HNHNKBLHBCP", "FGGBAFBEKCA", "FDOGNIGLFLI", "NDCDFFNIHJM", "DMGOJDBKCIH")
    class JLIJIJMOHHHEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    JLIJIJMOHHH_FIELD_NUMBER: _ClassVar[int]
    FEBAIKFCOOB_FIELD_NUMBER: _ClassVar[int]
    DNIDCKPPOKG_FIELD_NUMBER: _ClassVar[int]
    PKGNLEECMJJ_FIELD_NUMBER: _ClassVar[int]
    NNMFNFDLKAF_FIELD_NUMBER: _ClassVar[int]
    AGIDBEEINDE_FIELD_NUMBER: _ClassVar[int]
    OEEMPADNHAO_FIELD_NUMBER: _ClassVar[int]
    HNHNKBLHBCP_FIELD_NUMBER: _ClassVar[int]
    FGGBAFBEKCA_FIELD_NUMBER: _ClassVar[int]
    FDOGNIGLFLI_FIELD_NUMBER: _ClassVar[int]
    NDCDFFNIHJM_FIELD_NUMBER: _ClassVar[int]
    DMGOJDBKCIH_FIELD_NUMBER: _ClassVar[int]
    JLIJIJMOHHH: _containers.ScalarMap[int, int]
    FEBAIKFCOOB: _containers.RepeatedCompositeFieldContainer[_FABGOAPPDAO_pb2.FABGOAPPDAO]
    DNIDCKPPOKG: float
    PKGNLEECMJJ: int
    NNMFNFDLKAF: float
    AGIDBEEINDE: int
    OEEMPADNHAO: float
    HNHNKBLHBCP: int
    FGGBAFBEKCA: int
    FDOGNIGLFLI: int
    NDCDFFNIHJM: int
    DMGOJDBKCIH: float
    def __init__(self, JLIJIJMOHHH: _Optional[_Mapping[int, int]] = ..., FEBAIKFCOOB: _Optional[_Iterable[_Union[_FABGOAPPDAO_pb2.FABGOAPPDAO, _Mapping]]] = ..., DNIDCKPPOKG: _Optional[float] = ..., PKGNLEECMJJ: _Optional[int] = ..., NNMFNFDLKAF: _Optional[float] = ..., AGIDBEEINDE: _Optional[int] = ..., OEEMPADNHAO: _Optional[float] = ..., HNHNKBLHBCP: _Optional[int] = ..., FGGBAFBEKCA: _Optional[int] = ..., FDOGNIGLFLI: _Optional[int] = ..., NDCDFFNIHJM: _Optional[int] = ..., DMGOJDBKCIH: _Optional[float] = ...) -> None: ...
