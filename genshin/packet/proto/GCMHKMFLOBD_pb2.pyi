from genshin.packet.proto import LKIAMJCJLAK_pb2 as _LKIAMJCJLAK_pb2
from genshin.packet.proto import DGLNFLCMPKN_pb2 as _DGLNFLCMPKN_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GCMHKMFLOBD(_message.Message):
    __slots__ = ("BIGKKEOICGL", "EEOEDHCIEHA")
    BIGKKEOICGL_FIELD_NUMBER: _ClassVar[int]
    EEOEDHCIEHA_FIELD_NUMBER: _ClassVar[int]
    BIGKKEOICGL: _containers.RepeatedCompositeFieldContainer[_LKIAMJCJLAK_pb2.LKIAMJCJLAK]
    EEOEDHCIEHA: _containers.RepeatedCompositeFieldContainer[_DGLNFLCMPKN_pb2.DGLNFLCMPKN]
    def __init__(self, BIGKKEOICGL: _Optional[_Iterable[_Union[_LKIAMJCJLAK_pb2.LKIAMJCJLAK, _Mapping]]] = ..., EEOEDHCIEHA: _Optional[_Iterable[_Union[_DGLNFLCMPKN_pb2.DGLNFLCMPKN, _Mapping]]] = ...) -> None: ...
