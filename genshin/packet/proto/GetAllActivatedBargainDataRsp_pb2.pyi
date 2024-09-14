from genshin.packet.proto import BargainSnapshot_pb2 as _BargainSnapshot_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetAllActivatedBargainDataRsp(_message.Message):
    __slots__ = ("snapshot_list", "retcode")
    SNAPSHOT_LIST_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    snapshot_list: _containers.RepeatedCompositeFieldContainer[_BargainSnapshot_pb2.BargainSnapshot]
    retcode: int
    def __init__(self, snapshot_list: _Optional[_Iterable[_Union[_BargainSnapshot_pb2.BargainSnapshot, _Mapping]]] = ..., retcode: _Optional[int] = ...) -> None: ...
