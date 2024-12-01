from genshin.packet.proto import ICANCIPFHNK_pb2 as _ICANCIPFHNK_pb2
from genshin.packet.proto import JICKPPDLOHC_pb2 as _JICKPPDLOHC_pb2
from genshin.packet.proto import NBHHIAKNANM_pb2 as _NBHHIAKNANM_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JEIDECDIDLE(_message.Message):
    __slots__ = ("KCBLAFECKCH", "ODPNMGFHEOM", "FJEAHEFOLEL", "MDNEHEHJMEP", "KLPOGHNLINN", "DGINEEPPKLL", "GKONEBEGNHL", "MPFLDFDOGAI")
    KCBLAFECKCH_FIELD_NUMBER: _ClassVar[int]
    ODPNMGFHEOM_FIELD_NUMBER: _ClassVar[int]
    FJEAHEFOLEL_FIELD_NUMBER: _ClassVar[int]
    MDNEHEHJMEP_FIELD_NUMBER: _ClassVar[int]
    KLPOGHNLINN_FIELD_NUMBER: _ClassVar[int]
    DGINEEPPKLL_FIELD_NUMBER: _ClassVar[int]
    GKONEBEGNHL_FIELD_NUMBER: _ClassVar[int]
    MPFLDFDOGAI_FIELD_NUMBER: _ClassVar[int]
    KCBLAFECKCH: _ICANCIPFHNK_pb2.ICANCIPFHNK
    ODPNMGFHEOM: _ICANCIPFHNK_pb2.ICANCIPFHNK
    FJEAHEFOLEL: _containers.RepeatedCompositeFieldContainer[_JICKPPDLOHC_pb2.JICKPPDLOHC]
    MDNEHEHJMEP: _containers.RepeatedCompositeFieldContainer[_NBHHIAKNANM_pb2.NBHHIAKNANM]
    KLPOGHNLINN: _containers.RepeatedScalarFieldContainer[int]
    DGINEEPPKLL: _containers.RepeatedScalarFieldContainer[int]
    GKONEBEGNHL: _containers.RepeatedScalarFieldContainer[int]
    MPFLDFDOGAI: bool
    def __init__(self, KCBLAFECKCH: _Optional[_Union[_ICANCIPFHNK_pb2.ICANCIPFHNK, _Mapping]] = ..., ODPNMGFHEOM: _Optional[_Union[_ICANCIPFHNK_pb2.ICANCIPFHNK, _Mapping]] = ..., FJEAHEFOLEL: _Optional[_Iterable[_Union[_JICKPPDLOHC_pb2.JICKPPDLOHC, _Mapping]]] = ..., MDNEHEHJMEP: _Optional[_Iterable[_Union[_NBHHIAKNANM_pb2.NBHHIAKNANM, _Mapping]]] = ..., KLPOGHNLINN: _Optional[_Iterable[int]] = ..., DGINEEPPKLL: _Optional[_Iterable[int]] = ..., GKONEBEGNHL: _Optional[_Iterable[int]] = ..., MPFLDFDOGAI: bool = ...) -> None: ...
