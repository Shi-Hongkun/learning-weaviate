from app.utils.config import env
from app.utils.weaviate_client import get_weaviate_client_custom


def main():
    print(env)

    with get_weaviate_client_custom(env=env) as client:

        print(client.collections)


if __name__ == "__main__":
    main()
