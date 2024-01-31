'''
Make a quick workflow diagram for HARK meeting.
'''
import graphviz

HARKflow = graphviz.Digraph(comment='workflow for HARK')

HARKflow.node('HARK1', 'HARK 1.0', rank='sink')

with HARKflow.subgraph() as x:
    x.attr(rank='same')
    x.node('params','parameter \n improvements')
    x.node('solve', 'solver \n improvements')
    x.node('sim', 'simulation \n improvements')

with HARKflow.subgraph() as y:
    y.attr(rank='same')
    y.node('A', 'undo hierarchy \n among solvers')
    y.node('B', 'automated simulation \n from model dynamics')
    y.node('C2', 'rewrite input \n constructors')
    y.node('D', 'add "parameters \n block" to models')
    y.node('H', 'multiple "modes" \n for simulation')

with HARKflow.subgraph() as z:
    z.attr(rank='same')
    z.node('F', 'make parser for simulation', shape='rectangle')
    z.node('G', 'make parser for auto-solution', shape='rectangle')
    z.node('I', 'make "type \n constructor"', shape='rectangle')

HARKflow.node('C1', 'new system for \n constructed inputs')
HARKflow.node('E', 'design micro \n syntax for DSL', shape='rectangle', rank='source')

HARKflow.edge('params','HARK1')
HARKflow.edge('solve','HARK1')
HARKflow.edge('sim','HARK1')
HARKflow.edge('C1','C2')
HARKflow.edge('C2','params')
HARKflow.edge('D','params')
HARKflow.edge('A','solve')
HARKflow.edge('B','sim')
HARKflow.edge('H','sim')
HARKflow.edge('E','I')
HARKflow.edge('E','F')
HARKflow.edge('E','G')
HARKflow.edge('I','C2',style='invis')
HARKflow.edge('I','params')
HARKflow.edge('G','solve')
HARKflow.edge('F','sim')



