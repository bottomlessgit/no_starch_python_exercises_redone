# Base code taken from pg 153 of text as per question instructions
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

me = build_profile('john', 
                    'doe', 
                    location='senegal',
                    field='accounting',
                    prime_derective='to boldly go where no one has gone before',
                    hair_color='blue',
                    eye_color = 'orange')
print(me)