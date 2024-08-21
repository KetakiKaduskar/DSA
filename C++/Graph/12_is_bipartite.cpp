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

bool checkCompForBipartiteness(vector<list<Edge>>& graph, int src, int visited[]){
    queue<pair<int, int>> q;
    q.push(make_pair(src, 0));

    while(q.size() > 0){
        pair<int, int> rem = q.front();
        q.pop();

        if(visited[rem.first] != -1){
            if(rem.second != visited[rem.first]) return false;
        } else{
            visited[rem.first] = rem.second;
        }

        for(Edge e: graph[rem.first]){
            if(visited[e.neighbour] == -1){
                q.push(make_pair(e.neighbour, rem.second + 1));
            }
        }
    }

    return true;
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

    int visited[V];
    for(int i = 0; i < V; i++) visited[i] = -1;
    for(int vtx = 0; vtx < V; vtx++){
        if(visited[vtx] == -1){
            bool isCompBipartite = checkCompForBipartiteness(graph, vtx, visited);
            if (!isCompBipartite){
                cout<<"false"<<endl;
                return 0;
            }
        }
    }

    cout<<"true"<<endl;
}