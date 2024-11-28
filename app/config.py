import os

project_root = os.path.dirname(os.path.abspath(__file__))


class Configuration:
    """Contains the configuration information for the app."""

    # classification
    image_folder_path = os.path.join(project_root, "static/imagenet_subset")
    models = (
        "resnet18",
        "alexnet",
        "vgg16",
        "inception_v3",
    )
    # web server
    SECRET_KEY = os.environ.get("SECRET_KEY") or "9cj328s61hsd8"
    # queue
    REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
    REDIS_PORT = os.environ.get("REDIS_PORT", "6379")

    QUEUE = "classification"
