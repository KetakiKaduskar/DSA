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
    int V, E, start;
    cin>>V>>E;
    vector<list<Edge>> graph(V);

    for(int i=0; i<E; i++){
        int v1, v2;
        cin>>v1>>v2;
        addEdge(graph, v1, v2);
    }

    cin>>start;

    queue<pair<int, string>> q;
    q.push(make_pair(start, to_string(start) + ""));
    bool visited[V] = {false};
    

    while(q.size() > 0){
        pair<int, string> rem = q.front();
        q.pop();
        
        if(visited[rem.first] == true) continue;
        visited[rem.first] = true;

        cout<<rem.first<<"@"<<rem.second<<endl;

        for(Edge e: graph[rem.first]){
            if(visited[e.neighbour] == false){
                q.push(make_pair(e.neighbour, rem.second + to_string(e.neighbour)));
            }
        }
    }
    
    
}