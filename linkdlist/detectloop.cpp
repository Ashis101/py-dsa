#include<iostream>


using namespace std;

class Node{
    public:
        int data;
        Node* next;
        bool visited;

        Node(int d){
            this->data=d;
            this->next=NULL;
            this->visited=false;
        }
};


void addinList(Node* &tail,int value){

    // cout<<tail->data<<endl;
    if(tail == NULL){
        Node* temp=new Node(value);
        tail=temp;
        temp->next=temp;
    }else{
        Node* curr=tail;
        while (curr->next != NULL)
        {
            
            curr=curr->next;
        }
        
        Node* temp=new Node(value);
        temp->next=curr->next;
        curr->next=temp;

    }


}

void detectLoop(Node* &tail){

    Node* temp=tail;

    bool foundLoop=false;

    while (temp->next != NULL)
    {   
        if(temp->visited == true){
            foundLoop=true;
            break;
        }
        temp->visited=true;
        temp=temp->next;
    }
    
    cout<<"Found Loop ::"<<foundLoop<<endl;
}

void printAll(Node* &tail){
    Node* temp=tail;
    while(temp != NULL){
        cout<<temp->data<<endl;
        temp=temp->next;
    }
}

int main(){
    Node* tail=new Node(10);
    Node* node1=tail;
    addinList(node1,20);
    addinList(node1,30);
    addinList(node1,40);
    
    printAll(tail);

    detectLoop(tail);
}