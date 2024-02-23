# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import math_pb2 as math__pb2


class CalcStub(object):
    """services (RPC functions)

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Mult = channel.unary_unary(
                '/Calc/Mult',
                request_serializer=math__pb2.MultReq.SerializeToString,
                response_deserializer=math__pb2.MultResp.FromString,
                )
        self.MultMany = channel.unary_unary(
                '/Calc/MultMany',
                request_serializer=math__pb2.MultManyReq.SerializeToString,
                response_deserializer=math__pb2.MultResp.FromString,
                )


class CalcServicer(object):
    """services (RPC functions)

    """

    def Mult(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MultMany(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CalcServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Mult': grpc.unary_unary_rpc_method_handler(
                    servicer.Mult,
                    request_deserializer=math__pb2.MultReq.FromString,
                    response_serializer=math__pb2.MultResp.SerializeToString,
            ),
            'MultMany': grpc.unary_unary_rpc_method_handler(
                    servicer.MultMany,
                    request_deserializer=math__pb2.MultManyReq.FromString,
                    response_serializer=math__pb2.MultResp.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Calc', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Calc(object):
    """services (RPC functions)

    """

    @staticmethod
    def Mult(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Calc/Mult',
            math__pb2.MultReq.SerializeToString,
            math__pb2.MultResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MultMany(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Calc/MultMany',
            math__pb2.MultManyReq.SerializeToString,
            math__pb2.MultResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
