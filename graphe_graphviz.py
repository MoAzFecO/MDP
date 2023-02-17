import graphviz 

# Define the MDP as a directed graph
g = graphviz.Digraph('G', filename='mdp.gv', engine='dot')

# Define the states
g.attr('node', shape='circle')
g.node('S0', shape='doublecircle')
g.node('S1')
g.node('S2', peripheries='2')

# Add arrow to the first state
#g.attr('node', shape='point')
g.node('Start', label='', shape='point')
g.edge('Start', 'S0', arrowhead='vee')

# Define the actions and transitions
g.attr('node', shape='point')
g.edge('S0', 'a', label='a', dir='none', color='red')
g.edge('S0', 'b', label='b', dir='none', fontcolor='blue')
g.edge('b', 'S0', label='0.6', color='magenta', fontcolor='magenta')
g.edge('b', 'S1', label='0.2')
g.edge('b', 'S2', label='0.2')
g.edge('a', 'S1', label='0.2')
g.edge('a', 'S2', label='0.8')

# Render the graph
g.render('mdp', format='png', view=False)
