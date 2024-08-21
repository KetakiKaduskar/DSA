#include<iostream>
#include<vector>
#include<list>

using namespace std;

static vector<vector<int>> comps;

struct Edge{
    int source;
    int neighbour;

    Edge(int src, int nbr): source(src), neighbour(nbr){} 
};

void addEdge(vector<list<Edge>>& graph, int v1, int v2){
    graph[v1].push_back(Edge(v1, v2));
    graph[v2].push_back(Edge(v2, v1));
}

void drawTreeAndGenerateComps(vector<list<Edge>>& graph, int start, vector<int>& comp, bool visited[]){
    visited[start] = true;

    comp.push_back(start);

    for(Edge edge: graph[start]){
        if(visited[edge.neighbour] == false){
            drawTreeAndGenerateComps(graph, edge.neighbour, comp, visited);
        }
    }

}

int main(){
    int V, E, prod = 1, sum = 0;
    cin>>V>>E;
    vector<list<Edge>> graph(V);

    for(int i=0; i<E; i++){
        int v1, v2;
        cin>>v1>>v2;
        addEdge(graph, v1, v2);
    }

    bool visited[V] = {false};
    for(int vtx = 0; vtx < V; vtx++){
        if(visited[vtx] == false){
            vector<int> comp;
            drawTreeAndGenerateComps(graph, vtx, comp, visited);
            comps.push_back(comp);
        }
    }

    cout<<endl;

    for(int i = 0; i < comps.size(); i++){
        for(int j = i + 1; j < comps.size(); j++){
            prod = comps[i].size() * comps[j].size();
            sum += prod;
        }
    }

    cout<<sum;
    
}