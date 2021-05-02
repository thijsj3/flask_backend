import json
import os


def stories():
    location = './stories'
    stories = []
    for filename in os.listdir(location):
        with open(location + '/' + filename, 'r', encoding='utf8') as file:
            data = file.read()
            title = (data[data.rfind("title: ")+len("title: ")
                     :data.rfind("content: ")-1])
            content = (data[data.rfind("content: ") +
                       len("content: "):]).replace("\n", "\n\n")
            story = {"title": title, "content": content}
        stories.append(story)
    return stories
