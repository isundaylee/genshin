from genshin.packet.proto import LGPPBGENJBN_pb2 as _LGPPBGENJBN_pb2
from genshin.packet.proto import MGAIJNJIOJK_pb2 as _MGAIJNJIOJK_pb2
from genshin.packet.proto import LHIOAJDDIPL_pb2 as _LHIOAJDDIPL_pb2
from genshin.packet.proto import DFIPJEPBGPI_pb2 as _DFIPJEPBGPI_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OFCLOOBNFGL(_message.Message):
    __slots__ = ("HLOHGJIBKJI", "FKJPHKIHBMD", "CMGHNOODLIG", "EEBOKMCFEPE", "LALOFCFEJGG", "FCLHDJMAOPL", "PGLOENAGAFI", "DBCJOJCLNAD", "EINPPDEKDHB", "CDBFPFOJBIJ", "MBBKAENBCKD")
    class FKJPHKIHBMDEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    HLOHGJIBKJI_FIELD_NUMBER: _ClassVar[int]
    FKJPHKIHBMD_FIELD_NUMBER: _ClassVar[int]
    CMGHNOODLIG_FIELD_NUMBER: _ClassVar[int]
    EEBOKMCFEPE_FIELD_NUMBER: _ClassVar[int]
    LALOFCFEJGG_FIELD_NUMBER: _ClassVar[int]
    FCLHDJMAOPL_FIELD_NUMBER: _ClassVar[int]
    PGLOENAGAFI_FIELD_NUMBER: _ClassVar[int]
    DBCJOJCLNAD_FIELD_NUMBER: _ClassVar[int]
    EINPPDEKDHB_FIELD_NUMBER: _ClassVar[int]
    CDBFPFOJBIJ_FIELD_NUMBER: _ClassVar[int]
    MBBKAENBCKD_FIELD_NUMBER: _ClassVar[int]
    HLOHGJIBKJI: _containers.RepeatedScalarFieldContainer[int]
    FKJPHKIHBMD: _containers.ScalarMap[int, int]
    CMGHNOODLIG: _containers.RepeatedScalarFieldContainer[int]
    EEBOKMCFEPE: _containers.RepeatedCompositeFieldContainer[_LGPPBGENJBN_pb2.LGPPBGENJBN]
    LALOFCFEJGG: _containers.RepeatedScalarFieldContainer[int]
    FCLHDJMAOPL: _containers.RepeatedCompositeFieldContainer[_MGAIJNJIOJK_pb2.MGAIJNJIOJK]
    PGLOENAGAFI: _containers.RepeatedCompositeFieldContainer[_LHIOAJDDIPL_pb2.LHIOAJDDIPL]
    DBCJOJCLNAD: int
    EINPPDEKDHB: int
    CDBFPFOJBIJ: _DFIPJEPBGPI_pb2.DFIPJEPBGPI
    MBBKAENBCKD: int
    def __init__(self, HLOHGJIBKJI: _Optional[_Iterable[int]] = ..., FKJPHKIHBMD: _Optional[_Mapping[int, int]] = ..., CMGHNOODLIG: _Optional[_Iterable[int]] = ..., EEBOKMCFEPE: _Optional[_Iterable[_Union[_LGPPBGENJBN_pb2.LGPPBGENJBN, _Mapping]]] = ..., LALOFCFEJGG: _Optional[_Iterable[int]] = ..., FCLHDJMAOPL: _Optional[_Iterable[_Union[_MGAIJNJIOJK_pb2.MGAIJNJIOJK, _Mapping]]] = ..., PGLOENAGAFI: _Optional[_Iterable[_Union[_LHIOAJDDIPL_pb2.LHIOAJDDIPL, _Mapping]]] = ..., DBCJOJCLNAD: _Optional[int] = ..., EINPPDEKDHB: _Optional[int] = ..., CDBFPFOJBIJ: _Optional[_Union[_DFIPJEPBGPI_pb2.DFIPJEPBGPI, str]] = ..., MBBKAENBCKD: _Optional[int] = ...) -> None: ...
