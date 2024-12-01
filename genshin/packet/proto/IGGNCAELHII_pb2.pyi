from genshin.packet.proto import MIFDFAIHDDA_pb2 as _MIFDFAIHDDA_pb2
from genshin.packet.proto import DHNBIHGAEJB_pb2 as _DHNBIHGAEJB_pb2
from genshin.packet.proto import GGJNMDCOEHI_pb2 as _GGJNMDCOEHI_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IGGNCAELHII(_message.Message):
    __slots__ = ("MBDHJJOHCKO", "NPMJPLLMFBN", "CMPMHDGCFKH", "FMFEECNJNMO", "JPDBMDLEEEC", "HKEGEBJNJJD", "DHHJAJJNCOI", "KDJIFCPBGEN", "MEMEFFOINGB")
    class CMPMHDGCFKHEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _GGJNMDCOEHI_pb2.GGJNMDCOEHI
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_GGJNMDCOEHI_pb2.GGJNMDCOEHI, _Mapping]] = ...) -> None: ...
    MBDHJJOHCKO_FIELD_NUMBER: _ClassVar[int]
    NPMJPLLMFBN_FIELD_NUMBER: _ClassVar[int]
    CMPMHDGCFKH_FIELD_NUMBER: _ClassVar[int]
    FMFEECNJNMO_FIELD_NUMBER: _ClassVar[int]
    JPDBMDLEEEC_FIELD_NUMBER: _ClassVar[int]
    HKEGEBJNJJD_FIELD_NUMBER: _ClassVar[int]
    DHHJAJJNCOI_FIELD_NUMBER: _ClassVar[int]
    KDJIFCPBGEN_FIELD_NUMBER: _ClassVar[int]
    MEMEFFOINGB_FIELD_NUMBER: _ClassVar[int]
    MBDHJJOHCKO: _containers.RepeatedCompositeFieldContainer[_MIFDFAIHDDA_pb2.MIFDFAIHDDA]
    NPMJPLLMFBN: _DHNBIHGAEJB_pb2.DHNBIHGAEJB
    CMPMHDGCFKH: _containers.MessageMap[int, _GGJNMDCOEHI_pb2.GGJNMDCOEHI]
    FMFEECNJNMO: _containers.RepeatedScalarFieldContainer[int]
    JPDBMDLEEEC: int
    HKEGEBJNJJD: int
    DHHJAJJNCOI: int
    KDJIFCPBGEN: int
    MEMEFFOINGB: int
    def __init__(self, MBDHJJOHCKO: _Optional[_Iterable[_Union[_MIFDFAIHDDA_pb2.MIFDFAIHDDA, _Mapping]]] = ..., NPMJPLLMFBN: _Optional[_Union[_DHNBIHGAEJB_pb2.DHNBIHGAEJB, _Mapping]] = ..., CMPMHDGCFKH: _Optional[_Mapping[int, _GGJNMDCOEHI_pb2.GGJNMDCOEHI]] = ..., FMFEECNJNMO: _Optional[_Iterable[int]] = ..., JPDBMDLEEEC: _Optional[int] = ..., HKEGEBJNJJD: _Optional[int] = ..., DHHJAJJNCOI: _Optional[int] = ..., KDJIFCPBGEN: _Optional[int] = ..., MEMEFFOINGB: _Optional[int] = ...) -> None: ...
