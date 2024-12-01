from genshin.packet.proto import OMBEIFNNEDF_pb2 as _OMBEIFNNEDF_pb2
from genshin.packet.proto import HJPEIAODCBK_pb2 as _HJPEIAODCBK_pb2
from genshin.packet.proto import NLOBHEMPBEM_pb2 as _NLOBHEMPBEM_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DPDMGOJJJLE(_message.Message):
    __slots__ = ("KDOJKDMIAOM", "DNGFFHFBBKL", "COJOBIKFHOD", "EOFHLOIMPMK", "OOIPGFEDJMN", "KONANKACIEM", "IGCFEKLJNMJ", "MBBKAENBCKD", "MNCDPPBPPFA", "MHJHGIMLHLN")
    KDOJKDMIAOM_FIELD_NUMBER: _ClassVar[int]
    DNGFFHFBBKL_FIELD_NUMBER: _ClassVar[int]
    COJOBIKFHOD_FIELD_NUMBER: _ClassVar[int]
    EOFHLOIMPMK_FIELD_NUMBER: _ClassVar[int]
    OOIPGFEDJMN_FIELD_NUMBER: _ClassVar[int]
    KONANKACIEM_FIELD_NUMBER: _ClassVar[int]
    IGCFEKLJNMJ_FIELD_NUMBER: _ClassVar[int]
    MBBKAENBCKD_FIELD_NUMBER: _ClassVar[int]
    MNCDPPBPPFA_FIELD_NUMBER: _ClassVar[int]
    MHJHGIMLHLN_FIELD_NUMBER: _ClassVar[int]
    KDOJKDMIAOM: _containers.RepeatedCompositeFieldContainer[_OMBEIFNNEDF_pb2.OMBEIFNNEDF]
    DNGFFHFBBKL: _containers.RepeatedCompositeFieldContainer[_HJPEIAODCBK_pb2.HJPEIAODCBK]
    COJOBIKFHOD: int
    EOFHLOIMPMK: int
    OOIPGFEDJMN: int
    KONANKACIEM: int
    IGCFEKLJNMJ: _NLOBHEMPBEM_pb2.NLOBHEMPBEM
    MBBKAENBCKD: int
    MNCDPPBPPFA: bool
    MHJHGIMLHLN: int
    def __init__(self, KDOJKDMIAOM: _Optional[_Iterable[_Union[_OMBEIFNNEDF_pb2.OMBEIFNNEDF, _Mapping]]] = ..., DNGFFHFBBKL: _Optional[_Iterable[_Union[_HJPEIAODCBK_pb2.HJPEIAODCBK, _Mapping]]] = ..., COJOBIKFHOD: _Optional[int] = ..., EOFHLOIMPMK: _Optional[int] = ..., OOIPGFEDJMN: _Optional[int] = ..., KONANKACIEM: _Optional[int] = ..., IGCFEKLJNMJ: _Optional[_Union[_NLOBHEMPBEM_pb2.NLOBHEMPBEM, str]] = ..., MBBKAENBCKD: _Optional[int] = ..., MNCDPPBPPFA: bool = ..., MHJHGIMLHLN: _Optional[int] = ...) -> None: ...
