// Online C++ compiler to run C++ program online
#include <iostream>
#include <map>
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
    };
};


void insertAtFirst(Node* &head,int d){
        
    Node* n=new Node(d);
    n->next=head;
    head=n;
    
}


void printAll(Node* &head){
    Node* temp=head;
    while(temp != NULL){
        cout<<temp->data<<endl;
        temp=temp->next;
    }
}

void insertAtEnd(Node* &tail,int d){
    Node* temp=new Node(d);

    Node* temp1=tail;
    while (temp1->next != NULL)
    {
        temp1=temp1->next;

    }

    temp1->next=temp;
    
    
}


void insertInMiddle(Node* &tail,int d,int middle){
    Node* temp=new Node(d); 
    Node* ele=tail;

    while (ele->next != NULL )
    {
        if(ele->data == middle){
            Node* curr=ele;
            temp->next=curr->next;
            curr->next=temp;
            break;
        }

        ele=ele->next;
    }
    

}

void deleteElement(Node* &head,int pos){
    int counter=0;
    Node* before;
    Node* now=head;

    while (now->next != NULL)
    {
        if(counter == 0 && counter == pos ){
            head=now->next;
            now->next=NULL;
            break;
        }else if(counter > 0 && counter == pos){
            Node* after=now->next;
            before->next=after;
            now->next=NULL;
            break;
        }


        counter+=1;
        before=now;
        now=now->next;
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

    // useing map ds make function return type bool
    // if(tail == NULL){
    //     return  false;
    // }else{
    //     map<Node*,bool> visited;

    //     while (temp != NULL)
    //     {
    //         if(visited[temp] == true ){
    //             return true;
    //         }

    //         visited[temp]=true;
    //         temp=temp->next;
    //     }
    //     return false;
    // }

}

Node* getMid(Node* head){
    // use floyed detection algo to find mid
    // when fast is null and in which place slow reach ,that is mid 

    Node* fast=head->next;
    Node* slow=head;

    // while(fast->next->next !=NULL){
    //     fast=fast->next->next;
    //     slow=slow->next;
    // }

    while (fast != NULL && fast->next != NULL)
    {
        fast=fast->next->next;
        slow=slow->next;
    }
    

    Node* mid=slow;

    return mid;

}

int main() {
    // dynamic initialization Node* means variable points to this class
    Node* node1=new Node(10);
    
    Node* head=node1;
    Node* tail=node1;

    
    insertAtFirst(head,20);
    insertAtFirst(head,30);

    insertAtEnd(tail,50);
    insertAtEnd(tail,60);
    insertAtEnd(tail,70);
    insertInMiddle(head,55,100);
    
    // getting mid
    Node* mid=getMid(head);
    cout<<"Getting Mid::"<< mid->data<<endl;
    
    // making list circular 
    // cout<<"head::"<<head->data<<endl;
    // cout<<"tail::"<<tail->data;

    // tail->next=head->next;
    // cout<<"Before delete"<<endl;
    // detectLoop(head);

    printAll(head);
    //  if endless looop running then it prove that list is circular
    
    // cout<<"After delete"<<endl;
    // deleteElement(head,3);
    // printAll(head);
    
    
    

}