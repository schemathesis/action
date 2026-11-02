import pathlib
from concurrent import futures

import grpc
from google.protobuf import descriptor_pb2, descriptor_pool, message_factory
from grpc_reflection.v1alpha import reflection

HERE = pathlib.Path(__file__).parent.absolute()

proto = descriptor_pb2.FileDescriptorProto(name="greeter.proto", package="example", syntax="proto3")
message = proto.message_type.add(name="HelloRequest")
message.field.add(
    name="name",
    number=1,
    type=descriptor_pb2.FieldDescriptorProto.TYPE_STRING,
    label=descriptor_pb2.FieldDescriptorProto.LABEL_OPTIONAL,
)
proto.message_type.add(name="HelloReply").field.add(
    name="message",
    number=1,
    type=descriptor_pb2.FieldDescriptorProto.TYPE_STRING,
    label=descriptor_pb2.FieldDescriptorProto.LABEL_OPTIONAL,
)
proto.service.add(name="Greeter").method.add(
    name="SayHello", input_type=".example.HelloRequest", output_type=".example.HelloReply"
)

pool = descriptor_pool.Default()
pool.Add(proto)
HelloRequest = message_factory.GetMessageClass(pool.FindMessageTypeByName("example.HelloRequest"))
HelloReply = message_factory.GetMessageClass(pool.FindMessageTypeByName("example.HelloReply"))

# For runs that load the schema from a descriptor set instead of server reflection
(HERE / "greeter.binpb").write_bytes(descriptor_pb2.FileDescriptorSet(file=[proto]).SerializeToString())


def say_hello(request, context):
    return HelloReply(message=f"Hello, {request.name}")


handler = grpc.method_handlers_generic_handler(
    "example.Greeter",
    {
        "SayHello": grpc.unary_unary_rpc_method_handler(
            say_hello,
            request_deserializer=HelloRequest.FromString,
            response_serializer=HelloReply.SerializeToString,
        )
    },
)

server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
server.add_generic_rpc_handlers((handler,))
reflection.enable_server_reflection(("example.Greeter", reflection.SERVICE_NAME), server)
server.add_insecure_port("127.0.0.1:50051")
server.start()
server.wait_for_termination()
