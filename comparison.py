import json

def load_usernames(path):
    """
    Load a JSON file and return the set of all 'value' fields
    inside any string_list_data entries.
    Handles both:
      [{…}, {…}, …]
    and
      {"relationships_following": [{…}, …]}
    """
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, dict) and "relationships_following" in data:
        entries = data["relationships_following"]
    else:
        entries = data

    names = set()
    for rel in entries:
        for item in rel.get("string_list_data", []):
            if "value" in item:
                names.add(item["value"])
    return names

followers = load_usernames("followers_1.json")
following = load_usernames("following.json")

not_following_back = following - followers

print("People you follow who don't follow you back:")
for user in sorted(not_following_back):
    print("-", user)
