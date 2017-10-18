#!/usr/bin/env python
import distutils
from distutils.core import setup
from distutils.extension import Extension

import sys
import os
import subprocess

from distutils.command.build_py import build_py as _build_py


def exec_generate_proto(source):
    protoc_command = ["python3", "-m", "grpc_tools.protoc", "-I.", "--python_out=..", source]
    if subprocess.call(protoc_command) != 0:
        sys.exit(-1)
    sys.stdout.write("Generate {}_pb2.py ==> successfull\n".format(source.split('.')[0]))

    protoc_grpc_command = ["python3", "-m", "grpc_tools.protoc", "-I.", "--python_out=..","--grpc_python_out=..", source]
    if subprocess.call(protoc_grpc_command) != 0:
        sys.exit(-1)
    sys.stdout.write("Generate {}_grcp_pb2.py ==> successfull\n".format(source.split('.')[0]))


class GeneratePb(_build_py):
    def run(self):
        os.chdir("schema/")
        exec_generate_proto('block.proto')
        exec_generate_proto('commands.proto')
        exec_generate_proto('endpoint.proto')
        exec_generate_proto('primitive.proto')
        exec_generate_proto('queries.proto')
        exec_generate_proto('responses.proto')


if __name__ == '__main__':
    setup(
          name='iroha-ya-cli',
          version='0.7',
          description='Cli for hyperledger/iroha',
          author='Sonoko Mizuki',
          author_email='mizuki.sonoko@gmail.com',
          packages=['src'],
          include_package_data=True,
          install_requires=[
                'grpcio',
                'grpcio-tools',
                'protobuf',

                'sha3',
                'ed25519'
          ],
          cmdclass={
            'build_py': GeneratePb,
          },
          entry_points={
          'console_scripts':
            ['iroha-ya-cli=src.main:main']
          },
    )