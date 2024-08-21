#include<iostream>
#include<vector>
#include<list>

using namespace std;

struct Edge{
    int source;
    int neighbour;
    int weight;

    Edge(int src, int nbr, int wt): source(src), neighbour(nbr), weight(wt){} 
};

void addEdge(vector<list<Edge>>& graph, int v1, int v2, int wt){
    graph[v1].push_back(Edge(v1, v2, wt));
    graph[v2].push_back(Edge(v2, v1, wt));
}

void printAllPaths(vector<list<Edge>> graph, int start, int end, bool visited[], string psf){
    if(start == end){
        cout<<psf<<endl;
        return;
    }

    visited[start] = true;
    for(Edge edge: graph[start]){
        if(visited[edge.neighbour] == false){
            printAllPaths(graph, edge.neighbour, end, visited, psf + to_string(edge.neighbour));
        }
    }
    visited[start] = false;
}

int main(){
    int V, E, start, end;
    cin>>V>>E;
    vector<list<Edge>> graph(V);

    for(int i=0; i<E; i++){
        int v1, v2, wt;
        cin>>v1>>v2>>wt;
        addEdge(graph, v1, v2, wt);
    }

    cin>>start>>end;

    bool visited[V];
    printAllPaths(graph, start, end, visited, to_string(start) + "");
    
}