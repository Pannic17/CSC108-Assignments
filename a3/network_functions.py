""" CSC108 Assignment 3: Social Networks - Starter code """

from typing import List, Tuple, Dict, TextIO


def name_format(profiles_file: TextIO) -> List[str]:
    """Return a list of names with correct format
    """
    count = -1
    index = 0
    name = ''
    file_line = profiles_file.readlines()
    for string in file_line:
        count = count + 1
        if ',' in file_line[count]:
            line = string[:-2]
            index = line.index(",")
            name = line[index + 2:] + '' + line[:index - 1]
            file_line[count] = name
    return file_line


def load_profiles(profiles_file: TextIO, person_to_friends: Dict[str, List[str]], \
                  person_to_networks: Dict[str, List[str]]) -> None:
    """Update the "person to friends" dictionary person_to_friends and the
    "person to networks" dictionary person_to_networks to include data from
    profiles_file.
    """
    file_line = name_format(profiles_file)
    count = -1
    index = ''
    for string in file_line:
        count = count + 1
        if string != '\n':
            if count == 0 or file_line[count - 1] == '\n':
                index = string
                if not (index in person_to_friends):
                    person_to_friends[index] = []
                if not (index in person_to_networks):
                    person_to_networks[index] = []
            elif '\n' in string:
                person_to_networks[index].append(string[:2])
            else:
                person_to_friends[index].append(string)


def get_average_friend_count(person_to_friends: Dict[str, List[str]]) -> float:
    """Return the average number of friends
    """
    p = 0
    q = 0
    for person_name in person_to_friends:
        p = p + 1
        q = q + len(person_to_friends[person_name])
    if p > 0:
        return q / p
    else:
        return 0.0


def get_families(person_to_friends: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """Return a "last name to first names" dictionary
    based on the given "person to friends" dictionary. 
    """
    last_name_to_first_names = {}
    for i in person_to_friends:
        for j in person_to_friends[i]:
            space_index = j.rindex(' ')
            if not (j[space_index + 1:] in last_name_to_first_names):
                last_name_to_first_names[j[space_index + 1:]] = []
            if not (j[0:space_index] in last_name_to_first_names[j[space_index + 1:]]):
                last_name_to_first_names[j[space_index + 1:]].append(j[0:space_index])
        space_index = i.rindex(' ')
        if not (i[space_index + 1:] in last_name_to_first_names):
            last_name_to_first_names[i[space_index + 1:]] = []
        if not (i[0:space_index] in last_name_to_first_names[i[space_index + 1:]]):
            last_name_to_first_names[i[space_index + 1:]].append(i[0:space_index])
    for k in last_name_to_first_names:
        last_name_to_first_names[k].sort()
    return last_name_to_first_names


def invert_network(person_to_networks: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """Return a "network to people" dictionary 
    based on the given "person to networks" dictionary.
    The values in the dictionary are sorted alphabetically.
    """
    network_to_people = {}
    for i in person_to_networks:
        for j in person_to_networks[i]:
            if not (j in network_to_people):
                network_to_people[j] = []
            if not (i in network_to_people[j]):
                network_to_people[j].append(i)
    return network_to_people


def get_friends_of_friends(person_to_friends: Dict[str, List[str]], \
                           person: str) -> List[str]:
    """Given a "person to friends" dictionary and the name of a person
    return the list of names of people who are friends of the named person's friends. 
    """
    friends_of_friends = []
    for i in person_to_friends[person]:
        for j in person_to_friends:
            for k in person_to_friends[j]:
                if i == j and k != person:
                    friends_of_friends.append(k)
    friends_of_friends.sort()
    return friends_of_friends


def recommend_friends(person: str, person_to_friends: Dict[str, List[str]]) -> List[str]:
    """return a name to add a score according to friends
    """
    name_list = []
    for pi in person_to_friends[person]:
        for pj in person_to_friends:
            for pk in person_to_friends[pj]:
                if pi == pj and pk != person:
                    name_list.append(pk)
    return name_list


def recommend_networks(person: str, person_to_networks: Dict[str, List[str]]) \
        -> List[str]:
    """return a name to add a score according to networks
    """
    name_list = []
    for ni in person_to_networks[person]:
        for nj in person_to_networks:
            for nk in person_to_networks[nj]:
                if ni == nk and nj != person:
                    name_list.append(nj)
    return name_list


def basic_recommend(person: str, person_to_friends: Dict[str, List[str]], \
                    person_to_networks: Dict[str, List[str]]) -> Dict[str, int]:
    """return a list of friend with basic calculation
    """
    recommendations = {}
    if not person in person_to_friends:
        person_to_friends[person] = []
    if not person in person_to_networks:
        person_to_networks[person] = []
    # friends
    plist = recommend_friends(person, person_to_friends)
    for pk in plist:
        if not (pk in recommendations):
            recommendations[pk] = 1
        else:
            recommendations[pk] = recommendations[pk] + 1
    # networks
    nlist = recommend_networks(person, person_to_networks)
    for nj in nlist:
        if not (nj in recommendations):
            recommendations[nj] = 1
        else:
            recommendations[nj] = recommendations[nj] + 1
    return recommendations


def recommend_score(person: str, person_to_friends: Dict[str, List[str]], \
                    person_to_networks: Dict[str, List[str]]) -> Dict[str, int]:
    """Return a dictionary for sort of recommend friends and their score
    """
    recommendations = basic_recommend(person, person_to_friends, person_to_networks)
    # family
    fk = ''
    for fi in person_to_friends:
        if person[person.rindex(' '):] == fi[fi.rindex(' '):]:
            fk = fi
            if fk in recommendations:
                recommendations[fk] = recommendations[fk] + 1
        for fj in person_to_friends[fi]:
            if person[person.rindex(' '):] == fj[fj.rindex(' '):]:
                fk = fj
                if fk in recommendations:
                    recommendations[fk] = recommendations[fk] + 1
    return recommendations


def make_recommendations(person: str, person_to_friends: Dict[str, List[str]], \
                         person_to_networks: Dict[str, List[str]]) -> List[Tuple[str, int]]:
    """Return a list of recommendations of friends in format of Tuple
    """
    recommendations = recommend_score(person, person_to_friends, person_to_networks)
    # sort





    recommend_list = []
    for name in recommendations:
        # define
        score = recommendations[name]
        tup = (name, score)
        sequence = 0
        if recommend_list == []:
            # start
            recommend_list.append(tup)
        else:
            # rest
            while sequence < len(recommend_list):
                # loop count
                if score > recommend_list[sequence][1]:
                    # bigger
                    recommend_list.insert(sequence, tup)
                    sequence = len(recommend_list)
                elif score == recommend_list[sequence][1] and \
                        name < recommend_list[sequence][0]:
                    # equal
                    recommend_list.insert(sequence, tup)
                    sequence = len(recommend_list)
                sequence = sequence + 1
        if tup not in recommend_list:
            # smallest
            recommend_list.append(tup)
    # return
    return recommend_list


if __name__ == '__main__':
    import doctest

    doctest.testmod()
