from genshin.packet.proto import OADJBKDJNPL_pb2 as _OADJBKDJNPL_pb2
from genshin.packet.proto import MJPKECMOIGA_pb2 as _MJPKECMOIGA_pb2
from genshin.packet.proto import FGGKIFNGDON_pb2 as _FGGKIFNGDON_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HOLHJCEKDKH(_message.Message):
    __slots__ = ("EOMNMODEDFD", "CEMLGAAHAOM", "JGCKBJJGIAF", "FHKNGCBGDJL", "CJIHNOCINNM", "LOKPPLOEOFM", "GMGICOPOPFK", "EJNINFFFKJP", "ALOOBPBNDDH", "OLLLEIKDNAN", "BLMGFJBAFKB", "MJMLCOHBLPL", "FDDEHDHBABM", "KCJGPLKNPCL", "MGCBKEMOADN", "JLFGOPMDPDK", "PEFKMBHJCDL")
    class JGCKBJJGIAFEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class LOKPPLOEOFMEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    EOMNMODEDFD_FIELD_NUMBER: _ClassVar[int]
    CEMLGAAHAOM_FIELD_NUMBER: _ClassVar[int]
    JGCKBJJGIAF_FIELD_NUMBER: _ClassVar[int]
    FHKNGCBGDJL_FIELD_NUMBER: _ClassVar[int]
    CJIHNOCINNM_FIELD_NUMBER: _ClassVar[int]
    LOKPPLOEOFM_FIELD_NUMBER: _ClassVar[int]
    GMGICOPOPFK_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    ALOOBPBNDDH_FIELD_NUMBER: _ClassVar[int]
    OLLLEIKDNAN_FIELD_NUMBER: _ClassVar[int]
    BLMGFJBAFKB_FIELD_NUMBER: _ClassVar[int]
    MJMLCOHBLPL_FIELD_NUMBER: _ClassVar[int]
    FDDEHDHBABM_FIELD_NUMBER: _ClassVar[int]
    KCJGPLKNPCL_FIELD_NUMBER: _ClassVar[int]
    MGCBKEMOADN_FIELD_NUMBER: _ClassVar[int]
    JLFGOPMDPDK_FIELD_NUMBER: _ClassVar[int]
    PEFKMBHJCDL_FIELD_NUMBER: _ClassVar[int]
    EOMNMODEDFD: _OADJBKDJNPL_pb2.OADJBKDJNPL
    CEMLGAAHAOM: _OADJBKDJNPL_pb2.OADJBKDJNPL
    JGCKBJJGIAF: _containers.ScalarMap[int, int]
    FHKNGCBGDJL: _containers.RepeatedCompositeFieldContainer[_MJPKECMOIGA_pb2.MJPKECMOIGA]
    CJIHNOCINNM: _FGGKIFNGDON_pb2.FGGKIFNGDON
    LOKPPLOEOFM: _containers.ScalarMap[int, int]
    GMGICOPOPFK: int
    EJNINFFFKJP: int
    ALOOBPBNDDH: int
    OLLLEIKDNAN: int
    BLMGFJBAFKB: int
    MJMLCOHBLPL: int
    FDDEHDHBABM: bool
    KCJGPLKNPCL: bool
    MGCBKEMOADN: int
    JLFGOPMDPDK: int
    PEFKMBHJCDL: int
    def __init__(self, EOMNMODEDFD: _Optional[_Union[_OADJBKDJNPL_pb2.OADJBKDJNPL, _Mapping]] = ..., CEMLGAAHAOM: _Optional[_Union[_OADJBKDJNPL_pb2.OADJBKDJNPL, _Mapping]] = ..., JGCKBJJGIAF: _Optional[_Mapping[int, int]] = ..., FHKNGCBGDJL: _Optional[_Iterable[_Union[_MJPKECMOIGA_pb2.MJPKECMOIGA, _Mapping]]] = ..., CJIHNOCINNM: _Optional[_Union[_FGGKIFNGDON_pb2.FGGKIFNGDON, _Mapping]] = ..., LOKPPLOEOFM: _Optional[_Mapping[int, int]] = ..., GMGICOPOPFK: _Optional[int] = ..., EJNINFFFKJP: _Optional[int] = ..., ALOOBPBNDDH: _Optional[int] = ..., OLLLEIKDNAN: _Optional[int] = ..., BLMGFJBAFKB: _Optional[int] = ..., MJMLCOHBLPL: _Optional[int] = ..., FDDEHDHBABM: bool = ..., KCJGPLKNPCL: bool = ..., MGCBKEMOADN: _Optional[int] = ..., JLFGOPMDPDK: _Optional[int] = ..., PEFKMBHJCDL: _Optional[int] = ...) -> None: ...
