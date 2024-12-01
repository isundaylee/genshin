from genshin.packet.proto import OAAOCKLKAGG_pb2 as _OAAOCKLKAGG_pb2
from genshin.packet.proto import KHDNOCHBACF_pb2 as _KHDNOCHBACF_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PNBPKFNHMHM(_message.Message):
    __slots__ = ("OCBMAKJJCLH", "KFMLFNFGHPH")
    OCBMAKJJCLH_FIELD_NUMBER: _ClassVar[int]
    KFMLFNFGHPH_FIELD_NUMBER: _ClassVar[int]
    OCBMAKJJCLH: _containers.RepeatedCompositeFieldContainer[_OAAOCKLKAGG_pb2.OAAOCKLKAGG]
    KFMLFNFGHPH: _containers.RepeatedCompositeFieldContainer[_KHDNOCHBACF_pb2.KHDNOCHBACF]
    def __init__(self, OCBMAKJJCLH: _Optional[_Iterable[_Union[_OAAOCKLKAGG_pb2.OAAOCKLKAGG, _Mapping]]] = ..., KFMLFNFGHPH: _Optional[_Iterable[_Union[_KHDNOCHBACF_pb2.KHDNOCHBACF, _Mapping]]] = ...) -> None: ...
