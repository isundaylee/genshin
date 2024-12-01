from genshin.packet.proto import LMPINLNNPBD_pb2 as _LMPINLNNPBD_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PICCFJIDMML(_message.Message):
    __slots__ = ("KKPKGGPFPIM", "NIDHJMLJJII", "NMIPKMFLACP", "FCLOHOMHHHO", "MHJHGIMLHLN", "HKEGEBJNJJD")
    KKPKGGPFPIM_FIELD_NUMBER: _ClassVar[int]
    NIDHJMLJJII_FIELD_NUMBER: _ClassVar[int]
    NMIPKMFLACP_FIELD_NUMBER: _ClassVar[int]
    FCLOHOMHHHO_FIELD_NUMBER: _ClassVar[int]
    MHJHGIMLHLN_FIELD_NUMBER: _ClassVar[int]
    HKEGEBJNJJD_FIELD_NUMBER: _ClassVar[int]
    KKPKGGPFPIM: _containers.RepeatedScalarFieldContainer[int]
    NIDHJMLJJII: _containers.RepeatedCompositeFieldContainer[_LMPINLNNPBD_pb2.LMPINLNNPBD]
    NMIPKMFLACP: int
    FCLOHOMHHHO: int
    MHJHGIMLHLN: int
    HKEGEBJNJJD: int
    def __init__(self, KKPKGGPFPIM: _Optional[_Iterable[int]] = ..., NIDHJMLJJII: _Optional[_Iterable[_Union[_LMPINLNNPBD_pb2.LMPINLNNPBD, _Mapping]]] = ..., NMIPKMFLACP: _Optional[int] = ..., FCLOHOMHHHO: _Optional[int] = ..., MHJHGIMLHLN: _Optional[int] = ..., HKEGEBJNJJD: _Optional[int] = ...) -> None: ...
