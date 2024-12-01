from genshin.packet.proto import DDAAKFEFAIB_pb2 as _DDAAKFEFAIB_pb2
from genshin.packet.proto import KHCOEJHBNLL_pb2 as _KHCOEJHBNLL_pb2
from genshin.packet.proto import CMMDIEGNGML_pb2 as _CMMDIEGNGML_pb2
from genshin.packet.proto import MIJLIJEKDKH_pb2 as _MIJLIJEKDKH_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JEJPLCNAFBC(_message.Message):
    __slots__ = ("MMOIDIFGGLP", "DNCPECMNEKK", "BAGJBBKNADL", "KLIMJFEPDJH", "BEOFNMDOJBP")
    MMOIDIFGGLP_FIELD_NUMBER: _ClassVar[int]
    DNCPECMNEKK_FIELD_NUMBER: _ClassVar[int]
    BAGJBBKNADL_FIELD_NUMBER: _ClassVar[int]
    KLIMJFEPDJH_FIELD_NUMBER: _ClassVar[int]
    BEOFNMDOJBP_FIELD_NUMBER: _ClassVar[int]
    MMOIDIFGGLP: _containers.RepeatedCompositeFieldContainer[_DDAAKFEFAIB_pb2.DDAAKFEFAIB]
    DNCPECMNEKK: _containers.RepeatedCompositeFieldContainer[_KHCOEJHBNLL_pb2.KHCOEJHBNLL]
    BAGJBBKNADL: _containers.RepeatedCompositeFieldContainer[_CMMDIEGNGML_pb2.CMMDIEGNGML]
    KLIMJFEPDJH: _containers.RepeatedCompositeFieldContainer[_MIJLIJEKDKH_pb2.MIJLIJEKDKH]
    BEOFNMDOJBP: int
    def __init__(self, MMOIDIFGGLP: _Optional[_Iterable[_Union[_DDAAKFEFAIB_pb2.DDAAKFEFAIB, _Mapping]]] = ..., DNCPECMNEKK: _Optional[_Iterable[_Union[_KHCOEJHBNLL_pb2.KHCOEJHBNLL, _Mapping]]] = ..., BAGJBBKNADL: _Optional[_Iterable[_Union[_CMMDIEGNGML_pb2.CMMDIEGNGML, _Mapping]]] = ..., KLIMJFEPDJH: _Optional[_Iterable[_Union[_MIJLIJEKDKH_pb2.MIJLIJEKDKH, _Mapping]]] = ..., BEOFNMDOJBP: _Optional[int] = ...) -> None: ...
