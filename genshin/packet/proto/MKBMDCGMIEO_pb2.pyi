from genshin.packet.proto import BIFEDDINLOD_pb2 as _BIFEDDINLOD_pb2
from genshin.packet.proto import GMCJNDHELFG_pb2 as _GMCJNDHELFG_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MKBMDCGMIEO(_message.Message):
    __slots__ = ("OBHPOELIAPM", "BHMHDGKHBCE", "MFHKFMFACIN", "BIPADACDOFI", "LAKINGCAKKD", "OOIPGFEDJMN", "IONHGHGAJGG", "guid", "MBBKAENBCKD")
    OBHPOELIAPM_FIELD_NUMBER: _ClassVar[int]
    BHMHDGKHBCE_FIELD_NUMBER: _ClassVar[int]
    MFHKFMFACIN_FIELD_NUMBER: _ClassVar[int]
    BIPADACDOFI_FIELD_NUMBER: _ClassVar[int]
    LAKINGCAKKD_FIELD_NUMBER: _ClassVar[int]
    OOIPGFEDJMN_FIELD_NUMBER: _ClassVar[int]
    IONHGHGAJGG_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    MBBKAENBCKD_FIELD_NUMBER: _ClassVar[int]
    OBHPOELIAPM: _containers.RepeatedCompositeFieldContainer[_BIFEDDINLOD_pb2.BIFEDDINLOD]
    BHMHDGKHBCE: _containers.RepeatedCompositeFieldContainer[_GMCJNDHELFG_pb2.GMCJNDHELFG]
    MFHKFMFACIN: _containers.RepeatedScalarFieldContainer[int]
    BIPADACDOFI: _containers.RepeatedScalarFieldContainer[int]
    LAKINGCAKKD: bool
    OOIPGFEDJMN: int
    IONHGHGAJGG: int
    guid: int
    MBBKAENBCKD: int
    def __init__(self, OBHPOELIAPM: _Optional[_Iterable[_Union[_BIFEDDINLOD_pb2.BIFEDDINLOD, _Mapping]]] = ..., BHMHDGKHBCE: _Optional[_Iterable[_Union[_GMCJNDHELFG_pb2.GMCJNDHELFG, _Mapping]]] = ..., MFHKFMFACIN: _Optional[_Iterable[int]] = ..., BIPADACDOFI: _Optional[_Iterable[int]] = ..., LAKINGCAKKD: bool = ..., OOIPGFEDJMN: _Optional[int] = ..., IONHGHGAJGG: _Optional[int] = ..., guid: _Optional[int] = ..., MBBKAENBCKD: _Optional[int] = ...) -> None: ...
