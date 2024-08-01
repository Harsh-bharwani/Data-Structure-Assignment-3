#include<bits/stdc++.h>
using namespace std;
class LRUcache{
    public:
        class Node{
            public:
                int key;
                int val;
                Node* next=nullptr;
                Node* prev=nullptr;
            Node(int _key, int _val){
                key=_key;
                val=_val;
            }
        };

        Node* head= new Node(-1, -1);
        Node* tail= new Node(-1, -1);
        int cap;
        unordered_map<int, Node*>mp;
        LRUcache(int capacity){
            cap=capacity;
            head->next = tail;
            tail->prev = head;
        } 
        void addNode(Node* newnode){
            Node* temp=head->next;
            head->next=newnode;
            newnode->next=temp;
            newnode->prev=temp;
            temp->prev=newnode;
        }
        void deleteNode(Node* restored_node){
            restored_node->next->prev=restored_node->prev;
            restored_node->prev->next=restored_node->next;
            delete restored_node;
        }
        int get(int key){
            if(mp.find(key)!=mp.end()){
                Node* restored_node=mp[key];
                int res= restored_node->val;
                mp.erase(key);
                deleteNode(restored_node);
                addNode(restored_node);
                mp[key]=head->next;
                return res;
            }
            else{
                return -1;
            }
        }
        void put(int key, int value){
            if(mp.find(key)!=mp.end()){
                Node* existingNode=mp[key];
                mp.erase(key);
                deleteNode(existingNode);
            }
            if(mp.size()==cap){
                mp.erase(tail->prev->key);
                deleteNode(tail->prev);
            }
            addNode(new Node(key, value));
            mp[key]=head->next;
        }
};
int main(){
    LRUcache l(2);
    l.put(1,1);
    l.put(2,3);
    l.put(4,5);
    cout<<l.get(1);
}