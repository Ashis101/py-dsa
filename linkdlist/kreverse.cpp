#include<iostream>


using namespace std;

class Node{
    public:
    int data;
    Node* next;
    
    Node(int d){
        this->data=d;
        this->next=NULL;
    };
};

void kreverse(Node* head,int k){

    // edge case 
    if(head == NULL){
        return ;
    }

    Node* prev=NULL;
    Node* curr=head;
    Node* forward=NULL;
    int count=0;

    // swapping element
    while (curr != NULL && count < k)
    {
        forward=curr->next;
        curr->next=prev;
        prev=curr;
        curr=forward;
        count++;
    }
    
    if(forward != NULL){
        head->next=kreverse(forward,k);
    }

    // return head of reverse list 

    return prev;

}