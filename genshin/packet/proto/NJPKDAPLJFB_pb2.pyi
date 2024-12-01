from genshin.packet.proto import HJPEIAODCBK_pb2 as _HJPEIAODCBK_pb2
from genshin.packet.proto import NLOBHEMPBEM_pb2 as _NLOBHEMPBEM_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NJPKDAPLJFB(_message.Message):
    __slots__ = ("DNGFFHFBBKL", "HGALNDAOJLP", "IGCFEKLJNMJ", "KHOONEPKKNP", "KONANKACIEM", "AJCGKKPCCGD")
    DNGFFHFBBKL_FIELD_NUMBER: _ClassVar[int]
    HGALNDAOJLP_FIELD_NUMBER: _ClassVar[int]
    IGCFEKLJNMJ_FIELD_NUMBER: _ClassVar[int]
    KHOONEPKKNP_FIELD_NUMBER: _ClassVar[int]
    KONANKACIEM_FIELD_NUMBER: _ClassVar[int]
    AJCGKKPCCGD_FIELD_NUMBER: _ClassVar[int]
    DNGFFHFBBKL: _containers.RepeatedCompositeFieldContainer[_HJPEIAODCBK_pb2.HJPEIAODCBK]
    HGALNDAOJLP: int
    IGCFEKLJNMJ: _NLOBHEMPBEM_pb2.NLOBHEMPBEM
    KHOONEPKKNP: int
    KONANKACIEM: int
    AJCGKKPCCGD: int
    def __init__(self, DNGFFHFBBKL: _Optional[_Iterable[_Union[_HJPEIAODCBK_pb2.HJPEIAODCBK, _Mapping]]] = ..., HGALNDAOJLP: _Optional[int] = ..., IGCFEKLJNMJ: _Optional[_Union[_NLOBHEMPBEM_pb2.NLOBHEMPBEM, str]] = ..., KHOONEPKKNP: _Optional[int] = ..., KONANKACIEM: _Optional[int] = ..., AJCGKKPCCGD: _Optional[int] = ...) -> None: ...
