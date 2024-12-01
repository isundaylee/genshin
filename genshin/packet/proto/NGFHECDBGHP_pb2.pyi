from genshin.packet.proto import MPFODNPCFDI_pb2 as _MPFODNPCFDI_pb2
from genshin.packet.proto import BMIDAFBCOMP_pb2 as _BMIDAFBCOMP_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NGFHECDBGHP(_message.Message):
    __slots__ = ("LCPMKKBNBFB", "OPANIFFJCHE")
    LCPMKKBNBFB_FIELD_NUMBER: _ClassVar[int]
    OPANIFFJCHE_FIELD_NUMBER: _ClassVar[int]
    LCPMKKBNBFB: _containers.RepeatedCompositeFieldContainer[_MPFODNPCFDI_pb2.MPFODNPCFDI]
    OPANIFFJCHE: _BMIDAFBCOMP_pb2.BMIDAFBCOMP
    def __init__(self, LCPMKKBNBFB: _Optional[_Iterable[_Union[_MPFODNPCFDI_pb2.MPFODNPCFDI, _Mapping]]] = ..., OPANIFFJCHE: _Optional[_Union[_BMIDAFBCOMP_pb2.BMIDAFBCOMP, str]] = ...) -> None: ...
