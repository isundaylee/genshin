from genshin.packet.proto import JICKPPDLOHC_pb2 as _JICKPPDLOHC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GFNNBABOMDH(_message.Message):
    __slots__ = ("LPFCMMJCIBP", "JHBCBIEOBEP", "LBCDFBDMCJN", "HCJFDJHILAM", "PHGEDMBNPMP")
    LPFCMMJCIBP_FIELD_NUMBER: _ClassVar[int]
    JHBCBIEOBEP_FIELD_NUMBER: _ClassVar[int]
    LBCDFBDMCJN_FIELD_NUMBER: _ClassVar[int]
    HCJFDJHILAM_FIELD_NUMBER: _ClassVar[int]
    PHGEDMBNPMP_FIELD_NUMBER: _ClassVar[int]
    LPFCMMJCIBP: _containers.RepeatedScalarFieldContainer[int]
    JHBCBIEOBEP: _containers.RepeatedCompositeFieldContainer[_JICKPPDLOHC_pb2.JICKPPDLOHC]
    LBCDFBDMCJN: int
    HCJFDJHILAM: bool
    PHGEDMBNPMP: int
    def __init__(self, LPFCMMJCIBP: _Optional[_Iterable[int]] = ..., JHBCBIEOBEP: _Optional[_Iterable[_Union[_JICKPPDLOHC_pb2.JICKPPDLOHC, _Mapping]]] = ..., LBCDFBDMCJN: _Optional[int] = ..., HCJFDJHILAM: bool = ..., PHGEDMBNPMP: _Optional[int] = ...) -> None: ...
