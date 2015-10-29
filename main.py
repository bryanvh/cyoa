#!/usr/bin/python

class Path:
    def __init__(self, response):
        self.response = response
        self.target = None

    def create_vertex(self, story):
        self.target = Vertex(story)
        return self.target

    def display(self, indent=''):
        print '%s%s' % (indent, self.response)
        self.target.display(indent + ' ')

class Vertex:
    def __init__(self, story):
        self.paths = []
        self.story = story
        
    def create_path(self, response):
        path = Path(response)
        self.paths.append(path)
        return path

    def display(self, indent=''):
        print '%s%s' % (indent, self.story)
        for p in self.paths:
            p.display(indent + ' ')

step01 = Vertex('You are Hubert the Yellow.')
path = step01.create_path('accept')
step02 = path.create_vertex('The king is pleased!')
path = step01.create_path('decline')
step03 = path.create_vertex('You have chosen... poorly!')

step01.display()
