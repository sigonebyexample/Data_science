"""
Social Network Analysis Example
This script demonstrates basic social network analysis concepts using Python.
It analyzes friendships between users and finds mutual connections.
"""

# Define our list of users with unique IDs and names
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

# Define friendship connections as tuples of user IDs
friendships = [ (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9) ]

# Initialize empty friends list for each user
for user in users:
    user["friends"] = []

# Build the friendship network - make connections bidirectional
for i, j in friendships:
    users[i]["friends"].append(users[j])  # add j as a friend of i
    users[j]["friends"].append(users[i])  # add i as a friend of j

def number_of_friends(user):
    """Calculate the number of friends for a given user."""
    return len(user["friends"])

# Calculate total connections in the network
total_connections = sum(number_of_friends(user) for user in users)

# Calculate average number of connections per user
num_users = len(users)
avg_connections = total_connections / num_users

# Create a list of tuples containing user ID and their friend count
number_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

# Sort users by number of friends in descending order
sorted_friends = sorted(number_friends_by_id,
                       key=lambda x: x[1],  # Sort by the second element (friend count)
                       reverse=True)

print("Users sorted by number of friends (descending):")
for user_id, num_friends in sorted_friends:
    print(f"User {user_id}: {num_friends} friends")

def friends_of_friend_ids_bad(user):
    """
    Get all friends-of-friends IDs (naive approach).
    This includes duplicates and doesn't exclude direct friends.
    """
    return [foaf["id"]  # foaf = Friend Of A Friend
           for friend in user["friends"]  # For each direct friend
           for foaf in friend["friends"]]  # Get all of their friends

from collections import Counter  # Import Counter for counting mutual friends

def not_the_same(user, other_user):
    """Check if two users are different people."""
    return user["id"] != other_user["id"]

def not_friends(user, other_user):
    """Check if other_user is not already a direct friend of user."""
    return all(not_the_same(friend, other_user)
               for friend in user["friends"])

def friends_of_friend_ids(user):
    """
    Find friends-of-friends with counts (proper implementation).
    Returns a Counter object with friend IDs and how many mutual friends they have.
    """
    return Counter(foaf["id"]  # Count occurrences of each friend-of-friend ID
                   for friend in user["friends"]  # For each direct friend
                   for foaf in friend["friends"]  # For each of their friends
                   if not_the_same(user, foaf)  # Exclude the user themselves
                   and not_friends(user, foaf))  # Exclude direct friends

# Method 1: Safe way to get user by ID (recommended)
# Find the user with ID 5 using a generator expression
user_5 = next(user for user in users if user["id"] == 5)
print("\nFriends of friends for user 5 (safe method):", friends_of_friend_ids(user_5))

# Method 2: Direct list index access (works in this specific case)
# This works because user IDs match list indices, but isn't reliable in general
print("Friends of friends for user 5 (direct index):", friends_of_friend_ids(users[5]))

# Print additional network statistics
print(f"\nNetwork Statistics:")
print(f"Total users: {num_users}")
print(f"Total connections: {total_connections}")
print(f"Average connections per user: {avg_connections:.2f}")

# Display each user's friends
print(f"\nDetailed friend lists:")
for user in users:
    friend_names = [friend["name"] for friend in user["friends"]]
    print(f"{user['name']} (ID {user['id']}) is friends with: {', '.join(friend_names)}")
