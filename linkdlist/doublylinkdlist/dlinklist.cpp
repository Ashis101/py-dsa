#include<iostream>

using namespace std;

class Node{

    public:
        int data;
        Node* prev;
        Node* next;

        Node(int d){
            this->data=d;
            this->prev=NULL;
            this->next=NULL;
        }
};

void insertAtbegin(Node* &head,int digit){
    Node* temp=new Node(digit);

    if(head == NULL){
        Node* temp=new Node(digit);
        head=temp;
    }

    temp->next=head;
    head->prev=temp;
    head=temp;


}

void print(Node* &head){
    Node* curr=head;
    while (curr->next != NULL)
    {
        cout<< curr->data<<endl;
        curr=curr->next;
    }

    
}

int main(){
    Node* head=NULL;
    insertAtbegin(head,1);
    insertAtbegin(head,2);
    insertAtbegin(head,3);
    insertAtbegin(head,4);

    print(head);
}