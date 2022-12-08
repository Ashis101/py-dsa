#include<iostream>
#include<bits/stdc++.h>

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
class Solution{
    private:
    Node* mid(Node *head){
        Node* fast=head->next;
        Node* slow=head;

        while (fast != NULL && fast->next != NULL)
        {
            fast=fast->next->next;
            slow=slow->next;
        }
        return slow;
    }
    Node* reverse(Node *head){
        Node* next=NULL;
        Node* curr=head;
        Node* prev=NULL;
        
        while(curr != NULL){
            next=curr->next;
            curr->next=prev;
            prev=curr;
            curr=next;
        }
        return prev;
    }
    public:
        //Function to check whether the list is palindrome.
        bool isPalindrome(Node *head)
        {
            if(head == NULL){
                return head;
            }
            
            //find mid element
            Node* mid_ele=mid(head);
            
            Node* temp=mid_ele->next;
            // pointing reversed element to middle element next 
            mid_ele->next=reverse(temp);
            // comparing both halves
            
            Node* first_halve=head;
            Node* second_halve=mid_ele->next;
            
            while(second_halve != NULL){
                
                if(first_halve->data != second_halve->data){
                    return false;
                    
                }
                
                first_halve=first_halve->next;
                second_halve=second_halve->next;
            }
            
            return true;
            
        
        }
};