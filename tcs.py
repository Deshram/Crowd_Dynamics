import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from pprint import pprint
from crmon1 import bnimate

"""states = ['slow', 'med', 'fast']
pi = [0.35,0.35,0.3]
state_space = pd.Series(pi, index=states, name='states')
print(state_space)
print(state_space.sum())

q_df = pd.DataFrame(columns=states, index=states)
q_df.loc[states[0]] = [0.3, 0.3, 0.4]
q_df.loc[states[1]] = [0.45, 0.45, 0.1]
q_df.loc[states[2]] = [0.45, 0.25, .3]

print(q_df)

q = q_df.values
print('\n', q, q.shape, '\n')
print(q_df.sum(axis=1))
def _get_markov_edges(Q):
    edges = {}
    for col in Q.columns:
        for idx in Q.index:
            edges[(idx,col)] = Q.loc[idx,col]
    return edges

edges_wts = _get_markov_edges(q_df)
pprint(edges_wts)

hidden_states = ['low', 'medium', 'high']
pi = [(1/3),(1/3),(1/3)]
state_space = pd.Series(pi, index=hidden_states, name='states')
print(state_space)
print('\n', state_space.sum())
a_df = pd.DataFrame(columns=hidden_states, index=hidden_states)
a_df.loc[hidden_states[0]] = [0.2, 0.4, 0.4]
a_df.loc[hidden_states[1]] = [0.3, 0.3, 0.4]
a_df.loc[hidden_states[2]] = [0.2, 0.2, 0.6]
print(a_df)
a = a_df.values
print('\n', a, a.shape, '\n')
print(a_df.sum(axis=1))
observable_states = states
b_df = pd.DataFrame(columns=observable_states, index=hidden_states)
b_df.loc[hidden_states[0]] = [0.2, 0.6, 0.2]
b_df.loc[hidden_states[1]] = [0.4, 0.1, 0.5]
b_df.loc[hidden_states[2]] = [0.2,0.2,0.6]
print(b_df)
b = b_df.values
print('\n', b, b.shape, '\n')
print(b_df.sum(axis=1))
hide_edges_wts = _get_markov_edges(a_df)
pprint(hide_edges_wts)

emit_edges_wts = _get_markov_edges(b_df)
pprint(emit_edges_wts)"""

obs_map = {'slow':0, 'med':1, 'fast':2}
#Change your data below
obs = np.array([])
sc = bnimate(1)
obs = np.append(obs,sc[0])
print(obs)

"""inv_obs_map = dict((v,k) for k, v in obs_map.items())
obs_seq = [inv_obs_map[v] for v in list(obs)]

print( pd.DataFrame(np.column_stack([obs, obs_seq]), 
                    columns=['Obs_code', 'Obs_seq']) )
def viterbi(pi, a, b, obs):
    
    nStates = np.shape(b)[0]
    T = np.shape(obs)[0]
    
    
    path = np.zeros(T,dtype=int)
    
    delta = np.zeros((nStates, T))
    
    phi = np.zeros((nStates, T))
    delta[:, 0] = pi * b[:, obs[0]]
    phi[:, 0] = 0

    print('\nStart Walk Forward\n')    
    for t in range(1, T):
        for s in range(nStates):
            delta[s, t] = np.max(delta[:, t-1] * a[:, s]) * b[s, obs[t]] 
            phi[s, t] = np.argmax(delta[:, t-1] * a[:, s])
            print('s={s} and t={t}: phi[{s}, {t}] = {phi}'.format(s=s, t=t, phi=phi[s, t]))
    print('-'*50)
    print('Start Backtrace\n')
    path[T-1] = np.argmax(delta[:, T-1])
    for t in range(T-2, -1, -1):
        path[t] = phi[path[t+1], [t+1]]
        print('path[{}] = {}'.format(t, path[t]))
        
    return path, delta, phi

path, delta, phi = viterbi(pi, a, b, obs)
print('\nsingle best state path: \n', path)
print('delta:\n', delta)
print('phi:\n', phi)
state_map = {0:'low', 1:'medium',2:'fast'}
state_path = [state_map[v] for v in path]

(pd.DataFrame().assign(Observation=obs_seq).assign(Best_Path=state_path))
"""