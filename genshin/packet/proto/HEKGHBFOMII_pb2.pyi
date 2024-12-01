from genshin.packet.proto import GIIBEFAJGBK_pb2 as _GIIBEFAJGBK_pb2
from genshin.packet.proto import ELNAJEHAMJL_pb2 as _ELNAJEHAMJL_pb2
from genshin.packet.proto import BJKFJPJDMIC_pb2 as _BJKFJPJDMIC_pb2
from genshin.packet.proto import ENLAFOLMIOG_pb2 as _ENLAFOLMIOG_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HEKGHBFOMII(_message.Message):
    __slots__ = ("DKIMEEMCDIO", "MNFCNBIEPNH", "LFAPMGLGGBG", "CJBJINIEICP", "HJEHLPBGNIM", "INDIMDAICCE", "BJKBOPGGPJM", "IPDBKMDEOMF")
    DKIMEEMCDIO_FIELD_NUMBER: _ClassVar[int]
    MNFCNBIEPNH_FIELD_NUMBER: _ClassVar[int]
    LFAPMGLGGBG_FIELD_NUMBER: _ClassVar[int]
    CJBJINIEICP_FIELD_NUMBER: _ClassVar[int]
    HJEHLPBGNIM_FIELD_NUMBER: _ClassVar[int]
    INDIMDAICCE_FIELD_NUMBER: _ClassVar[int]
    BJKBOPGGPJM_FIELD_NUMBER: _ClassVar[int]
    IPDBKMDEOMF_FIELD_NUMBER: _ClassVar[int]
    DKIMEEMCDIO: _containers.RepeatedScalarFieldContainer[int]
    MNFCNBIEPNH: _containers.RepeatedCompositeFieldContainer[_GIIBEFAJGBK_pb2.GIIBEFAJGBK]
    LFAPMGLGGBG: _containers.RepeatedScalarFieldContainer[int]
    CJBJINIEICP: _containers.RepeatedCompositeFieldContainer[_ELNAJEHAMJL_pb2.ELNAJEHAMJL]
    HJEHLPBGNIM: _containers.RepeatedScalarFieldContainer[int]
    INDIMDAICCE: _containers.RepeatedCompositeFieldContainer[_BJKFJPJDMIC_pb2.BJKFJPJDMIC]
    BJKBOPGGPJM: _containers.RepeatedCompositeFieldContainer[_ENLAFOLMIOG_pb2.ENLAFOLMIOG]
    IPDBKMDEOMF: bool
    def __init__(self, DKIMEEMCDIO: _Optional[_Iterable[int]] = ..., MNFCNBIEPNH: _Optional[_Iterable[_Union[_GIIBEFAJGBK_pb2.GIIBEFAJGBK, _Mapping]]] = ..., LFAPMGLGGBG: _Optional[_Iterable[int]] = ..., CJBJINIEICP: _Optional[_Iterable[_Union[_ELNAJEHAMJL_pb2.ELNAJEHAMJL, _Mapping]]] = ..., HJEHLPBGNIM: _Optional[_Iterable[int]] = ..., INDIMDAICCE: _Optional[_Iterable[_Union[_BJKFJPJDMIC_pb2.BJKFJPJDMIC, _Mapping]]] = ..., BJKBOPGGPJM: _Optional[_Iterable[_Union[_ENLAFOLMIOG_pb2.ENLAFOLMIOG, _Mapping]]] = ..., IPDBKMDEOMF: bool = ...) -> None: ...
