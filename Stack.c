#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
};

typedef struct Node *node;

struct Node *head;

void initializeHead() {
    head = (node)malloc(sizeof(struct Node));
    head->next = NULL;
}

void push(int value) {
    node new_node = (node)malloc(sizeof(struct Node));
    new_node->data = value;

    if (head != NULL) {
        new_node->next = head;
    }
    head = new_node;
}

int pop() {
    int value = head->data;
    head = head->next;
    return value;
}

int peek() {
    if (head != NULL) {
        return head->data;
    } else {
        return -1;
    }
}

void printStack() {
    if (head == NULL) {
        return;
    }

    node current = head;
    while (current->next != NULL) {
        printf("%d\n",current->data);
        current = current->next;
    }
}

int main() {
    initializeHead();
    push(5);
    push(10);
    push(15);
    push(20);
    push(25);
    push(30);
    push(35);
    printf("Stack\n");
    printStack();
    pop();
    pop();
    printf("Stack\n");
    printStack();
    return 0;
}

