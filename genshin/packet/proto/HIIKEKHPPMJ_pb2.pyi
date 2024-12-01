from genshin.packet.proto import JKFFGCHKLAA_pb2 as _JKFFGCHKLAA_pb2
from genshin.packet.proto import GLDPGOIFKKJ_pb2 as _GLDPGOIFKKJ_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HIIKEKHPPMJ(_message.Message):
    __slots__ = ("ACCCBLMCDOA", "NEHPGMLDKMF", "NIEKGOMDMOC", "HGGEHLMHKMP", "IBKIHEHNHLH", "MPNJAOCKMAH")
    ACCCBLMCDOA_FIELD_NUMBER: _ClassVar[int]
    NEHPGMLDKMF_FIELD_NUMBER: _ClassVar[int]
    NIEKGOMDMOC_FIELD_NUMBER: _ClassVar[int]
    HGGEHLMHKMP_FIELD_NUMBER: _ClassVar[int]
    IBKIHEHNHLH_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    ACCCBLMCDOA: _containers.RepeatedCompositeFieldContainer[_JKFFGCHKLAA_pb2.JKFFGCHKLAA]
    NEHPGMLDKMF: _containers.RepeatedCompositeFieldContainer[_GLDPGOIFKKJ_pb2.GLDPGOIFKKJ]
    NIEKGOMDMOC: bool
    HGGEHLMHKMP: int
    IBKIHEHNHLH: int
    MPNJAOCKMAH: int
    def __init__(self, ACCCBLMCDOA: _Optional[_Iterable[_Union[_JKFFGCHKLAA_pb2.JKFFGCHKLAA, _Mapping]]] = ..., NEHPGMLDKMF: _Optional[_Iterable[_Union[_GLDPGOIFKKJ_pb2.GLDPGOIFKKJ, _Mapping]]] = ..., NIEKGOMDMOC: bool = ..., HGGEHLMHKMP: _Optional[int] = ..., IBKIHEHNHLH: _Optional[int] = ..., MPNJAOCKMAH: _Optional[int] = ...) -> None: ...
