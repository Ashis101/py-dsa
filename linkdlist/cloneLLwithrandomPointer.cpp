#include<iostream>
#include<bits/stdc++.h>

using namespace std;

class Node{
    public:
    int data;
    Node* next;
    Node* random;
    
    Node(int d){
        this->data=d;
        this->next=NULL;
        this->random=NULL;
    };
};

class Solution{
private:
    Node* cloneNode(Node* &head,Node* &tail,int d){
            
        Node* temp=new Node(d);
        
        if(head == NULL){
            head=temp;
            tail=temp;
        }else{
            tail->next=temp;
            tail=temp;
        }
    }
    public:
    Node *copyList(Node *head)
    {
        Node* cloneHead=NULL;
        Node* cloneTail=NULL;
        
        Node* temp=head;
        
        while(temp != NULL){
            cloneNode(cloneHead,cloneTail,temp->data);
            temp=temp->next;
        }
        
        // making map to create old to new ll pointer
        unordered_map<Node*,Node*> oldTonew;
        
        Node* cloneList=cloneHead;
        Node* originalList=head;
        
        while(cloneList != NULL && originalList != NULL){
            oldTonew[originalList]=cloneList;
            
            cloneList=cloneList->next;
            originalList=originalList->next;
        }
        
        // now pointing random pointer
        
        Node* cloneNode=cloneHead;
        Node* originalNode=head;
        
        while(originalNode != NULL){
            cloneNode->random=oldTonew[originalNode->random];
            cloneNode=cloneNode->next;
            originalNode=originalNode->next;
            
        }
        
        return cloneHead;
    }

};