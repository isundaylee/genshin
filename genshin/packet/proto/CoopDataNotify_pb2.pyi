from genshin.packet.proto import CoopChapter_pb2 as _CoopChapter_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CoopDataNotify(_message.Message):
    __slots__ = ("is_have_progress", "chapter_list", "cur_coop_point", "viewed_chapter_list")
    IS_HAVE_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    CHAPTER_LIST_FIELD_NUMBER: _ClassVar[int]
    CUR_COOP_POINT_FIELD_NUMBER: _ClassVar[int]
    VIEWED_CHAPTER_LIST_FIELD_NUMBER: _ClassVar[int]
    is_have_progress: bool
    chapter_list: _containers.RepeatedCompositeFieldContainer[_CoopChapter_pb2.CoopChapter]
    cur_coop_point: int
    viewed_chapter_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, is_have_progress: bool = ..., chapter_list: _Optional[_Iterable[_Union[_CoopChapter_pb2.CoopChapter, _Mapping]]] = ..., cur_coop_point: _Optional[int] = ..., viewed_chapter_list: _Optional[_Iterable[int]] = ...) -> None: ...
