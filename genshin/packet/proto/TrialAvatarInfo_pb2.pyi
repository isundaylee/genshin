from genshin.packet.proto import BLIFJLGHEEM_pb2 as _BLIFJLGHEEM_pb2
from genshin.packet.proto import Item_pb2 as _Item_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TrialAvatarInfo(_message.Message):
    __slots__ = ("LMAIEOEHELF", "ENFBAMCLFHC", "JFFDOKFMLKJ")
    LMAIEOEHELF_FIELD_NUMBER: _ClassVar[int]
    ENFBAMCLFHC_FIELD_NUMBER: _ClassVar[int]
    JFFDOKFMLKJ_FIELD_NUMBER: _ClassVar[int]
    LMAIEOEHELF: _BLIFJLGHEEM_pb2.BLIFJLGHEEM
    ENFBAMCLFHC: _containers.RepeatedCompositeFieldContainer[_Item_pb2.Item]
    JFFDOKFMLKJ: int
    def __init__(self, LMAIEOEHELF: _Optional[_Union[_BLIFJLGHEEM_pb2.BLIFJLGHEEM, _Mapping]] = ..., ENFBAMCLFHC: _Optional[_Iterable[_Union[_Item_pb2.Item, _Mapping]]] = ..., JFFDOKFMLKJ: _Optional[int] = ...) -> None: ...
