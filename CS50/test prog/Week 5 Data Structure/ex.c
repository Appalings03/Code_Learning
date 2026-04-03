const int cap =50;

// Queue -> FIFO ; first in first out
typedef struct
{
    person people[cap]; // max amount
    int size; // current amount
}queue;

//Stacks -> LIFO ; last in first out
typedef struct
{
    person people[cap]; // max amount
    int size; // current amount
}stacks;

/*
Difference is how the queue/stacks is filled
*/
