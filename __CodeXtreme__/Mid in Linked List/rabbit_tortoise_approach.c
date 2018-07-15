//Rabbit Tortoise Approach - for finding Middle element of a Linked List

/*
It include taking two pointers
    struct node*head
    struct node*fast_ptr
    struct node*slow_ptr
when the fast_ptr will traverse the whole list by jumping two space an iteration,
the slow_ptr will traverse till the half of the list
*/


#include<stdio.h>
#include<stdlib.h>

typedef struct node
{
    int data;
    struct node* next;
}node;

node* create(int n);
node* display(node* head);

int main()
{
    int head;
    head = create(5);   //list of length 5
    printf("\nThe linked list is: ");
    display(head);
    mid(head);

return 0;
}

// Function using rabbit tortoise approach for finding mid element of list
void mid(node* head)
{
    node*fast_ptr = head;
    node*slow_ptr = head;

    while(1){

        if(fast_ptr->next == NULL)
            break;
        fast_ptr = fast_ptr->next;
        fast_ptr = fast_ptr->next;
        slow_ptr = slow_ptr->next;
    }

    printf("\nMid element of list = ");
    printf("%d\n", slow_ptr->data);

}

// Function to create the Linked List
node* create(int n)
{
    int i=0;
        node* p = NULL;
        node* head = NULL;
        node* temp = NULL;

        for(i=0; i<n; i++)
        {
            temp = (node*)malloc(sizeof(node));
            temp->data = i+1;
            temp->next = NULL;
            if(head == NULL)
                head = temp;
            else
            {
                p = head;
                while(p->next != NULL)
                    p = p->next;
                p->next = temp;
            }

        }
    return head;
}

// Function to display the Linked List
node* display(node* head)
        {
            node* p = NULL;
            if(head == NULL)
                printf("\nList is empty");
            else
            {
                p = head;
                while(p != NULL)
                {
                    printf("%d->",p->data);
                    p = p->next;
                }
            }
            return 0;
        }
