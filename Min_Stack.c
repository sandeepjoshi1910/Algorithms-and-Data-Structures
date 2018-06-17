#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
};

typedef struct Node *node;

node createNode() {
    node temp;
    temp = (node)malloc(sizeof(struct Node));
    temp->next = NULL;
    return temp;
}

node appendNode(int value, node head) {
    node new_node = createNode();
    new_node->data = value;

    if (head == NULL) {
        return new_node;
    } else {
        node current = head;
        while (current->next != NULL) {
            current = current->next;
        }
        current->next = new_node;
    }
    return head;
}

node appendAtBegining(int value, node head) {
    node new_node = createNode();
    new_node->data = value;

    if (head == NULL) {
        return new_node;
    } else {
        new_node->next = head;
        head = new_node;
        return head;
    }
}

void printList(node head) {
    node current = head;
    while (current != NULL) {
        printf("%d\n",current->data);
        current = current->next;
    }
}


int main() {
    node head = appendNode(5,NULL);
    head = appendNode(10,head);
    head = appendNode(11,head);
    head = appendNode(12,head);
    head = appendNode(14,head);
    head = appendNode(16,head);
    head = appendNode(19,head);
    head = appendNode(22,head);
    head = appendNode(56,head);
    printList(head);
}