from genshin.packet.proto import IOAHICPMIEB_pb2 as _IOAHICPMIEB_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OILDAMFJODC(_message.Message):
    __slots__ = ("DJPDELLJHJF", "AOPGDGMGKIA", "DKEFLELLNCK", "JEPOOMPBGLN", "BFJAHDAHEML", "LEDDHCIFLBC", "BGJFEMOACPL")
    DJPDELLJHJF_FIELD_NUMBER: _ClassVar[int]
    AOPGDGMGKIA_FIELD_NUMBER: _ClassVar[int]
    DKEFLELLNCK_FIELD_NUMBER: _ClassVar[int]
    JEPOOMPBGLN_FIELD_NUMBER: _ClassVar[int]
    BFJAHDAHEML_FIELD_NUMBER: _ClassVar[int]
    LEDDHCIFLBC_FIELD_NUMBER: _ClassVar[int]
    BGJFEMOACPL_FIELD_NUMBER: _ClassVar[int]
    DJPDELLJHJF: _containers.RepeatedScalarFieldContainer[int]
    AOPGDGMGKIA: _containers.RepeatedScalarFieldContainer[int]
    DKEFLELLNCK: _containers.RepeatedScalarFieldContainer[int]
    JEPOOMPBGLN: _containers.RepeatedScalarFieldContainer[int]
    BFJAHDAHEML: _containers.RepeatedScalarFieldContainer[int]
    LEDDHCIFLBC: _containers.RepeatedCompositeFieldContainer[_IOAHICPMIEB_pb2.IOAHICPMIEB]
    BGJFEMOACPL: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, DJPDELLJHJF: _Optional[_Iterable[int]] = ..., AOPGDGMGKIA: _Optional[_Iterable[int]] = ..., DKEFLELLNCK: _Optional[_Iterable[int]] = ..., JEPOOMPBGLN: _Optional[_Iterable[int]] = ..., BFJAHDAHEML: _Optional[_Iterable[int]] = ..., LEDDHCIFLBC: _Optional[_Iterable[_Union[_IOAHICPMIEB_pb2.IOAHICPMIEB, _Mapping]]] = ..., BGJFEMOACPL: _Optional[_Iterable[int]] = ...) -> None: ...
