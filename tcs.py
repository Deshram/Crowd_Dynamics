import numpy as np
import pandas as pd
import networkx as nx
import os
#os.environ["PROJ_LIB"]="C:\ProgramData\Anaconda3\pkgs\proj4-5.2.0-ha925a31_1\Library\share"
import matplotlib.pyplot as plt
from pprint import pprint
from crmon1 import bnimate
 


states = ['slow', 'med', 'fast']
pi = [0.35,0.35,0.3]
state_space = pd.Series(pi, index=states, name='states')
# print(state_space)
# print(state_space.sum())
q_df = pd.DataFrame(columns=states, index=states)
q_df.loc[states[0]] = [0.3, 0.3, 0.4]
q_df.loc[states[1]] = [0.45, 0.45, 0.1]
q_df.loc[states[2]] = [0.45, 0.25, .3]
# print(q_df)
q = q_df.values
# print('\n', q, q.shape, '\n')
# print(q_df.sum(axis=1))
def _get_markov_edges(Q):
    edges = {}
    for col in Q.columns:
        for idx in Q.index:
            edges[(idx,col)] = Q.loc[idx,col]
    return edges
edges_wts = _get_markov_edges(q_df)
# pprint(edges_wts)
hidden_states = ['low', 'medium', 'high']
pi = [(1/3),(1/3),(1/3)]
state_space = pd.Series(pi, index=hidden_states, name='states')
# print(state_space)
# print('\n', state_space.sum())
a_df = pd.DataFrame(columns=hidden_states, index=hidden_states)
a_df.loc[hidden_states[0]] = [0.2, 0.4, 0.4]
a_df.loc[hidden_states[1]] = [0.3, 0.3, 0.4]
a_df.loc[hidden_states[2]] = [0.2, 0.2, 0.6]
# print(a_df)
a = a_df.values
# print('\n', a, a.shape, '\n')
# print(a_df.sum(axis=1))
observable_states = states
b_df = pd.DataFrame(columns=observable_states, index=hidden_states)
b_df.loc[hidden_states[0]] = [0.2, 0.6, 0.2]
b_df.loc[hidden_states[1]] = [0.4, 0.1, 0.5]
b_df.loc[hidden_states[2]] = [0.2,0.2,0.6]
# print(b_df)
b = b_df.values
# print('\n', b, b.shape, '\n')
# print(b_df.sum(axis=1))
hide_edges_wts = _get_markov_edges(a_df)
# pprint(hide_edges_wts)
emit_edges_wts = _get_markov_edges(b_df)
# pprint(emit_edges_wts)

obs_map = {'slow':0, 'med':1, 'fast':2}
obs2=[]
obs3=[]
obs4=[]
obs5=[]
obs6=[]
obs7=[]
obs8=[]
obs9=[]
obs10=[]
obs11=[]
obs12=[]
obs13=[]
obs14=[]
obs15=[]
obs16=[]
obs17=[]
obs18=[]
obs19=[]
obs20=[]
obs21=[]
file1 = open("output.txt","r+")
file2 = open("output2.txt","r+")
file3 = open("output3.txt","r+")
file4 = open("output4.txt","r+")
file5 = open("output5.txt","r+")
file6 = open("output6.txt","r+")
file7 = open("output7.txt","r+")
file8 = open("output8.txt","r+")
file9 = open("output9.txt","r+")
file10 = open("output10.txt","r+")
file11 = open("output11.txt","r+")
file12 = open("output12.txt","r+")
file13 = open("output13.txt","r+")
file14 = open("output14.txt","r+")
file15 = open("output15.txt","r+")
file16 = open("output16.txt","r+")
file17 = open("output17.txt","r+")
file18 = open("output18.txt","r+")
file19 = open("output19.txt","r+")
file20 = open("output20.txt","r+")
sc=bnimate(1)
with open('output.txt') as f:
    obs2 = f.read().splitlines()
with open('output2.txt') as f:
    obs3 = f.read().splitlines()
with open('output3.txt') as f:
    obs4 = f.read().splitlines()
with open('output4.txt') as f:
    obs5 = f.read().splitlines()
with open('output5.txt') as f:
    obs6 = f.read().splitlines()
with open('output6.txt') as f:
    obs7 = f.read().splitlines()
with open('output7.txt') as f:
    obs8 = f.read().splitlines()
with open('output8.txt') as f:
    obs9 = f.read().splitlines()
with open('output9.txt') as f:
    obs10 = f.read().splitlines()
with open('output10.txt') as f:
    obs11 = f.read().splitlines()
with open('output11.txt') as f:
    obs12 = f.read().splitlines()
with open('output12.txt') as f:
    obs13 = f.read().splitlines()
with open('output13.txt') as f:
    obs14 = f.read().splitlines()
with open('output14.txt') as f:
    obs15 = f.read().splitlines()
with open('output15.txt') as f:
    obs16 = f.read().splitlines()
with open('output16.txt') as f:
    obs17 = f.read().splitlines()
with open('output17.txt') as f:
    obs18 = f.read().splitlines()
with open('output18.txt') as f:
    obs19 = f.read().splitlines()
with open('output19.txt') as f:
    obs20 = f.read().splitlines()
with open('output20.txt') as f:
    obs21 = f.read().splitlines()

obs2=[int(i) for i in obs2]
obs3=[int(i) for i in obs3]
obs4=[int(i) for i in obs4]
obs5=[int(i) for i in obs5]
obs6=[int(i) for i in obs6]
obs7=[int(i) for i in obs7]
obs8=[int(i) for i in obs8]
obs9=[int(i) for i in obs9]
obs10=[int(i) for i in obs10]
obs11=[int(i) for i in obs11]
obs12=[int(i) for i in obs12]
obs13=[int(i) for i in obs13]
obs14=[int(i) for i in obs14]
obs15=[int(i) for i in obs15]
obs16=[int(i) for i in obs16]
obs17=[int(i) for i in obs17]
obs18=[int(i) for i in obs18]
obs19=[int(i) for i in obs19]
obs20=[int(i) for i in obs20]
obs21=[int(i) for i in obs21]

file1.truncate(0)
file1.close()

file2.truncate(0)
file2.close()

file3.truncate(0)
file3.close()

file4.truncate(0)
file4.close()

file5.truncate(0)
file5.close()

file6.truncate(0)
file6.close()

file7.truncate(0)
file7.close()

file8.truncate(0)
file8.close()

file9.truncate(0)
file9.close()

file10.truncate(0)
file10.close()

file11.truncate(0)
file11.close()

file12.truncate(0)
file12.close()

file13.truncate(0)
file13.close()

file14.truncate(0)
file14.close()

file15.truncate(0)
file15.close()

file16.truncate(0)
file16.close()

file17.truncate(0)
file17.close()

file18.truncate(0)
file18.close()

file19.truncate(0)
file19.close()

file20.truncate(0)
file20.close()

# obs = np.append(obs,sc)
# obs2.append(sc[1])
obs2=np.asarray(obs2)
obs3=np.asarray(obs3)
obs4=np.asarray(obs4)
obs5=np.asarray(obs5)
obs6=np.asarray(obs6)
obs7=np.asarray(obs7)
obs8=np.asarray(obs8)
obs9=np.asarray(obs9)
obs10=np.asarray(obs10)
obs11=np.asarray(obs11)
obs12=np.asarray(obs12)
obs13=np.asarray(obs13)
obs14=np.asarray(obs14)
obs15=np.asarray(obs15)
obs16=np.asarray(obs16)
obs17=np.asarray(obs17)
obs18=np.asarray(obs18)
obs19=np.asarray(obs19)
obs20=np.asarray(obs20)
obs21=np.asarray(obs21)
# print(obs)

# print(obs)
inv_obs_map = dict((v,k) for k, v in obs_map.items())
obs_seq = [inv_obs_map[v] for v in list(obs2)]
obs_seq2 = [inv_obs_map[v] for v in list(obs3)]
obs_seq3 = [inv_obs_map[v] for v in list(obs4)]
obs_seq4 = [inv_obs_map[v] for v in list(obs5)]
obs_seq5 = [inv_obs_map[v] for v in list(obs6)]
obs_seq6 = [inv_obs_map[v] for v in list(obs7)]
obs_seq7 = [inv_obs_map[v] for v in list(obs8)]
obs_seq8 = [inv_obs_map[v] for v in list(obs9)]
obs_seq9 = [inv_obs_map[v] for v in list(obs10)]
obs_seq10 = [inv_obs_map[v] for v in list(obs11)]
obs_seq11 = [inv_obs_map[v] for v in list(obs12)]
obs_seq12 = [inv_obs_map[v] for v in list(obs13)]
obs_seq13 = [inv_obs_map[v] for v in list(obs14)]
obs_seq14 = [inv_obs_map[v] for v in list(obs15)]
obs_seq15 = [inv_obs_map[v] for v in list(obs16)]
obs_seq16 = [inv_obs_map[v] for v in list(obs17)]
obs_seq17 = [inv_obs_map[v] for v in list(obs18)]
obs_seq18 = [inv_obs_map[v] for v in list(obs19)]
obs_seq19 = [inv_obs_map[v] for v in list(obs20)]
obs_seq20 = [inv_obs_map[v] for v in list(obs21)]


# print( pd.DataFrame(np.column_stack([obs, obs_seq]), 
#                     columns=['Obs_code', 'Obs_seq']) )
def viterbi(pi, a, b, obs):
    
    nStates = np.shape(b)[0]
    T = np.shape(obs)[0]
    
    path = np.zeros(T,dtype=int)
    
    delta = np.zeros((nStates, T))
    
    phi = np.zeros((nStates, T))
    delta[:, 0] = pi * b[:, obs[0]]
    phi[:, 0] = 0

    # print('\nStart Walk Forward\n')    
    for t in range(1, T):
        for s in range(nStates):
            delta[s, t] = np.max(delta[:, t-1] * a[:, s]) * b[s, obs[t]] 
            phi[s, t] = np.argmax(delta[:, t-1] * a[:, s])
            # print('s={s} and t={t}: phi[{s}, {t}] = {phi}'.format(s=s, t=t, phi=phi[s, t]))
    # print('-'*50)
    # print('Start Backtrace\n')
    path[T-1] = np.argmax(delta[:, T-1])
    for t in range(T-2, -1, -1):
        path[t] = phi[path[t+1], [t+1]]
        # print('path[{}] = {}'.format(t, path[t]))
        
    return path, delta, phi
def printfunction():
	path1, delta, phi = viterbi(pi, a, b, obs2)
	print('\nsingle best state path: \n', path1)
	state_map = {0:'low', 1:'medium',2:'fast'}
	state_path = [state_map[v] for v in path1]

	path2, delta2, phi2 = viterbi(pi, a, b, obs3)
	print('\nsingle best state path: \n', path2)

	path3, delta3, phi3 = viterbi(pi, a, b, obs4)
	print('\nsingle best state path: \n', path3)

	path4, delta4, phi4 = viterbi(pi, a, b, obs5)
	print('\nsingle best state path: \n', path4)

	path5, delta5, phi5 = viterbi(pi, a, b, obs6)
	print('\nsingle best state path: \n', path5)

	path6, delta6, phi6 = viterbi(pi, a, b, obs7)
	print('\nsingle best state path: \n', path6)

	path7, delta7, phi7 = viterbi(pi, a, b, obs8)
	print('\nsingle best state path: \n', path7)

	path8, delta8, phi8 = viterbi(pi, a, b, obs9)
	print('\nsingle best state path: \n', path8)

	path9, delta9, phi9 = viterbi(pi, a, b, obs10)
	print('\nsingle best state path: \n', path9)

	path10, delta10, phi10 = viterbi(pi, a, b, obs11)
	print('\nsingle best state path: \n', path10)

	path11, delta11, phi11 = viterbi(pi, a, b, obs12)
	print('\nsingle best state path: \n', path11)

	path12, delta12, phi12 = viterbi(pi, a, b, obs13)
	print('\nsingle best state path: \n', path12)

	path13, delta13, phi13 = viterbi(pi, a, b, obs14)
	print('\nsingle best state path: \n', path13)

	path14, delta14, phi14 = viterbi(pi, a, b, obs15)
	print('\nsingle best state path: \n', path14)

	path15, delta15, phi15 = viterbi(pi, a, b, obs16)
	print('\nsingle best state path: \n', path15)

	path16, delta16, phi16 = viterbi(pi, a, b, obs17)
	print('\nsingle best state path: \n', path16)

	path17, delta17, phi17 = viterbi(pi, a, b, obs18)
	print('\nsingle best state path: \n', path17)

	path18, delta18, phi18 = viterbi(pi, a, b, obs19)
	print('\nsingle best state path: \n', path18)

	path19, delta19, phi19 = viterbi(pi, a, b, obs20)
	print('\nsingle best state path: \n', path19)

	path20, delta20, phi20 = viterbi(pi, a, b, obs21)
	print('\nsingle best state path: \n', path20)

	(pd.DataFrame().assign(Observation=obs_seq).assign(Best_Path=state_path))
	(pd.DataFrame().assign(Observation=obs_seq2).assign(Best_Path=state_path))
	(pd.DataFrame().assign(Observation=obs_seq3).assign(Best_Path=state_path))
	(pd.DataFrame().assign(Observation=obs_seq4).assign(Best_Path=state_path))
	(pd.DataFrame().assign(Observation=obs_seq5).assign(Best_Path=state_path))
	(pd.DataFrame().assign(Observation=obs_seq6).assign(Best_Path=state_path))
	(pd.DataFrame().assign(Observation=obs_seq7).assign(Best_Path=state_path))
	(pd.DataFrame().assign(Observation=obs_seq8).assign(Best_Path=state_path))
	(pd.DataFrame().assign(Observation=obs_seq9).assign(Best_Path=state_path))
	(pd.DataFrame().assign(Observation=obs_seq10).assign(Best_Path=state_path))
	(pd.DataFrame().assign(Observation=obs_seq11).assign(Best_Path=state_path))
	(pd.DataFrame().assign(Observation=obs_seq12).assign(Best_Path=state_path))
	(pd.DataFrame().assign(Observation=obs_seq13).assign(Best_Path=state_path))
	(pd.DataFrame().assign(Observation=obs_seq14).assign(Best_Path=state_path))
	(pd.DataFrame().assign(Observation=obs_seq15).assign(Best_Path=state_path))
	(pd.DataFrame().assign(Observation=obs_seq16).assign(Best_Path=state_path))
	(pd.DataFrame().assign(Observation=obs_seq17).assign(Best_Path=state_path))
	(pd.DataFrame().assign(Observation=obs_seq18).assign(Best_Path=state_path))
	(pd.DataFrame().assign(Observation=obs_seq19).assign(Best_Path=state_path))
	(pd.DataFrame().assign(Observation=obs_seq20).assign(Best_Path=state_path))
	return path1,path2,path3,path4,path5,path6,path7,path8,path9,path10,path11,path12,path13,path14,path15,path16,path17,path18,path19,path20
printfunction()