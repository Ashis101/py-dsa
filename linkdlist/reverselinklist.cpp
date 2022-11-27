#include<iostream>

class Node{
    public:
    int data;
    Node* next;
    
    Node(int d){
        this->data=d;
        this->next=NULL;
    };
};

void reverse(Node* &head){
    if(head == NULL || head->next == NULL){
            return head;
        }
        
        Node* prev=NULL;
        Node* curr=head;
        
        while(curr != NULL){
            Node* forward=curr->next;
            curr->next=prev;
            prev=curr;
            curr=forward;
            
        }
        return prev;
}

int main(){

    Node* head=new Node(10);

    reverse(head);

}