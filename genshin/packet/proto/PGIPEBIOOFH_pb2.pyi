from genshin.packet.proto import JICKPPDLOHC_pb2 as _JICKPPDLOHC_pb2
from genshin.packet.proto import GPJGHADEOEN_pb2 as _GPJGHADEOEN_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PGIPEBIOOFH(_message.Message):
    __slots__ = ("BFPMIHHHMIP", "AMFBNEJGHMA", "HPAGCFJIEKP", "GMGHAJIDBOE")
    BFPMIHHHMIP_FIELD_NUMBER: _ClassVar[int]
    AMFBNEJGHMA_FIELD_NUMBER: _ClassVar[int]
    HPAGCFJIEKP_FIELD_NUMBER: _ClassVar[int]
    GMGHAJIDBOE_FIELD_NUMBER: _ClassVar[int]
    BFPMIHHHMIP: str
    AMFBNEJGHMA: _containers.RepeatedCompositeFieldContainer[_JICKPPDLOHC_pb2.JICKPPDLOHC]
    HPAGCFJIEKP: _containers.RepeatedCompositeFieldContainer[_GPJGHADEOEN_pb2.GPJGHADEOEN]
    GMGHAJIDBOE: int
    def __init__(self, BFPMIHHHMIP: _Optional[str] = ..., AMFBNEJGHMA: _Optional[_Iterable[_Union[_JICKPPDLOHC_pb2.JICKPPDLOHC, _Mapping]]] = ..., HPAGCFJIEKP: _Optional[_Iterable[_Union[_GPJGHADEOEN_pb2.GPJGHADEOEN, _Mapping]]] = ..., GMGHAJIDBOE: _Optional[int] = ...) -> None: ...
