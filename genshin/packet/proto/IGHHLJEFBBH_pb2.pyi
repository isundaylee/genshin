from genshin.packet.proto import ELHHGIEOICP_pb2 as _ELHHGIEOICP_pb2
from genshin.packet.proto import HFHJKHOPLMN_pb2 as _HFHJKHOPLMN_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IGHHLJEFBBH(_message.Message):
    __slots__ = ("FAGJDJIGLON", "MEIKGBOLDGH", "CLJIKPEPLEC", "EAEKNFBGKPA", "KKPPJFKDDEP", "EDOJGAFAKDA", "JLAIAAEKGGM", "JABGACILLEC", "JIMELGDJMLF")
    FAGJDJIGLON_FIELD_NUMBER: _ClassVar[int]
    MEIKGBOLDGH_FIELD_NUMBER: _ClassVar[int]
    CLJIKPEPLEC_FIELD_NUMBER: _ClassVar[int]
    EAEKNFBGKPA_FIELD_NUMBER: _ClassVar[int]
    KKPPJFKDDEP_FIELD_NUMBER: _ClassVar[int]
    EDOJGAFAKDA_FIELD_NUMBER: _ClassVar[int]
    JLAIAAEKGGM_FIELD_NUMBER: _ClassVar[int]
    JABGACILLEC_FIELD_NUMBER: _ClassVar[int]
    JIMELGDJMLF_FIELD_NUMBER: _ClassVar[int]
    FAGJDJIGLON: _containers.RepeatedCompositeFieldContainer[_ELHHGIEOICP_pb2.ELHHGIEOICP]
    MEIKGBOLDGH: _containers.RepeatedCompositeFieldContainer[_HFHJKHOPLMN_pb2.HFHJKHOPLMN]
    CLJIKPEPLEC: _containers.RepeatedScalarFieldContainer[int]
    EAEKNFBGKPA: int
    KKPPJFKDDEP: int
    EDOJGAFAKDA: bool
    JLAIAAEKGGM: bool
    JABGACILLEC: int
    JIMELGDJMLF: int
    def __init__(self, FAGJDJIGLON: _Optional[_Iterable[_Union[_ELHHGIEOICP_pb2.ELHHGIEOICP, _Mapping]]] = ..., MEIKGBOLDGH: _Optional[_Iterable[_Union[_HFHJKHOPLMN_pb2.HFHJKHOPLMN, _Mapping]]] = ..., CLJIKPEPLEC: _Optional[_Iterable[int]] = ..., EAEKNFBGKPA: _Optional[int] = ..., KKPPJFKDDEP: _Optional[int] = ..., EDOJGAFAKDA: bool = ..., JLAIAAEKGGM: bool = ..., JABGACILLEC: _Optional[int] = ..., JIMELGDJMLF: _Optional[int] = ...) -> None: ...
