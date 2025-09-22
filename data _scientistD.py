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
total_connections = sum(number_of_friends user) for user in users)
from __future__ import division
num_users = len(users)
avg_connections = total_connections / num_users
num_frienf_by_id = [(user["id"], number_of_friends(user)) for user in users]
sorted(num_frienf_by_id, key=lambda (user_id, num_friends): num_friends, reverse=True)
