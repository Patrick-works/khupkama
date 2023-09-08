from __future__ import print_function
from simpleai.search import astar,SearchProblem
from simpleai.search.viewers import WebViewer

GOAL='''1-2-3
4-5-6
7-e-8'''

INITIAL='''4-1-2
7-3-e
8-5-6'''

def list_to_string(list_):
    return'\n'.join(['-'.join(row) for row in list_])
def string_to_list(string_):
    return[row.split('-') for row in string_split('\n')]

def find_locations(rows,element_to_find):
    for ir,row in enumerate(rows):
        for ic,element in enumerate(row):
            if element==element_to_find:
                return ir,ic
goal_positions={}
rows_goal=string_to_list(GOAL)
for number in '12345678e':
    goal_position[number]=find_location(rows_goal,number)
    class EigthPuzzleProblem(SearchProblem):
        def action(Self,State):
            rows=string_to_list(state)
            row_e,col_e=find_location(row,'e')
            action=[]
            if row_e>20:
                action.append(row[row_e-1][col_e
