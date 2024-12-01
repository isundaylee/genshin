from genshin.packet.proto import OFBHCGGGGGN_pb2 as _OFBHCGGGGGN_pb2
from genshin.packet.proto import OAOPJBOCJJD_pb2 as _OAOPJBOCJJD_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IBLOCCLJHLC(_message.Message):
    __slots__ = ("FMIEBPKJJPJ", "OJBEHPEBOEP", "JAPEOEJLNPD", "LICEOCKLOGD", "OMENIAMEDCE", "HCJFDJHILAM", "LCDDIDLJEDN", "LJAIKBEHODC")
    class FMIEBPKJJPJEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _OFBHCGGGGGN_pb2.OFBHCGGGGGN
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_OFBHCGGGGGN_pb2.OFBHCGGGGGN, _Mapping]] = ...) -> None: ...
    FMIEBPKJJPJ_FIELD_NUMBER: _ClassVar[int]
    OJBEHPEBOEP_FIELD_NUMBER: _ClassVar[int]
    JAPEOEJLNPD_FIELD_NUMBER: _ClassVar[int]
    LICEOCKLOGD_FIELD_NUMBER: _ClassVar[int]
    OMENIAMEDCE_FIELD_NUMBER: _ClassVar[int]
    HCJFDJHILAM_FIELD_NUMBER: _ClassVar[int]
    LCDDIDLJEDN_FIELD_NUMBER: _ClassVar[int]
    LJAIKBEHODC_FIELD_NUMBER: _ClassVar[int]
    FMIEBPKJJPJ: _containers.MessageMap[int, _OFBHCGGGGGN_pb2.OFBHCGGGGGN]
    OJBEHPEBOEP: int
    JAPEOEJLNPD: int
    LICEOCKLOGD: _OAOPJBOCJJD_pb2.OAOPJBOCJJD
    OMENIAMEDCE: bool
    HCJFDJHILAM: bool
    LCDDIDLJEDN: int
    LJAIKBEHODC: int
    def __init__(self, FMIEBPKJJPJ: _Optional[_Mapping[int, _OFBHCGGGGGN_pb2.OFBHCGGGGGN]] = ..., OJBEHPEBOEP: _Optional[int] = ..., JAPEOEJLNPD: _Optional[int] = ..., LICEOCKLOGD: _Optional[_Union[_OAOPJBOCJJD_pb2.OAOPJBOCJJD, str]] = ..., OMENIAMEDCE: bool = ..., HCJFDJHILAM: bool = ..., LCDDIDLJEDN: _Optional[int] = ..., LJAIKBEHODC: _Optional[int] = ...) -> None: ...
