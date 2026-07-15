def commands(binary_str):
    
    actions = ["wink", "double blink", "close your eyes", "jump"]
    result = [action for bit, action in zip(binary_str[-4:][::-1], actions) if bit == "1"]


    return result[::-1] if binary_str[-5] == "1" else result