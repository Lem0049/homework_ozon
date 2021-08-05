def get_value(d_ry, value):
    film_collection = [k for k, v in d_ry.items() if v == value]
    return film_collection


'''This program calculates average of rating for serials in the same genre'''


def get_average(d_ry, scroll):
    rating_coll = []  # create empty  list
    for i in scroll:  # condition for sort Film by rating
        rating_coll.append(d_ry[i])  # append rating in list
    return float(sum(rating_coll)) / len(rating_coll)  # calculates average of rating
