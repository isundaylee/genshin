from genshin.packet.proto import GLDPGOIFKKJ_pb2 as _GLDPGOIFKKJ_pb2
from genshin.packet.proto import KIPKGCACPBK_pb2 as _KIPKGCACPBK_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CGOIHCDFFEJ(_message.Message):
    __slots__ = ("NEHPGMLDKMF", "EFCDELGMMKG")
    NEHPGMLDKMF_FIELD_NUMBER: _ClassVar[int]
    EFCDELGMMKG_FIELD_NUMBER: _ClassVar[int]
    NEHPGMLDKMF: _containers.RepeatedCompositeFieldContainer[_GLDPGOIFKKJ_pb2.GLDPGOIFKKJ]
    EFCDELGMMKG: _containers.RepeatedCompositeFieldContainer[_KIPKGCACPBK_pb2.KIPKGCACPBK]
    def __init__(self, NEHPGMLDKMF: _Optional[_Iterable[_Union[_GLDPGOIFKKJ_pb2.GLDPGOIFKKJ, _Mapping]]] = ..., EFCDELGMMKG: _Optional[_Iterable[_Union[_KIPKGCACPBK_pb2.KIPKGCACPBK, _Mapping]]] = ...) -> None: ...
