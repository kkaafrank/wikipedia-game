from dotenv import dotenv_values

config: dict = {
    **dotenv_values("./global_constants/shared_global_constants.txt"),
    **dotenv_values("./global_constants/local_constants.txt"),
}

for key, value in config.items():
    try:
        value_as_float: float = float(value)
        config[key] = value_as_float
    except ValueError:
        continue