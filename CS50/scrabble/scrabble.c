#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int check_score(string word, int length);
void compare_result(int score1, int score2);
string to_upper(string word, int length);

const int letterValue[26] = {1, 3, 3, 2,  1, 4, 2, 4, 1, 8, 5, 1, 3,
                             1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int main(int argc, string argv[])
{
    // var
    int score_player[2];
    string player[2];
    int length[2];

    // Ask for answer
    player[0] = get_string("Player 1: ");
    player[1] = get_string("Player 2: ");

    // check len of word
    length[0] = strlen(player[0]);
    length[1] = strlen(player[1]);
    // printf("L1:%i, L2 %i\n", length[0],length[1]);

    player[0] = to_upper(player[0], length[0]);
    player[1] = to_upper(player[1], length[1]);

    // check score
    score_player[0] = check_score(player[0], length[0]);
    score_player[1] = check_score(player[1], length[1]);

    // coompare score
    compare_result(score_player[0], score_player[1]);
    return 0;
}

int check_score(string word, int length)
{
    int score = 0;
    // check the score of each letter and add it to itself
    for (int i = 0; i < length; i++)
    {
        unsigned char cc = word[i];
        if (!isupper(cc))
        {
            if (cc != ' ' && cc != '*')
            {
                // Add 0 to the score
                // printf("invalid word: %s\n",word);
                score = score + 0;
            }
        }
        else
        {
            score = score + letterValue[cc - 'A'];
        }
    }
    return score;
}

string to_upper(string word, int length)
{
    // change each letter to its uppercase variant
    for (int i = 0; i < length; i++)
    {
        unsigned char cc = word[i];
        word[i] = toupper(cc);
    }
    // printf("%s\n", word);
    return word;
}

void compare_result(int score1, int score2)
{
    // compare the score of the players
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score1 < score2)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}
