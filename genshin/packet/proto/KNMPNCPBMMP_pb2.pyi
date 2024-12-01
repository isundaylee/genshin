from genshin.packet.proto import BHNJIKABAOK_pb2 as _BHNJIKABAOK_pb2
from genshin.packet.proto import HNNAAANKING_pb2 as _HNNAAANKING_pb2
from genshin.packet.proto import IJFNLMOGGLK_pb2 as _IJFNLMOGGLK_pb2
from genshin.packet.proto import BCBDFLGIOCC_pb2 as _BCBDFLGIOCC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KNMPNCPBMMP(_message.Message):
    __slots__ = ("NMMHPMHIAPF", "FFDIPJHIPCK", "MCIPDHGDFKO", "MHBJPOKCIBB", "NAJAGAKHGKN", "MJBNBFEDDHA")
    NMMHPMHIAPF_FIELD_NUMBER: _ClassVar[int]
    FFDIPJHIPCK_FIELD_NUMBER: _ClassVar[int]
    MCIPDHGDFKO_FIELD_NUMBER: _ClassVar[int]
    MHBJPOKCIBB_FIELD_NUMBER: _ClassVar[int]
    NAJAGAKHGKN_FIELD_NUMBER: _ClassVar[int]
    MJBNBFEDDHA_FIELD_NUMBER: _ClassVar[int]
    NMMHPMHIAPF: _containers.RepeatedCompositeFieldContainer[_BHNJIKABAOK_pb2.BHNJIKABAOK]
    FFDIPJHIPCK: _containers.RepeatedCompositeFieldContainer[_HNNAAANKING_pb2.HNNAAANKING]
    MCIPDHGDFKO: _containers.RepeatedCompositeFieldContainer[_IJFNLMOGGLK_pb2.IJFNLMOGGLK]
    MHBJPOKCIBB: _containers.RepeatedCompositeFieldContainer[_BHNJIKABAOK_pb2.BHNJIKABAOK]
    NAJAGAKHGKN: _containers.RepeatedCompositeFieldContainer[_BCBDFLGIOCC_pb2.BCBDFLGIOCC]
    MJBNBFEDDHA: bool
    def __init__(self, NMMHPMHIAPF: _Optional[_Iterable[_Union[_BHNJIKABAOK_pb2.BHNJIKABAOK, _Mapping]]] = ..., FFDIPJHIPCK: _Optional[_Iterable[_Union[_HNNAAANKING_pb2.HNNAAANKING, _Mapping]]] = ..., MCIPDHGDFKO: _Optional[_Iterable[_Union[_IJFNLMOGGLK_pb2.IJFNLMOGGLK, _Mapping]]] = ..., MHBJPOKCIBB: _Optional[_Iterable[_Union[_BHNJIKABAOK_pb2.BHNJIKABAOK, _Mapping]]] = ..., NAJAGAKHGKN: _Optional[_Iterable[_Union[_BCBDFLGIOCC_pb2.BCBDFLGIOCC, _Mapping]]] = ..., MJBNBFEDDHA: bool = ...) -> None: ...
