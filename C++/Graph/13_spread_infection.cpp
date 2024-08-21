#include<iostream>
#include<vector>
#include<list>
#include<queue>

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

int main(){
    int V, E, src, t;
    cin>>V>>E;
    vector<list<Edge>> graph(V);

    for(int i=0; i<E; i++){
        int v1, v2;
        cin>>v1>>v2;
        addEdge(graph, v1, v2);
    }

    cin>>src>>t;

    queue<pair<int, int>> q;
    q.push(make_pair(src, 1));

    int visited[V];
    for(int i = 0; i < V; i++) visited[i] = 0;
    int count = 0;

    while(q.size() > 0){
        pair<int, int> rem = q.front();
        q.pop();

        if(visited[rem.first] > 0){
            continue;
        }
        visited[rem.first] = rem.second;
        if(rem.second > t) break;
        count++;

        for(Edge e: graph[rem.first]){
            if(visited[e.neighbour] == 0){
                q.push(make_pair(e.neighbour, rem.second + 1));
            }
        }
    }

    cout<<count<<endl;
}