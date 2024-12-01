from genshin.packet.proto import PKJMPCPEGGO_pb2 as _PKJMPCPEGGO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HJPEIAODCBK(_message.Message):
    __slots__ = ("IANEBDKAMBM", "MPMEJIBKJEO", "IJLHLCLLENE", "MHPFNLKCFOM", "OAOPAOOMIPB", "EFAJIHMNOBK", "GJABNFPKMEB", "NCCPPHNNPBF", "OOIPGFEDJMN")
    class GJABNFPKMEBEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    IANEBDKAMBM_FIELD_NUMBER: _ClassVar[int]
    MPMEJIBKJEO_FIELD_NUMBER: _ClassVar[int]
    IJLHLCLLENE_FIELD_NUMBER: _ClassVar[int]
    MHPFNLKCFOM_FIELD_NUMBER: _ClassVar[int]
    OAOPAOOMIPB_FIELD_NUMBER: _ClassVar[int]
    EFAJIHMNOBK_FIELD_NUMBER: _ClassVar[int]
    GJABNFPKMEB_FIELD_NUMBER: _ClassVar[int]
    NCCPPHNNPBF_FIELD_NUMBER: _ClassVar[int]
    OOIPGFEDJMN_FIELD_NUMBER: _ClassVar[int]
    IANEBDKAMBM: _PKJMPCPEGGO_pb2.PKJMPCPEGGO
    MPMEJIBKJEO: str
    IJLHLCLLENE: str
    MHPFNLKCFOM: str
    OAOPAOOMIPB: _containers.RepeatedScalarFieldContainer[int]
    EFAJIHMNOBK: str
    GJABNFPKMEB: _containers.ScalarMap[int, int]
    NCCPPHNNPBF: int
    OOIPGFEDJMN: int
    def __init__(self, IANEBDKAMBM: _Optional[_Union[_PKJMPCPEGGO_pb2.PKJMPCPEGGO, _Mapping]] = ..., MPMEJIBKJEO: _Optional[str] = ..., IJLHLCLLENE: _Optional[str] = ..., MHPFNLKCFOM: _Optional[str] = ..., OAOPAOOMIPB: _Optional[_Iterable[int]] = ..., EFAJIHMNOBK: _Optional[str] = ..., GJABNFPKMEB: _Optional[_Mapping[int, int]] = ..., NCCPPHNNPBF: _Optional[int] = ..., OOIPGFEDJMN: _Optional[int] = ...) -> None: ...
