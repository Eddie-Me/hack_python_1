"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "fooziman"
    result = "".join(reversed(result))
    result = "".join(reversed(result.capitalize()))
    return result

print(fn_hack_4())