from genshin.packet.proto import KDEHCGJAGFJ_pb2 as _KDEHCGJAGFJ_pb2
from genshin.packet.proto import CBIMLMHCMLN_pb2 as _CBIMLMHCMLN_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DJFJJGEDFPH(_message.Message):
    __slots__ = ("KFHPBOFMMAG", "KDAIEIPOCOD")
    KFHPBOFMMAG_FIELD_NUMBER: _ClassVar[int]
    KDAIEIPOCOD_FIELD_NUMBER: _ClassVar[int]
    KFHPBOFMMAG: _containers.RepeatedCompositeFieldContainer[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ]
    KDAIEIPOCOD: _containers.RepeatedCompositeFieldContainer[_CBIMLMHCMLN_pb2.CBIMLMHCMLN]
    def __init__(self, KFHPBOFMMAG: _Optional[_Iterable[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]]] = ..., KDAIEIPOCOD: _Optional[_Iterable[_Union[_CBIMLMHCMLN_pb2.CBIMLMHCMLN, _Mapping]]] = ...) -> None: ...
