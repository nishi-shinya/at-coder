#include <iostream>
#include <memory>
#include <cstdio>

struct Node
{
	int key;
	Node *prev, *next;
};

Node *nil;

void init () {
	nil = (Node *)malloc(sizeof(Node));
	nil->next = nil;
	nil->prev = nil;
}

void insert (int key) {
	Node *x = (Node *)malloc(sizeof(Node));
	x->key = key;
	x->next = nil->next;
	nil->next->prev = x;
	nil->next = x;
	x->prev = nil;
}

Node* listSearch(int key) {
	Node *cur = nil->next;
	
}
