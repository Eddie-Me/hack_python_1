"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    result = result.upper()
    result = result.replace("O", "0")
    result = result.replace ("I", "1")
    result = result.replace ("A", "@")
    result= list(result)
    return result

print(fn_hack_10())  