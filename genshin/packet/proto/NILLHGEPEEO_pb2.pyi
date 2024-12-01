from genshin.packet.proto import OFELNADBNKC_pb2 as _OFELNADBNKC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NILLHGEPEEO(_message.Message):
    __slots__ = ("AHKLLFKIDCN", "JAHPPELNEDF", "NNPGPKKBLIH", "JIMELGDJMLF", "CHPHEAEDCJL", "EHAEACFBOOL")
    class AHKLLFKIDCNEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    AHKLLFKIDCN_FIELD_NUMBER: _ClassVar[int]
    JAHPPELNEDF_FIELD_NUMBER: _ClassVar[int]
    NNPGPKKBLIH_FIELD_NUMBER: _ClassVar[int]
    JIMELGDJMLF_FIELD_NUMBER: _ClassVar[int]
    CHPHEAEDCJL_FIELD_NUMBER: _ClassVar[int]
    EHAEACFBOOL_FIELD_NUMBER: _ClassVar[int]
    AHKLLFKIDCN: _containers.ScalarMap[int, int]
    JAHPPELNEDF: _containers.RepeatedCompositeFieldContainer[_OFELNADBNKC_pb2.OFELNADBNKC]
    NNPGPKKBLIH: int
    JIMELGDJMLF: int
    CHPHEAEDCJL: int
    EHAEACFBOOL: int
    def __init__(self, AHKLLFKIDCN: _Optional[_Mapping[int, int]] = ..., JAHPPELNEDF: _Optional[_Iterable[_Union[_OFELNADBNKC_pb2.OFELNADBNKC, _Mapping]]] = ..., NNPGPKKBLIH: _Optional[int] = ..., JIMELGDJMLF: _Optional[int] = ..., CHPHEAEDCJL: _Optional[int] = ..., EHAEACFBOOL: _Optional[int] = ...) -> None: ...
