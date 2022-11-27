// Online C++ compiler to run C++ program online
#include <iostream>

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


int main() {
    // dynamic initialization Node* means variable points to this class
    Node* node1=new Node(10);
    
    Node* head=node1;
    Node* tail=node1;

    
    insertAtFirst(head,20);
    insertAtFirst(head,30);

    insertAtEnd(head,50);
    insertAtEnd(head,60);
    insertAtEnd(head,70);
    insertInMiddle(head,55,100);
    
    cout<<"Before delete"<<endl;
    printAll(head);
    cout<<"After delete"<<endl;
    deleteElement(head,3);
    printAll(head);
    
    
    

}