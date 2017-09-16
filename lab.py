# NO IMPORTS ALLOWED!

import json

#required
def did_x_and_y_act_together(data, actor_id_1, actor_id_2):
    '''
    :param data: The database to check the relationship between the two actors
    :param actor_id_1: The id number of one of the actors
    :param actor_id_2: The id number of the other actor
    :return: A boolean of whether the actors have worked together before
    '''
    for pair in data:
        if (pair[0] == actor_id_1 and pair[1] == actor_id_2) \
        or (pair[0] == actor_id_2 and pair[1] == actor_id_1):
            return True
    return False

#required
def get_actors_with_bacon_number(data, n):
    '''
    :param data: The database containing the actors
    :param n: The degree of separation between Bacon and the actors
    :return: A list containing the ID numbers of all actors with a Bacon number of n
    '''
    BACON_ID = 4724
    degree_list = [BACON_ID]
    visited = {BACON_ID}
    for i in range(n):
        print("degree:", i) #!!!!
        worked_with = get_worked_with_set(data, degree_list)
        degree_list = []
        for actor_id in worked_with:
            if not (actor_id in visited):
                degree_list.append(actor_id)
                visited.add(actor_id)
    return degree_list

def convert_to_dict(data):
    '''
    :param data:
    :return:
    '''
    output = {}
    #entry is [actor_id1, actor_id2, movie_id]
    for entry in data:
        if entry[0] in output.keys():
            output[entry[0]].add(entry[1])
        else:
            output[entry[0]] = set(entry[1])

        if entry[1] in output.keys():
            output[entry[1]].add(entry[0])
        else:
            output[entry[1]] = set(entry[0])

    return output


def get_actor_name(data, actor_id):
    '''

    :param data: The database mapping actor ids to actor names
    :param actor_id: The id of the actor
    :return: The actor's name
    '''
    return str(data[actor_id])  # cast should be unneccesary

def get_worked_with_actor(data, actor_id):
    '''
    :param data:
    :param actor_id: A list of the ids of the actors from whom the list branches
    :return: A set of actor ids for actors who have worked with this actor
    '''

    #go through all pairs
    #if pair contains id in list
    #add that id to the output list

    output = set()
    #pair is a list of 2 actor ids and a movie id
    for pair in data:
        if (actor_id == pair[0] and actor_id != pair[1]):
            output.add(pair[1])

        elif(actor_id == pair[1] and actor_id != pair[0]):
            output.add(pair[0])
    return output

def get_worked_with_set(data, actor_id_set):
    '''
    :param data: The data set of actors
    :param actor_id_set: A set of actor ids
    :return: A set of actors' ids who have worked with the initial set of actors
    '''

    output = set()
    for actor in actor_id_set:
        print("next actor same set", actor)
        output.update(get_worked_with_actor(data, actor))
    return output

#required
def get_bacon_path(data, actor_id):
    BACON_ID = 4724
    return get_path(data, BACON_ID, actor_id)

#required
def get_path(data, actor_id_1, actor_id_2):
    initPath = [actor_id_1]
    pathQueue = [initPath]
    while len(pathQueue) != 0:
        tempPath = pathQueue.pop(0)
        lastNode = tempPath[-1]
        if lastNode == actor_id_2:
            return tempPath
        for nextNode in set(get_worked_with_actor(data, lastNode)):
            if nextNode not in tempPath:
                newPath = tempPath+[nextNode]
                pathQueue.append(newPath)
    return None


if __name__ == '__main__':
    # with open('resources/small.json') as f:
    #     smalldb = json.load(f)

    # additional code here will be run only when lab.py is invoked directly
    # (not when imported from test.py), so this is a good place to put code
    # used, for example, to generate the results for the online questions.

    #Test 1
    # filename = 'resources/names.json'
    # with open(filename, 'r') as f:
    #     data = json.load(f)
    # for key in data.keys():
    #     if data[key] == 1372470:
    #         print(key)

    #Test 2
    # names_file = 'resources/names.json'
    # movies_together_file = 'resources/small.json'
    # with open(movies_together_file, 'r') as f:
    #     movies_together = json.load(f)
    # with open(names_file, 'r') as f:
    #     names = json.load(f)
    #
    # actor1 = names['Shii Ann Huang']
    # actor2 = names['Barbara Flynn']
    # print (did_x_and_y_act_together(movies_together, actor1, actor2))

    #Test 3: small Bacon 3
    # small = 'resources/small.json'
    # with open(small, 'r') as f:
    #     small = json.load(f)
    #
    # #maps strings to numbers
    # small_names = 'resources/small_names.json'
    # with open(small_names, 'r') as f:
    #     small_names = json.load(f)
    #
    # actor_ids = set(get_actors_with_bacon_number(small, 4))
    # actor_names = []
    #
    # for name in small_names.keys():
    #     if small_names[name] in actor_ids:
    #         actor_names.append(name)
    # print(actor_names)

    #Test 3b: large Bacon 5
    small = 'resources/large.json'
    with open(small, 'r') as f:
        small = json.load(f)

    # maps strings to numbers
    small_names = 'resources/names.json'
    with open(small_names, 'r') as f:
        small_names = json.load(f)

    actor_ids = set(get_actors_with_bacon_number(small, 5))
    actor_names = []

    for name in small_names.keys():
        if small_names[name] in actor_ids:
            actor_names.append(name)
    print(actor_names)

    # large = 'resources/large.json'
    # with open(large, 'r') as f:
    #     large = json.load(f)
    #
    # small = 'resources/small.json'
    # with open(small, 'r') as f:
    #     small = json.load(f)