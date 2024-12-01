from genshin.packet.proto import EMEAJKNIEFA_pb2 as _EMEAJKNIEFA_pb2
from genshin.packet.proto import MPHAJNOFPHP_pb2 as _MPHAJNOFPHP_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AJMOOMNAMDF(_message.Message):
    __slots__ = ("NOBMGICJGBB", "EEHFGMOLAGK", "NKEDFMOJOHL", "ICDLEPJHIDB", "MBBKAENBCKD", "IFPLLIOOGED", "DNNFDNAPJNJ", "KKLADHFCBFJ", "FGLOHNKKPPG", "DNKAAKGGPAP")
    NOBMGICJGBB_FIELD_NUMBER: _ClassVar[int]
    EEHFGMOLAGK_FIELD_NUMBER: _ClassVar[int]
    NKEDFMOJOHL_FIELD_NUMBER: _ClassVar[int]
    ICDLEPJHIDB_FIELD_NUMBER: _ClassVar[int]
    MBBKAENBCKD_FIELD_NUMBER: _ClassVar[int]
    IFPLLIOOGED_FIELD_NUMBER: _ClassVar[int]
    DNNFDNAPJNJ_FIELD_NUMBER: _ClassVar[int]
    KKLADHFCBFJ_FIELD_NUMBER: _ClassVar[int]
    FGLOHNKKPPG_FIELD_NUMBER: _ClassVar[int]
    DNKAAKGGPAP_FIELD_NUMBER: _ClassVar[int]
    NOBMGICJGBB: _EMEAJKNIEFA_pb2.EMEAJKNIEFA
    EEHFGMOLAGK: _containers.RepeatedCompositeFieldContainer[_EMEAJKNIEFA_pb2.EMEAJKNIEFA]
    NKEDFMOJOHL: int
    ICDLEPJHIDB: int
    MBBKAENBCKD: int
    IFPLLIOOGED: int
    DNNFDNAPJNJ: _MPHAJNOFPHP_pb2.MPHAJNOFPHP
    KKLADHFCBFJ: int
    FGLOHNKKPPG: bool
    DNKAAKGGPAP: bool
    def __init__(self, NOBMGICJGBB: _Optional[_Union[_EMEAJKNIEFA_pb2.EMEAJKNIEFA, _Mapping]] = ..., EEHFGMOLAGK: _Optional[_Iterable[_Union[_EMEAJKNIEFA_pb2.EMEAJKNIEFA, _Mapping]]] = ..., NKEDFMOJOHL: _Optional[int] = ..., ICDLEPJHIDB: _Optional[int] = ..., MBBKAENBCKD: _Optional[int] = ..., IFPLLIOOGED: _Optional[int] = ..., DNNFDNAPJNJ: _Optional[_Union[_MPHAJNOFPHP_pb2.MPHAJNOFPHP, str]] = ..., KKLADHFCBFJ: _Optional[int] = ..., FGLOHNKKPPG: bool = ..., DNKAAKGGPAP: bool = ...) -> None: ...
