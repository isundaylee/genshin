from genshin.packet.proto import KBBAJAALEEJ_pb2 as _KBBAJAALEEJ_pb2
from genshin.packet.proto import JICKPPDLOHC_pb2 as _JICKPPDLOHC_pb2
from genshin.packet.proto import NLOBHEMPBEM_pb2 as _NLOBHEMPBEM_pb2
from genshin.packet.proto import KABBEPLLGOJ_pb2 as _KABBEPLLGOJ_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NOPFEHEJLEH(_message.Message):
    __slots__ = ("PLMDDOEIFPL", "JDPOHCKAOAH", "OFPGJHPIFPO", "JHBCBIEOBEP", "FADINCNPBMD", "IGCFEKLJNMJ", "KONANKACIEM", "EOFHLOIMPMK", "IMIOGMDOKCB")
    PLMDDOEIFPL_FIELD_NUMBER: _ClassVar[int]
    JDPOHCKAOAH_FIELD_NUMBER: _ClassVar[int]
    OFPGJHPIFPO_FIELD_NUMBER: _ClassVar[int]
    JHBCBIEOBEP_FIELD_NUMBER: _ClassVar[int]
    FADINCNPBMD_FIELD_NUMBER: _ClassVar[int]
    IGCFEKLJNMJ_FIELD_NUMBER: _ClassVar[int]
    KONANKACIEM_FIELD_NUMBER: _ClassVar[int]
    EOFHLOIMPMK_FIELD_NUMBER: _ClassVar[int]
    IMIOGMDOKCB_FIELD_NUMBER: _ClassVar[int]
    PLMDDOEIFPL: _containers.RepeatedScalarFieldContainer[int]
    JDPOHCKAOAH: _containers.RepeatedScalarFieldContainer[int]
    OFPGJHPIFPO: _KBBAJAALEEJ_pb2.KBBAJAALEEJ
    JHBCBIEOBEP: _containers.RepeatedCompositeFieldContainer[_JICKPPDLOHC_pb2.JICKPPDLOHC]
    FADINCNPBMD: bool
    IGCFEKLJNMJ: _NLOBHEMPBEM_pb2.NLOBHEMPBEM
    KONANKACIEM: int
    EOFHLOIMPMK: int
    IMIOGMDOKCB: _KABBEPLLGOJ_pb2.KABBEPLLGOJ
    def __init__(self, PLMDDOEIFPL: _Optional[_Iterable[int]] = ..., JDPOHCKAOAH: _Optional[_Iterable[int]] = ..., OFPGJHPIFPO: _Optional[_Union[_KBBAJAALEEJ_pb2.KBBAJAALEEJ, _Mapping]] = ..., JHBCBIEOBEP: _Optional[_Iterable[_Union[_JICKPPDLOHC_pb2.JICKPPDLOHC, _Mapping]]] = ..., FADINCNPBMD: bool = ..., IGCFEKLJNMJ: _Optional[_Union[_NLOBHEMPBEM_pb2.NLOBHEMPBEM, str]] = ..., KONANKACIEM: _Optional[int] = ..., EOFHLOIMPMK: _Optional[int] = ..., IMIOGMDOKCB: _Optional[_Union[_KABBEPLLGOJ_pb2.KABBEPLLGOJ, str]] = ...) -> None: ...
