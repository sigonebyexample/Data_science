users = [
    { "id": 0, "name": "Alice" },
    { "id": 1, "name": "Bob" },
    { "id": 2, "name": "Charlie" },
    { "id": 3, "name": "David" },
    { "id": 4, "name": "Eve" },
    { "id": 5, "name": "Frank" },
    { "id": 6, "name": "Grace" },
    { "id": 7, "name": "Heidi" },
    { "id": 8, "name": "Ivan" },
    { "id": 9, "name": "Judy" }
]

friendships = [ (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9) ]

for user in users:
    user["friends"] = []

for i, j in friendships:
    users[i]["friends"].append(users[j])  # add j as a friend of i
    users[j]["friends"].append(users[i])  # add i as a friend of j

def number_of_friends(user):
    return len(user["friends"])

total_connections = sum(number_of_friends(user) for user in users)

num_users = len(users)
avg_connections = total_connections / num_users

number_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

# Corrected line - use indexing instead of tuple unpacking in lambda
sorted_friends = sorted(number_friends_by_id,
                       key=lambda x: x[1],  # x[1] refers to num_friends
                       reverse=True)

print("Users sorted by number of friends (descending):")
for user_id, num_friends in sorted_friends:
    print(f"User {user_id}: {num_friends} friends")


def friends_of_friend_ids_bad(user):
    return [foaf["id"]
           for friend in user["friends"]
           for foaf in friend["friends"]]

from collections import Counter

def not_the_same(user, other_user):
    return user["id"] != other_user["id"]

def not_friends(user, other_user):
    return all(not_the_same(friend, other_user)
               for friend in user["friends"])

def friends_of_friend_ids(user):
    return Counter(foaf["id"]
                   for friend in user["friends"]
                   for foaf in friend["friends"]
                   if not_the_same(user, foaf)
                   and not_friends(user, foaf))

# Corrected: Access user with id=5 from the users list
user_5 = next(user for user in users if user["id"] == 5)
print("Friends of friends for user 5:", friends_of_friend_ids(user_5))

# Or alternatively, if you want to access by list index (but this is less reliable):
# print("Friends of friends for user 5:", friends_of_friend_ids(users[5]))
interests = [
(0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
(0, "Spark"), (0, "Storm"), (0, "Cassandra"),
(1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
(1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
(2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
(3, "statistics"), (3, "regression"), (3, "probability"),
(4, "machine learning"), (4, "regression"), (4, "decision trees"),
(4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
(5, "Haskell"), (5, "programming languages"), (6, "statistics"),
(6, "probability"), (6, "mathematics"), (6, "theory"),
(7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
(7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
(8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
(9, "Java"), (9, "MapReduce"), (9, "Big Data")
]
def data_scientists_who_like(target_interest):
    return [user_id
            for user_id, interest in interests
            if interest == target_interest]
from collections import defaultdict
user_id_by_interest= defaultdict(list)
for user_id, interest in interests:
    user_id_by_interest[interest].append(user_id)
