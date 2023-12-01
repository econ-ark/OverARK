import yaml
from yaml import Loader, Dumper


## distributions

class Bernoulli:
    def __init__(self, p=None):
        self.p = p

class MeanOneLogNormal:
    def __init__(self, sigma=None):
        self.sigma = sigma


class LogNormal:
    def __init__(self, mu=None, sigma=None):
        self.mu = mu
        self.sigma = sigma

## modeling

class Control:
    def __init__(self, inset = None, constraints = None):
        self.inset = inset
        self.constraints = constraints

def control_constructor(loader: yaml.SafeLoader, node: yaml.nodes.MappingNode) -> Control:
  return Control(**loader.construct_mapping(node))

class Link:
    def __init__(self, head = None, tail = None, twist = None, tick= None, finite = None):
        self.head = head
        self.tail = tail
        self.twist = twist
        self.tick = tick
        self.finite = finite

## strategies


class HardRule:
    def __init__(self, block = None, decision_rule = None):
        self.block = block
        self.decision_rule = decision_rule

class Bellman:
    def __init__(self, block = None, reward = None, discount = None, continuation = None):
        self.block = block
        self.reward = reward
        self.discount = discount
        self.continuation = continuation

class LifetimeReward:
    def __init__(self, block = None, reward = None, discount = None):
        self.block = block
        self.reward = reward
        self.discount = discount


## solution methods

class EGM:
    def __init__(self, grid = None, discretizations = None):
        self.grid = grid
        self.discretizations = discretizations


def get_loader():
  """Add constructors to PyYAML loader."""
  loader = yaml.SafeLoader
  yaml.SafeLoader.add_constructor("!Bellman", Bellman)
  yaml.SafeLoader.add_constructor("!Bernoulli", Bellman)
  yaml.SafeLoader.add_constructor("!Control", Control)
  yaml.SafeLoader.add_constructor("!EGM", EGM)
  yaml.SafeLoader.add_constructor("!HardRule", HardRule)
  yaml.SafeLoader.add_constructor("!LifetimeReward", LifetimeReward)
  yaml.SafeLoader.add_constructor("!Link", Link)
  yaml.SafeLoader.add_constructor("!LogNormal", LogNormal)

  return loader

try:
    config = yaml.load(open('perfect_foresight.yaml', 'r'), Loader= get_loader())

    # data is copied
    assert config['model']['blocks']['consumption'] == config['model']['strategies'][1]['block']
    # data is maintained once in memory and referenced in both places
    assert config['model']['blocks']['consumption'] is config['model']['strategies'][1]['block']

    # object created by parser
    c1 = config['model']['blocks']['consumption']['dynamics']['c']
    c2 = config['model']['strategies'][1]['block']['dynamics']['c']

    # objects are equal
    assert c1 == c2
    # objects are identical in memory; the reference is shared.
    assert c1 is c2

except yaml.YAMLError as exc:
    print("Error in configuration file:", exc)
