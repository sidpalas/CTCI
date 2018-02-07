from Graph import Graph
from Graph import Node

class DependencyGraph(Graph):
        def __init__(self, projectList, dependencyList):
            self.nodes = []
            self.projectList = projectList[:]
            self.allowable = projectList[:]
            self.totalPackages = len(projectList)
            self.numPackagesInstalled = 0
            self.installOrder = []
            #add all projects as nodes
            for project in self.projectList:
                projectNode = Node(project, [], []) #unless the children and parents are explicitly set to empty, they will become linked across nodes...
                self.addNode(projectNode)
            #add the depdendency links
            for dependency in dependencyList:
                #add error handling for if a dependency is specified for project not in projectList
                idxParent = self.projectList.index(dependency[0])
                idxChild = self.projectList.index(dependency[1])
                if dependency[1] in self.allowable:
                    self.allowable.remove(dependency[1]) #the child now has a dependency and cant be installed immediately
                #why are the parents and children being applied to all nodes?!?
                self.nodes[idxParent].addChild(self.nodes[idxChild])
                self.nodes[idxChild].addParent(self.nodes[idxParent])

        def installProject(self, projectName):
            idx = self.projectList.index(projectName)
            if len(self.nodes[idx].parents) > 0:
                return False
            else:
                parent = self.nodes[idx]
                self.installOrder.append(parent.name)
                self.numPackagesInstalled += 1
                for child in self.nodes[idx].children:
                    child.parents.remove(parent)
                    if len(child.parents) == 0:
                        self.allowable.append(child.name)
                self.projectList.remove(projectName)
                self.nodes.remove(parent)
                return True

        def findInstallOrder(self):
            while len(self.allowable) > 0:
                nextPackage = self.allowable[0]
                installed = self.installProject(nextPackage)
                if installed == False:
                    return False
                else:
                    self.allowable.remove(nextPackage)

            if self.numPackagesInstalled == self.totalPackages:
                return self.installOrder
            else:
                return False

testProjectList = ['a','b','c','d','e','f']
testDependenciesList = [['a','d'],['f','b'],['b','d'],['f','a'],['d','c'],['a','b']]
testGraph = DependencyGraph(testProjectList, testDependenciesList)
print testGraph.findInstallOrder()

testDependenciesList2 = [['a','d'],['f','b'],['b','d'],['f','a'],['d','c'],['a','b'],['b','a']]
testGraph2 = DependencyGraph(testProjectList, testDependenciesList2)
print testGraph2.findInstallOrder()
