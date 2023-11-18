import yaml


class MeanOneLogNormal:
    def __init__(self, sigma=None):
        self.sigma = sigma


class LogNormal:
    def __init__(self, mu=None, sigma=None):
        self.mu = mu
        self.sigma = sigma


def mean_one_log_normal_constructor(loader, node):
    value = loader.construct_mapping(node)
    return MeanOneLogNormal(sigma=value["std"])


def log_normal_constructor(loader, node):
    value = loader.construct_mapping(node)
    return LogNormal(mu=value["mean"], sigma=value["std"])


# Add constructors to the YAML loader
yaml.SafeLoader.add_constructor("!MeanOneLogNormal", mean_one_log_normal_constructor)
yaml.SafeLoader.add_constructor("!LogNormal", log_normal_constructor)
