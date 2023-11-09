#include<iostream>
#include<vector>
#include<list>
#include <unordered_set>

using namespace std;

struct Edge{
    int source;
    int neighbour;

    Edge(int src, int nbr): source(src), neighbour(nbr){} 
};

void addEdge(vector<list<Edge>>& graph, int v1, int v2){
    graph[v1].push_back(Edge(v1, v2));
    graph[v2].push_back(Edge(v2, v1));
}

void hamiltonian(vector<list<Edge>>& graph, int start, unordered_set<int>& visited, string psf, int ostart){
    if(visited.size() == graph.size() - 1){
        cout<<psf;

        bool closingEdgeFound = false;
        for(Edge e: graph[start]){
            if(e.neighbour == ostart) closingEdgeFound = true;
        }

        if(closingEdgeFound == false) cout<<"."<<endl;
        else cout<<"*"<<endl;
    }

    visited.insert(start);
    for(Edge edge: graph[start]){
        if(visited.find(edge.neighbour) == visited.end()){
            hamiltonian(graph, edge.neighbour, visited, psf + to_string(edge.neighbour), ostart);
        }
    }
    visited.erase(start);
}

int main(){
    int V, E, start;
    cin>>V>>E;
    vector<list<Edge>> graph(V);

    for(int i=0; i<E; i++){
        int v1, v2;
        cin>>v1>>v2;
        addEdge(graph, v1, v2);
    }

    cin>>start;

    unordered_set<int> visited;
    hamiltonian(graph, start, visited, to_string(start) + "", start);
    
}