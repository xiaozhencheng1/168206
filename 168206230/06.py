graph = {}
graph["yp"] = {}
graph["yp"]["hjcp"] = 5
graph["yp"]["hb"] = 0
graph["cp"] = {}
graph["cp"]["jt"] = 15
graph["cp"]["jzg"] = 20
graph["hb"] = {}
graph["hb"]["jt"] = 30
graph["hb"]["jzg"] = 35
graph["jzg"] = {}
graph["jzg"]["gq"] = 10
graph["jt"] = {}
graph["jt"]["gq"] = 20
graph["gq"] = {}

infinity = float("inf")#散列表是开销
costs = {}
costs["cp"] = 5
costs["hb"] = 0
costs["jt"] = infinity
costs["jzg"] = infinity
costs["gq"] = infinity

parents = {}   #散列表是父子节点
parents["cp"] = "yp"
parents["hb"] = "yp"
parents["jzg"] = None
parents["jt"] = None
parents["gq"] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def find_shortest_path():
    node='gq'
    shortest_path=["gq"]
    while node!="yp":
          node=parents[node]
          shortest_path.append(node)
    shortest_path.reverse()
    print('\n最终路径：')
    print(shortest_path)
    
if __name__ == '__main__':
    node=find_lowest_cost_node(costs)   
    while node is not None:
        cost=costs[node]
        neighbors=graph[node]
        for n in neighbors.keys():
            new_cost=cost+neighbors[n]
            if costs[n]>new_cost:
                costs[n]=new_cost
                parents[n]=node
        processed.append(node) 
        node=find_lowest_cost_node(costs)
    shortest_path=find_shortest_path()
    print(shortest_path)
print('\n节点:开销')
print(costs)
print('\n节点：父节点')
print(parents)



    
