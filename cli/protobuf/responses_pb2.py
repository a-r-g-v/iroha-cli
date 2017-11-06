# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: responses.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import block_pb2 as block__pb2
import primitive_pb2 as primitive__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='responses.proto',
  package='iroha.protocol',
  syntax='proto3',
  serialized_pb=_b('\n\x0fresponses.proto\x12\x0eiroha.protocol\x1a\x0b\x62lock.proto\x1a\x0fprimitive.proto\"?\n\x05\x41sset\x12\x10\n\x08\x61sset_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\x12\x11\n\tprecision\x18\x03 \x01(\r\"t\n\x07\x41\x63\x63ount\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12\x13\n\x0b\x64omain_name\x18\x02 \x01(\t\x12\x30\n\x0bpermissions\x18\x03 \x01(\x0b\x32\x1b.iroha.protocol.Permissions\x12\x0e\n\x06quorum\x18\x04 \x01(\r\"]\n\x0c\x41\x63\x63ountAsset\x12\x10\n\x08\x61sset_id\x18\x01 \x01(\t\x12\x12\n\naccount_id\x18\x02 \x01(\t\x12\'\n\x07\x62\x61lance\x18\x03 \x01(\x0b\x32\x16.iroha.protocol.Amount\"K\n\x14\x41\x63\x63ountAssetResponse\x12\x33\n\raccount_asset\x18\x01 \x01(\x0b\x32\x1c.iroha.protocol.AccountAsset\";\n\x0f\x41\x63\x63ountResponse\x12(\n\x07\x61\x63\x63ount\x18\x01 \x01(\x0b\x32\x17.iroha.protocol.Account\"5\n\rAssetResponse\x12$\n\x05\x61sset\x18\x01 \x01(\x0b\x32\x15.iroha.protocol.Asset\"\x1e\n\rRolesResponse\x12\r\n\x05roles\x18\x01 \x03(\t\".\n\x17RolePermissionsResponse\x12\x13\n\x0bpermissions\x18\x01 \x03(\t\"\xf9\x01\n\rErrorResponse\x12\x34\n\x06reason\x18\x01 \x01(\x0e\x32$.iroha.protocol.ErrorResponse.Reason\"\xb1\x01\n\x06Reason\x12\x15\n\x11STATELESS_INVALID\x10\x00\x12\x14\n\x10STATEFUL_INVALID\x10\x01\x12\x0e\n\nNO_ACCOUNT\x10\x02\x12\x15\n\x11NO_ACCOUNT_ASSETS\x10\x03\x12\x12\n\x0eNO_SIGNATORIES\x10\x04\x12\x11\n\rNOT_SUPPORTED\x10\x05\x12\x10\n\x0cWRONG_FORMAT\x10\x06\x12\x0c\n\x08NO_ASSET\x10\x07\x12\x0c\n\x08NO_ROLES\x10\x08\"#\n\x13SignatoriesResponse\x12\x0c\n\x04keys\x18\x01 \x03(\x0c\"I\n\x14TransactionsResponse\x12\x31\n\x0ctransactions\x18\x01 \x03(\x0b\x32\x1b.iroha.protocol.Transaction\"\xa6\x04\n\rQueryResponse\x12G\n\x17\x61\x63\x63ount_assets_response\x18\x01 \x01(\x0b\x32$.iroha.protocol.AccountAssetResponseH\x00\x12;\n\x10\x61\x63\x63ount_response\x18\x02 \x01(\x0b\x32\x1f.iroha.protocol.AccountResponseH\x00\x12\x37\n\x0e\x65rror_response\x18\x03 \x01(\x0b\x32\x1d.iroha.protocol.ErrorResponseH\x00\x12\x43\n\x14signatories_response\x18\x04 \x01(\x0b\x32#.iroha.protocol.SignatoriesResponseH\x00\x12\x45\n\x15transactions_response\x18\x05 \x01(\x0b\x32$.iroha.protocol.TransactionsResponseH\x00\x12\x37\n\x0e\x61sset_response\x18\x06 \x01(\x0b\x32\x1d.iroha.protocol.AssetResponseH\x00\x12\x37\n\x0eroles_response\x18\x07 \x01(\x0b\x32\x1d.iroha.protocol.RolesResponseH\x00\x12L\n\x19role_permissions_response\x18\x08 \x01(\x0b\x32\'.iroha.protocol.RolePermissionsResponseH\x00\x42\n\n\x08responseb\x06proto3')
  ,
  dependencies=[block__pb2.DESCRIPTOR,primitive__pb2.DESCRIPTOR,])



_ERRORRESPONSE_REASON = _descriptor.EnumDescriptor(
  name='Reason',
  full_name='iroha.protocol.ErrorResponse.Reason',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATELESS_INVALID', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATEFUL_INVALID', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_ACCOUNT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_ACCOUNT_ASSETS', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_SIGNATORIES', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_SUPPORTED', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WRONG_FORMAT', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_ASSET', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_ROLES', index=8, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=689,
  serialized_end=866,
)
_sym_db.RegisterEnumDescriptor(_ERRORRESPONSE_REASON)


_ASSET = _descriptor.Descriptor(
  name='Asset',
  full_name='iroha.protocol.Asset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='asset_id', full_name='iroha.protocol.Asset.asset_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='iroha.protocol.Asset.domain_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='precision', full_name='iroha.protocol.Asset.precision', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=128,
)


_ACCOUNT = _descriptor.Descriptor(
  name='Account',
  full_name='iroha.protocol.Account',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account_id', full_name='iroha.protocol.Account.account_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='domain_name', full_name='iroha.protocol.Account.domain_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='permissions', full_name='iroha.protocol.Account.permissions', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quorum', full_name='iroha.protocol.Account.quorum', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=246,
)


_ACCOUNTASSET = _descriptor.Descriptor(
  name='AccountAsset',
  full_name='iroha.protocol.AccountAsset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='asset_id', full_name='iroha.protocol.AccountAsset.asset_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='account_id', full_name='iroha.protocol.AccountAsset.account_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='balance', full_name='iroha.protocol.AccountAsset.balance', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=248,
  serialized_end=341,
)


_ACCOUNTASSETRESPONSE = _descriptor.Descriptor(
  name='AccountAssetResponse',
  full_name='iroha.protocol.AccountAssetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account_asset', full_name='iroha.protocol.AccountAssetResponse.account_asset', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=343,
  serialized_end=418,
)


_ACCOUNTRESPONSE = _descriptor.Descriptor(
  name='AccountResponse',
  full_name='iroha.protocol.AccountResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account', full_name='iroha.protocol.AccountResponse.account', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=420,
  serialized_end=479,
)


_ASSETRESPONSE = _descriptor.Descriptor(
  name='AssetResponse',
  full_name='iroha.protocol.AssetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='asset', full_name='iroha.protocol.AssetResponse.asset', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=481,
  serialized_end=534,
)


_ROLESRESPONSE = _descriptor.Descriptor(
  name='RolesResponse',
  full_name='iroha.protocol.RolesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='roles', full_name='iroha.protocol.RolesResponse.roles', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=536,
  serialized_end=566,
)


_ROLEPERMISSIONSRESPONSE = _descriptor.Descriptor(
  name='RolePermissionsResponse',
  full_name='iroha.protocol.RolePermissionsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='permissions', full_name='iroha.protocol.RolePermissionsResponse.permissions', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=568,
  serialized_end=614,
)


_ERRORRESPONSE = _descriptor.Descriptor(
  name='ErrorResponse',
  full_name='iroha.protocol.ErrorResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reason', full_name='iroha.protocol.ErrorResponse.reason', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ERRORRESPONSE_REASON,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=617,
  serialized_end=866,
)


_SIGNATORIESRESPONSE = _descriptor.Descriptor(
  name='SignatoriesResponse',
  full_name='iroha.protocol.SignatoriesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keys', full_name='iroha.protocol.SignatoriesResponse.keys', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=868,
  serialized_end=903,
)


_TRANSACTIONSRESPONSE = _descriptor.Descriptor(
  name='TransactionsResponse',
  full_name='iroha.protocol.TransactionsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transactions', full_name='iroha.protocol.TransactionsResponse.transactions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=905,
  serialized_end=978,
)


_QUERYRESPONSE = _descriptor.Descriptor(
  name='QueryResponse',
  full_name='iroha.protocol.QueryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account_assets_response', full_name='iroha.protocol.QueryResponse.account_assets_response', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='account_response', full_name='iroha.protocol.QueryResponse.account_response', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_response', full_name='iroha.protocol.QueryResponse.error_response', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signatories_response', full_name='iroha.protocol.QueryResponse.signatories_response', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transactions_response', full_name='iroha.protocol.QueryResponse.transactions_response', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='asset_response', full_name='iroha.protocol.QueryResponse.asset_response', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='roles_response', full_name='iroha.protocol.QueryResponse.roles_response', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role_permissions_response', full_name='iroha.protocol.QueryResponse.role_permissions_response', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='response', full_name='iroha.protocol.QueryResponse.response',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=981,
  serialized_end=1531,
)

_ACCOUNT.fields_by_name['permissions'].message_type = primitive__pb2._PERMISSIONS
_ACCOUNTASSET.fields_by_name['balance'].message_type = primitive__pb2._AMOUNT
_ACCOUNTASSETRESPONSE.fields_by_name['account_asset'].message_type = _ACCOUNTASSET
_ACCOUNTRESPONSE.fields_by_name['account'].message_type = _ACCOUNT
_ASSETRESPONSE.fields_by_name['asset'].message_type = _ASSET
_ERRORRESPONSE.fields_by_name['reason'].enum_type = _ERRORRESPONSE_REASON
_ERRORRESPONSE_REASON.containing_type = _ERRORRESPONSE
_TRANSACTIONSRESPONSE.fields_by_name['transactions'].message_type = block__pb2._TRANSACTION
_QUERYRESPONSE.fields_by_name['account_assets_response'].message_type = _ACCOUNTASSETRESPONSE
_QUERYRESPONSE.fields_by_name['account_response'].message_type = _ACCOUNTRESPONSE
_QUERYRESPONSE.fields_by_name['error_response'].message_type = _ERRORRESPONSE
_QUERYRESPONSE.fields_by_name['signatories_response'].message_type = _SIGNATORIESRESPONSE
_QUERYRESPONSE.fields_by_name['transactions_response'].message_type = _TRANSACTIONSRESPONSE
_QUERYRESPONSE.fields_by_name['asset_response'].message_type = _ASSETRESPONSE
_QUERYRESPONSE.fields_by_name['roles_response'].message_type = _ROLESRESPONSE
_QUERYRESPONSE.fields_by_name['role_permissions_response'].message_type = _ROLEPERMISSIONSRESPONSE
_QUERYRESPONSE.oneofs_by_name['response'].fields.append(
  _QUERYRESPONSE.fields_by_name['account_assets_response'])
_QUERYRESPONSE.fields_by_name['account_assets_response'].containing_oneof = _QUERYRESPONSE.oneofs_by_name['response']
_QUERYRESPONSE.oneofs_by_name['response'].fields.append(
  _QUERYRESPONSE.fields_by_name['account_response'])
_QUERYRESPONSE.fields_by_name['account_response'].containing_oneof = _QUERYRESPONSE.oneofs_by_name['response']
_QUERYRESPONSE.oneofs_by_name['response'].fields.append(
  _QUERYRESPONSE.fields_by_name['error_response'])
_QUERYRESPONSE.fields_by_name['error_response'].containing_oneof = _QUERYRESPONSE.oneofs_by_name['response']
_QUERYRESPONSE.oneofs_by_name['response'].fields.append(
  _QUERYRESPONSE.fields_by_name['signatories_response'])
_QUERYRESPONSE.fields_by_name['signatories_response'].containing_oneof = _QUERYRESPONSE.oneofs_by_name['response']
_QUERYRESPONSE.oneofs_by_name['response'].fields.append(
  _QUERYRESPONSE.fields_by_name['transactions_response'])
_QUERYRESPONSE.fields_by_name['transactions_response'].containing_oneof = _QUERYRESPONSE.oneofs_by_name['response']
_QUERYRESPONSE.oneofs_by_name['response'].fields.append(
  _QUERYRESPONSE.fields_by_name['asset_response'])
_QUERYRESPONSE.fields_by_name['asset_response'].containing_oneof = _QUERYRESPONSE.oneofs_by_name['response']
_QUERYRESPONSE.oneofs_by_name['response'].fields.append(
  _QUERYRESPONSE.fields_by_name['roles_response'])
_QUERYRESPONSE.fields_by_name['roles_response'].containing_oneof = _QUERYRESPONSE.oneofs_by_name['response']
_QUERYRESPONSE.oneofs_by_name['response'].fields.append(
  _QUERYRESPONSE.fields_by_name['role_permissions_response'])
_QUERYRESPONSE.fields_by_name['role_permissions_response'].containing_oneof = _QUERYRESPONSE.oneofs_by_name['response']
DESCRIPTOR.message_types_by_name['Asset'] = _ASSET
DESCRIPTOR.message_types_by_name['Account'] = _ACCOUNT
DESCRIPTOR.message_types_by_name['AccountAsset'] = _ACCOUNTASSET
DESCRIPTOR.message_types_by_name['AccountAssetResponse'] = _ACCOUNTASSETRESPONSE
DESCRIPTOR.message_types_by_name['AccountResponse'] = _ACCOUNTRESPONSE
DESCRIPTOR.message_types_by_name['AssetResponse'] = _ASSETRESPONSE
DESCRIPTOR.message_types_by_name['RolesResponse'] = _ROLESRESPONSE
DESCRIPTOR.message_types_by_name['RolePermissionsResponse'] = _ROLEPERMISSIONSRESPONSE
DESCRIPTOR.message_types_by_name['ErrorResponse'] = _ERRORRESPONSE
DESCRIPTOR.message_types_by_name['SignatoriesResponse'] = _SIGNATORIESRESPONSE
DESCRIPTOR.message_types_by_name['TransactionsResponse'] = _TRANSACTIONSRESPONSE
DESCRIPTOR.message_types_by_name['QueryResponse'] = _QUERYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Asset = _reflection.GeneratedProtocolMessageType('Asset', (_message.Message,), dict(
  DESCRIPTOR = _ASSET,
  __module__ = 'responses_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.Asset)
  ))
_sym_db.RegisterMessage(Asset)

Account = _reflection.GeneratedProtocolMessageType('Account', (_message.Message,), dict(
  DESCRIPTOR = _ACCOUNT,
  __module__ = 'responses_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.Account)
  ))
_sym_db.RegisterMessage(Account)

AccountAsset = _reflection.GeneratedProtocolMessageType('AccountAsset', (_message.Message,), dict(
  DESCRIPTOR = _ACCOUNTASSET,
  __module__ = 'responses_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.AccountAsset)
  ))
_sym_db.RegisterMessage(AccountAsset)

AccountAssetResponse = _reflection.GeneratedProtocolMessageType('AccountAssetResponse', (_message.Message,), dict(
  DESCRIPTOR = _ACCOUNTASSETRESPONSE,
  __module__ = 'responses_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.AccountAssetResponse)
  ))
_sym_db.RegisterMessage(AccountAssetResponse)

AccountResponse = _reflection.GeneratedProtocolMessageType('AccountResponse', (_message.Message,), dict(
  DESCRIPTOR = _ACCOUNTRESPONSE,
  __module__ = 'responses_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.AccountResponse)
  ))
_sym_db.RegisterMessage(AccountResponse)

AssetResponse = _reflection.GeneratedProtocolMessageType('AssetResponse', (_message.Message,), dict(
  DESCRIPTOR = _ASSETRESPONSE,
  __module__ = 'responses_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.AssetResponse)
  ))
_sym_db.RegisterMessage(AssetResponse)

RolesResponse = _reflection.GeneratedProtocolMessageType('RolesResponse', (_message.Message,), dict(
  DESCRIPTOR = _ROLESRESPONSE,
  __module__ = 'responses_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.RolesResponse)
  ))
_sym_db.RegisterMessage(RolesResponse)

RolePermissionsResponse = _reflection.GeneratedProtocolMessageType('RolePermissionsResponse', (_message.Message,), dict(
  DESCRIPTOR = _ROLEPERMISSIONSRESPONSE,
  __module__ = 'responses_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.RolePermissionsResponse)
  ))
_sym_db.RegisterMessage(RolePermissionsResponse)

ErrorResponse = _reflection.GeneratedProtocolMessageType('ErrorResponse', (_message.Message,), dict(
  DESCRIPTOR = _ERRORRESPONSE,
  __module__ = 'responses_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.ErrorResponse)
  ))
_sym_db.RegisterMessage(ErrorResponse)

SignatoriesResponse = _reflection.GeneratedProtocolMessageType('SignatoriesResponse', (_message.Message,), dict(
  DESCRIPTOR = _SIGNATORIESRESPONSE,
  __module__ = 'responses_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.SignatoriesResponse)
  ))
_sym_db.RegisterMessage(SignatoriesResponse)

TransactionsResponse = _reflection.GeneratedProtocolMessageType('TransactionsResponse', (_message.Message,), dict(
  DESCRIPTOR = _TRANSACTIONSRESPONSE,
  __module__ = 'responses_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.TransactionsResponse)
  ))
_sym_db.RegisterMessage(TransactionsResponse)

QueryResponse = _reflection.GeneratedProtocolMessageType('QueryResponse', (_message.Message,), dict(
  DESCRIPTOR = _QUERYRESPONSE,
  __module__ = 'responses_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.QueryResponse)
  ))
_sym_db.RegisterMessage(QueryResponse)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
