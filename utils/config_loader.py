import yaml


def load_config(env=None):
    with open("config/config.yaml", "r") as f:
        config = yaml.safe_load(f)

    env = env or config["default_env"]  # ✅ fallback to default
    return config["environments"][env]
