#!/usr/bin/env python

class TreeNode():
    def __init__(self, name, *children):
        self.name = name
        self.children = children

    def visit(self, someVisitor):
        someVisitor.arrivedAt(self)
        someVisitor.down()

        for c in self.children:
            c.visit(someVisitor)

        someVisitor.up()


class Visitor():
    def __init__(self):
        self.depth = 0

    def down(self):
        self.depth += 1

    def up(self):
        self.depth -+ 1

    def arrivedAt(self, aTreeNode):
        print self.depth, aTreeNode.name

c2 = TreeNode("c2", TreeNode("c22"), TreeNode("c222"))
c3 = TreeNode("c3", TreeNode("c33"), TreeNode("c333"))
c1 = TreeNode("c1", c2, c3)
someTree = TreeNode( "Top", c1)
dumpNodes = Visitor()
someTree.visit(dumpNodes)


print 'adding extra code here'
print 'adding 2nd extra code here'

print 'nikun is cool'

