#include<iostream>
#include<vector>
#include<list>
#include<limits>
#include<queue>

using namespace std;

string spath;
int spathwt = numeric_limits<int>::max();
string lpath;
int lpathwt = numeric_limits<int>::min();
string cpath;
int cpathwt = numeric_limits<int>::max();
string fpath;
int fpathwt = numeric_limits<int>::min();

priority_queue<pair<int, string>, vector<pair<int, string>>, greater<pair<int, string>>> pq;

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

void multisolver(vector<list<Edge>> graph, int start, int end, bool visited[], int criteria, int k, string psf, int wsf){
    if(start == end){
        if(wsf < spathwt){
            spathwt = wsf;
            spath = psf;
        }
        if(wsf > lpathwt){
            lpathwt = wsf;
            lpath = psf;
        }
        if(wsf > criteria && wsf < cpathwt){
            cpathwt = wsf;
            cpath = psf;
        }
        if(wsf < criteria && wsf > fpathwt){
            fpathwt = wsf;
            fpath = psf;
        }

        if(pq.size() < k){
            pq.push(make_pair(wsf, psf));
        } else{
            if(wsf > pq.top().first){
                pq.pop();
                pq.push(make_pair(wsf, psf));
            }
        }
        return;
    }

    visited[start] = true;
    for(Edge edge: graph[start]){
        if(visited[edge.neighbour] == false){
            multisolver(graph, edge.neighbour, end, visited, criteria, k, psf + to_string(edge.neighbour), wsf + edge.weight);
        }
    }
    visited[start] = false;
}

int main(){
    int V, E, start, end, criteria, k;
    cin>>V>>E;
    vector<list<Edge>> graph(V);

    for(int i=0; i<E; i++){
        int v1, v2, wt;
        cin>>v1>>v2>>wt;
        addEdge(graph, v1, v2, wt);
    }

    cin>>start>>end>>criteria>>k;

    bool visited[V];
    multisolver(graph, start, end, visited, criteria, k, to_string(start) + "", 0);

    cout<<"smallest path = "<<spath<<"@"<<spathwt<<endl;
    cout<<"largest path = "<<lpath<<"@"<<lpathwt<<endl;
    cout<<"just smaller path = "<<fpath<<"@"<<fpathwt<<endl;
    cout<<"just larger path = "<<cpath<<"@"<<cpathwt<<endl;

    cout<<k<<"th largest path = "<<pq.top().second<<"@"<<pq.top().first<<endl;
    
}