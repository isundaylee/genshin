from genshin.packet.proto import ONFPPNPPNEG_pb2 as _ONFPPNPPNEG_pb2
from genshin.packet.proto import GKEGLHBKJPL_pb2 as _GKEGLHBKJPL_pb2
from genshin.packet.proto import EJCCPJJDIEN_pb2 as _EJCCPJJDIEN_pb2
from genshin.packet.proto import MHCEOAICLJF_pb2 as _MHCEOAICLJF_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IBKGCGGJODP(_message.Message):
    __slots__ = ("GAFMCJBMFAE", "FFANFEEJALE", "BCLBHOBHBIM", "PIKPHKJINIB", "MPFLDFDOGAI")
    GAFMCJBMFAE_FIELD_NUMBER: _ClassVar[int]
    FFANFEEJALE_FIELD_NUMBER: _ClassVar[int]
    BCLBHOBHBIM_FIELD_NUMBER: _ClassVar[int]
    PIKPHKJINIB_FIELD_NUMBER: _ClassVar[int]
    MPFLDFDOGAI_FIELD_NUMBER: _ClassVar[int]
    GAFMCJBMFAE: _ONFPPNPPNEG_pb2.ONFPPNPPNEG
    FFANFEEJALE: _GKEGLHBKJPL_pb2.GKEGLHBKJPL
    BCLBHOBHBIM: _EJCCPJJDIEN_pb2.EJCCPJJDIEN
    PIKPHKJINIB: _MHCEOAICLJF_pb2.MHCEOAICLJF
    MPFLDFDOGAI: bool
    def __init__(self, GAFMCJBMFAE: _Optional[_Union[_ONFPPNPPNEG_pb2.ONFPPNPPNEG, _Mapping]] = ..., FFANFEEJALE: _Optional[_Union[_GKEGLHBKJPL_pb2.GKEGLHBKJPL, _Mapping]] = ..., BCLBHOBHBIM: _Optional[_Union[_EJCCPJJDIEN_pb2.EJCCPJJDIEN, _Mapping]] = ..., PIKPHKJINIB: _Optional[_Union[_MHCEOAICLJF_pb2.MHCEOAICLJF, _Mapping]] = ..., MPFLDFDOGAI: bool = ...) -> None: ...
