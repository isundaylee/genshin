from genshin.packet.proto import JICKPPDLOHC_pb2 as _JICKPPDLOHC_pb2
from genshin.packet.proto import LPNOKFFDBNE_pb2 as _LPNOKFFDBNE_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CGCHKPDKPEH(_message.Message):
    __slots__ = ("INPFJMANEHI", "FPKNCKLMOHJ", "JGEFHAHAFKI", "LIOELANODLF", "JFKEAAOFEKJ")
    INPFJMANEHI_FIELD_NUMBER: _ClassVar[int]
    FPKNCKLMOHJ_FIELD_NUMBER: _ClassVar[int]
    JGEFHAHAFKI_FIELD_NUMBER: _ClassVar[int]
    LIOELANODLF_FIELD_NUMBER: _ClassVar[int]
    JFKEAAOFEKJ_FIELD_NUMBER: _ClassVar[int]
    INPFJMANEHI: _containers.RepeatedCompositeFieldContainer[_JICKPPDLOHC_pb2.JICKPPDLOHC]
    FPKNCKLMOHJ: _containers.RepeatedCompositeFieldContainer[_LPNOKFFDBNE_pb2.LPNOKFFDBNE]
    JGEFHAHAFKI: _JICKPPDLOHC_pb2.JICKPPDLOHC
    LIOELANODLF: bool
    JFKEAAOFEKJ: bool
    def __init__(self, INPFJMANEHI: _Optional[_Iterable[_Union[_JICKPPDLOHC_pb2.JICKPPDLOHC, _Mapping]]] = ..., FPKNCKLMOHJ: _Optional[_Iterable[_Union[_LPNOKFFDBNE_pb2.LPNOKFFDBNE, _Mapping]]] = ..., JGEFHAHAFKI: _Optional[_Union[_JICKPPDLOHC_pb2.JICKPPDLOHC, _Mapping]] = ..., LIOELANODLF: bool = ..., JFKEAAOFEKJ: bool = ...) -> None: ...
