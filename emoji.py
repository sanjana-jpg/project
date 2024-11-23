emoji = {
    "☺": "smiling face with smiling eyes"
    "😂":"face with tears of joy"
    "😗": "kissing face"
    "😶":"face without mouth"
    "😥": "sad but relieved face"
    "😴":"sleeping face"
    "😋": "face savoring food"
}

def emoji_to_text(emoji):
    return emoji_dict.get(emoji, "unknown emoji")


print("welcome to the emoji to text converter")
emoji_input = input("enter an emoji")

text_output = emoji - to - text(emoji_input)
print(f"the mesning of the emoji is {text_output}")
