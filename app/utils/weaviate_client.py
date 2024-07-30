import weaviate
from weaviate.client import WeaviateClient

from app.utils.config import EnvSettings


def get_weaviate_client_custom(env: EnvSettings) -> WeaviateClient:
    client = weaviate.connect_to_custom(
        http_host=env.weaviate_http_host,
        http_port=env.weaviate_http_port,
        grpc_host=env.weaviate_grpc_host,
        grpc_port=env.weaviate_grpc_port,
        http_secure=env.weaviate_secure,
        grpc_secure=env.weaviate_secure,
        headers=(
            None
            if env.weaviate_token is None
            else {"Authorization": f"Bearer {env.weaviate_token}"}
        ),
    )

    assert client.is_live() == True
    assert client.is_ready() == True

    return client


def get_weaviate_client_local(env: EnvSettings) -> WeaviateClient:
    client = weaviate.connect_to_local(
        host=env.weaviate_http_host,
        port=env.weaviate_http_port,
        grpc_port=env.weaviate_grpc_port,
        auth_credentials=weaviate.classes.init.Auth.api_key(env.weaviate_token),
    )

    assert client.is_live() == True
    assert client.is_ready() == True

    return client
