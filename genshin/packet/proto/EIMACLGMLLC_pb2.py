# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/EIMACLGMLLC.proto
# Protobuf Python Version: 5.27.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    3,
    '',
    'genshin/packet/proto/EIMACLGMLLC.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import AHPBNFDOIPM_pb2 as genshin_dot_packet_dot_proto_dot_AHPBNFDOIPM__pb2
from genshin.packet.proto import JNOLLBCHCNH_pb2 as genshin_dot_packet_dot_proto_dot_JNOLLBCHCNH__pb2
from genshin.packet.proto import COPFHIOLNHG_pb2 as genshin_dot_packet_dot_proto_dot_COPFHIOLNHG__pb2
from genshin.packet.proto import PDDFKAKPAPF_pb2 as genshin_dot_packet_dot_proto_dot_PDDFKAKPAPF__pb2
from genshin.packet.proto import BDIMCFFEKON_pb2 as genshin_dot_packet_dot_proto_dot_BDIMCFFEKON__pb2
from genshin.packet.proto import DKIBLFIGLAP_pb2 as genshin_dot_packet_dot_proto_dot_DKIBLFIGLAP__pb2
from genshin.packet.proto import LMJBPCIGOBK_pb2 as genshin_dot_packet_dot_proto_dot_LMJBPCIGOBK__pb2
from genshin.packet.proto import EJMPGPPFPJG_pb2 as genshin_dot_packet_dot_proto_dot_EJMPGPPFPJG__pb2
from genshin.packet.proto import OLOBKCFCJEE_pb2 as genshin_dot_packet_dot_proto_dot_OLOBKCFCJEE__pb2
from genshin.packet.proto import LCFIPCLANEK_pb2 as genshin_dot_packet_dot_proto_dot_LCFIPCLANEK__pb2
from genshin.packet.proto import IKNFOPHBEDP_pb2 as genshin_dot_packet_dot_proto_dot_IKNFOPHBEDP__pb2
from genshin.packet.proto import DDAJIEEALEI_pb2 as genshin_dot_packet_dot_proto_dot_DDAJIEEALEI__pb2
from genshin.packet.proto import MAGGMEBGLAL_pb2 as genshin_dot_packet_dot_proto_dot_MAGGMEBGLAL__pb2
from genshin.packet.proto import HENGHIEEKGJ_pb2 as genshin_dot_packet_dot_proto_dot_HENGHIEEKGJ__pb2
from genshin.packet.proto import GHFMHHGBENE_pb2 as genshin_dot_packet_dot_proto_dot_GHFMHHGBENE__pb2
from genshin.packet.proto import KDOOEOMBEOC_pb2 as genshin_dot_packet_dot_proto_dot_KDOOEOMBEOC__pb2
from genshin.packet.proto import KJGDEOCDPEM_pb2 as genshin_dot_packet_dot_proto_dot_KJGDEOCDPEM__pb2
from genshin.packet.proto import GIFDGFMGKOL_pb2 as genshin_dot_packet_dot_proto_dot_GIFDGFMGKOL__pb2
from genshin.packet.proto import FELOLBOAKFD_pb2 as genshin_dot_packet_dot_proto_dot_FELOLBOAKFD__pb2
from genshin.packet.proto import MOOKABDAJLO_pb2 as genshin_dot_packet_dot_proto_dot_MOOKABDAJLO__pb2
from genshin.packet.proto import CDJBCFJMBAK_pb2 as genshin_dot_packet_dot_proto_dot_CDJBCFJMBAK__pb2
from genshin.packet.proto import DPPLPCHGCLJ_pb2 as genshin_dot_packet_dot_proto_dot_DPPLPCHGCLJ__pb2
from genshin.packet.proto import HHLHLMEKFND_pb2 as genshin_dot_packet_dot_proto_dot_HHLHLMEKFND__pb2
from genshin.packet.proto import LDFJJJDEFOA_pb2 as genshin_dot_packet_dot_proto_dot_LDFJJJDEFOA__pb2
from genshin.packet.proto import FCHLLHGCMDC_pb2 as genshin_dot_packet_dot_proto_dot_FCHLLHGCMDC__pb2
from genshin.packet.proto import FEJFGONNBFL_pb2 as genshin_dot_packet_dot_proto_dot_FEJFGONNBFL__pb2
from genshin.packet.proto import LACKBPABKHB_pb2 as genshin_dot_packet_dot_proto_dot_LACKBPABKHB__pb2
from genshin.packet.proto import IACHJPIMDFA_pb2 as genshin_dot_packet_dot_proto_dot_IACHJPIMDFA__pb2
from genshin.packet.proto import HFFFCNEFIKM_pb2 as genshin_dot_packet_dot_proto_dot_HFFFCNEFIKM__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&genshin/packet/proto/EIMACLGMLLC.proto\x1a&genshin/packet/proto/AHPBNFDOIPM.proto\x1a&genshin/packet/proto/JNOLLBCHCNH.proto\x1a&genshin/packet/proto/COPFHIOLNHG.proto\x1a&genshin/packet/proto/PDDFKAKPAPF.proto\x1a&genshin/packet/proto/BDIMCFFEKON.proto\x1a&genshin/packet/proto/DKIBLFIGLAP.proto\x1a&genshin/packet/proto/LMJBPCIGOBK.proto\x1a&genshin/packet/proto/EJMPGPPFPJG.proto\x1a&genshin/packet/proto/OLOBKCFCJEE.proto\x1a&genshin/packet/proto/LCFIPCLANEK.proto\x1a&genshin/packet/proto/IKNFOPHBEDP.proto\x1a&genshin/packet/proto/DDAJIEEALEI.proto\x1a&genshin/packet/proto/MAGGMEBGLAL.proto\x1a&genshin/packet/proto/HENGHIEEKGJ.proto\x1a&genshin/packet/proto/GHFMHHGBENE.proto\x1a&genshin/packet/proto/KDOOEOMBEOC.proto\x1a&genshin/packet/proto/KJGDEOCDPEM.proto\x1a&genshin/packet/proto/GIFDGFMGKOL.proto\x1a&genshin/packet/proto/FELOLBOAKFD.proto\x1a&genshin/packet/proto/MOOKABDAJLO.proto\x1a&genshin/packet/proto/CDJBCFJMBAK.proto\x1a&genshin/packet/proto/DPPLPCHGCLJ.proto\x1a&genshin/packet/proto/HHLHLMEKFND.proto\x1a&genshin/packet/proto/LDFJJJDEFOA.proto\x1a&genshin/packet/proto/FCHLLHGCMDC.proto\x1a&genshin/packet/proto/FEJFGONNBFL.proto\x1a&genshin/packet/proto/LACKBPABKHB.proto\x1a&genshin/packet/proto/IACHJPIMDFA.proto\x1a&genshin/packet/proto/HFFFCNEFIKM.proto\"\xbc\x0b\n\x0b\x45IMACLGMLLC\x12!\n\x0bPFJGLPFAAGA\x18\x17 \x01(\x0b\x32\x0c.AHPBNFDOIPM\x12\x13\n\x0bLJCDEEFBFML\x18\x1d \x03(\r\x12!\n\x0b\x45JEHOGBGBIJ\x18\x66 \x01(\x0b\x32\x0c.JNOLLBCHCNH\x12\x13\n\x0bHLADAENGOEG\x18\x18 \x03(\r\x12!\n\x0b\x46LJFNPMNGFI\x18\x64 \x01(\x0b\x32\x0c.COPFHIOLNHG\x12!\n\x0bNAJIKMLHPFB\x18\x65 \x01(\x0b\x32\x0c.PDDFKAKPAPF\x12!\n\x0bKLPMJCFGNPI\x18g \x01(\x0b\x32\x0c.BDIMCFFEKON\x12!\n\x0bJIOIGFOFFFF\x18\x1b \x01(\x0b\x32\x0c.DKIBLFIGLAP\x12\x13\n\x0b\x41LNAIFDJFGA\x18\x16 \x01(\r\x12\x13\n\x0b\x41IMBJLBHOCN\x18\n \x01(\x08\x12\x13\n\x0b\x43\x42MJDGBPBAI\x18\x08 \x01(\x08\x12\x13\n\x0bKBNHDNPJJBH\x18\t \x01(\r\x12\x13\n\x0b\x46NKMGAGEDAH\x18\x19 \x01(\r\x12\x13\n\x0bODFMAHNOBHH\x18\x1a \x01(\r\x12\x13\n\x0bHLKDDNGCKJN\x18\x03 \x01(\r\x12\x13\n\x0bOCKIBANLDMK\x18\x01 \x01(\r\x12\x13\n\x0bJBMEBKOANNI\x18\x04 \x01(\r\x12\x13\n\x0bGHGOAAGEINH\x18\x1c \x01(\r\x12\x13\n\x0bOHCHPMIFDHG\x18\x15 \x01(\r\x12!\n\x0b\x42NGPKPJNMCG\x18\x05 \x01(\x0e\x32\x0c.LMJBPCIGOBK\x12\x13\n\x0bLMFJIFDKIIO\x18\x07 \x01(\r\x12\x13\n\x0bJABDDPGGIKF\x18\x0b \x01(\r\x12\x13\n\x0b\x45HAEACFBOOL\x18\x02 \x01(\r\x12 \n\nboss_chest\x18\x14 \x01(\x0b\x32\x0c.EJMPGPPFPJG\x12!\n\x0bscreen_info\x18\x30 \x01(\x0b\x32\x0c.OLOBKCFCJEE\x12#\n\rblossom_chest\x18) \x01(\x0b\x32\x0c.LCFIPCLANEK\x12 \n\nshell_info\x18/ \x01(\x0b\x32\x0c.IKNFOPHBEDP\x12\x1d\n\x07weather\x18\x11 \x01(\x0b\x32\x0c.DDAJIEEALEI\x12$\n\x0e\x61\x62ility_gadget\x18\x12 \x01(\x0b\x32\x0c.MAGGMEBGLAL\x12#\n\rclient_gadget\x18\x0f \x01(\x0b\x32\x0c.HENGHIEEKGJ\x12\x30\n\x1a\x63oin_collect_operator_info\x18@ \x01(\x0b\x32\x0c.GHFMHHGBENE\x12#\n\rgather_gadget\x18\r \x01(\x0b\x32\x0c.KDOOEOMBEOC\x12+\n\x15roguelike_gadget_info\x18= \x01(\x0b\x32\x0c.KJGDEOCDPEM\x12#\n\roffering_info\x18, \x01(\x0b\x32\x0c.GIFDGFMGKOL\x12,\n\x16night_crow_gadget_info\x18> \x01(\x0b\x32\x0c.FELOLBOAKFD\x12#\n\rstatue_gadget\x18\x13 \x01(\x0b\x32\x0c.MOOKABDAJLO\x12\x31\n\x1b\x64\x65shret_obelisk_gadget_info\x18? \x01(\x0b\x32\x0c.CDJBCFJMBAK\x12%\n\x0f\x66oundation_info\x18- \x01(\x0b\x32\x0c.DPPLPCHGCLJ\x12\x1d\n\x07worktop\x18\x0e \x01(\x0b\x32\x0c.HHLHLMEKFND\x12$\n\x0egeneral_reward\x18+ \x01(\x0b\x32\x0c.LDFJJJDEFOA\x12\"\n\x0cvehicle_info\x18. \x01(\x0b\x32\x0c.FCHLLHGCMDC\x12$\n\x0e\x66ish_pool_info\x18; \x01(\x0b\x32\x0c.FEJFGONNBFL\x12$\n\x0emp_play_reward\x18* \x01(\x0b\x32\x0c.LACKBPABKHB\x12#\n\rtrifle_gadget\x18\x43 \x01(\x0b\x32\x0c.IACHJPIMDFA\x12-\n\x17\x63ustom_gadget_tree_info\x18< \x01(\x0b\x32\x0c.HFFFCNEFIKM\x12\x13\n\x0b\x42MMBMCLKGMO\x18\x06 \x01(\rb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.EIMACLGMLLC_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EIMACLGMLLC']._serialized_start=1203
  _globals['_EIMACLGMLLC']._serialized_end=2671
# @@protoc_insertion_point(module_scope)