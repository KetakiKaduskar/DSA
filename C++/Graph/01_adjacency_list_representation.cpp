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

void addEdge(vector<list<Edge>>& adjList, int v1, int v2, int wt){
    adjList[v1].push_back(Edge(v1, v2, wt));
    adjList[v2].push_back(Edge(v2, v1, wt));
}

void printGraph(vector<list<Edge>>& adjList){
    int v = adjList.size();
    for(int i=0; i<v; i++){
        for(Edge edge: adjList[i]){
            cout<<edge.source<<": "<<edge.neighbour<<" "<<edge.weight<<endl;
        }
    }
}

int main(){
    int V, E;
    cin>>V>>E;
    vector<list<Edge>> adjList(V);

    for(int i=0; i<E; i++){
        int v1, v2, wt;
        cin>>v1>>v2>>wt;
        addEdge(adjList, v1, v2, wt);
    }
    
    printGraph(adjList);
}