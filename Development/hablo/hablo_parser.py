
from inspect import signature
import numpy as np
from pprint import pprint as pp
from sympy.utilities.lambdify import lambdify
from  sympy.parsing.sympy_parser import parse_expr
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

def constructor_from_class(cls):
    def constructor(loader, node):
        value = loader.construct_mapping(node)
        return cls(**value)
    
    return constructor


class HabloExpression():

    def __init__(self, text):
        self.expr = parse_expr(text)
        self.npf = self.func()

        # first derivatives.
        self.diffs = {
            sym.__str__() : 
            self.expr.diff(sym)
            for sym
            in list(self.expr.free_symbols)
        }

    def func(self):
        return lambdify(list(self.expr.free_symbols), self.expr, "numpy")


def math_text_to_lambda(text):
    expr = parse_expr(text)
    func = lambdify(list(expr.free_symbols), expr, "numpy")
    return func


def get_loader():
  """Add constructors to PyYAML loader."""
  loader = yaml.SafeLoader
  yaml.SafeLoader.add_constructor("!Bellman", constructor_from_class(Bellman))
  yaml.SafeLoader.add_constructor("!Bernoulli", constructor_from_class(Bernoulli))
  yaml.SafeLoader.add_constructor("!Control", constructor_from_class(Control))
  yaml.SafeLoader.add_constructor("!EGM", constructor_from_class(EGM))
  yaml.SafeLoader.add_constructor("!HardRule", constructor_from_class(HardRule))
  yaml.SafeLoader.add_constructor("!LifetimeReward", constructor_from_class(LifetimeReward))
  yaml.SafeLoader.add_constructor("!Link", constructor_from_class(Link))
  yaml.SafeLoader.add_constructor("!LogNormal", constructor_from_class(LogNormal))

  return loader

"""
try:
    config = yaml.load(open('perfect_foresight_full_experimental.yaml', 'r'), Loader= get_loader())

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

    a_str = config['model']['blocks']['consumption']['dynamics']['a']
    a_expr = parse_expr(a_str)
    a_func = lambdify(list(a_expr.free_symbols), a_expr, "numpy")

    m = np.random.random(100)
    c = np.random.random(100)

    #import pdb; pdb.set_trace()

except yaml.YAMLError as exc:
    print("Error in configuration file:", exc)
"""