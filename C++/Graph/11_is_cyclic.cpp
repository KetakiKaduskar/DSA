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

bool isCyclic(vector<list<Edge>>& graph, int src, bool visited[]){
    queue<pair<int, string>> q;
    q.push(make_pair(src, to_string(src) + ""));

    while(q.size() > 0){
        pair<int, string> rem = q.front();
        q.pop();

        if(visited[rem.first] == true) return true;
        visited[rem.first] = true;

        for(Edge e: graph[rem.first]){
            if(visited[e.neighbour] == false){
                q.push(make_pair(e.neighbour, rem.second + to_string(e.neighbour)));
            }
        }
    }

    return false;
}

int main(){
    int V, E;
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
            bool cycle = isCyclic(graph, vtx, visited);
            if (cycle){
                cout<<"true"<<endl;
                return 0;
            }
        }
    }

    cout<<"false"<<endl;
}