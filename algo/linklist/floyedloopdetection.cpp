
#include<iostream>


using namespace std;


// bool 
int floyedDetection(Node* head){
    Node* slow=head;
    Node* fast=head;

    if(head == NULL){
        return false;
    }else{

        while (slow != NULL && fast !=NULL)
        {
            if(slow == fast){
                return slow;
                // return true;
            }

            slow=slow->next;
            fast=fast->next;

            if(fast->next != NULL){
                fast=fast->next;
            }
        }
        
        // return false;
        return NULL;
    }

}


Node* getstartingNode(Node* head){

    Node* interection=floyedDetection(head);
    Node* slow=head;
    Node* fast=intersection;

    while (slow != intersection)
    {
        slow=slow->next;
        fast=intersection->next;
    }

    return slow;

}

Node* removeLoop(Node* head){

    Node* temp=getstartingNode(head);
    Node* prev=NULL;

    while (temp != temp->next)
    {
        prev=temp;
        temp=temp->next;
    }
    
    prev->next=NULL;
    
}
