#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <time.h>
#include "hacking.h"

#define DATAFILE "/var/chance.data" //File to store user data


//Custom user struct to store information about users
struct user{
  int uid;
  int credits;
  int highscore;
  char name[100];
  int (*current_game) ();
};

//Function prototypes
int get_player_data();
void register_new_player();
void update_player_data();
void show_highscore();
void jackpot();
void input_name()
void print_cards(char *, char *, int);
int take_wager(int, int);
void play_the_game();
int pick_a_number();
int dealer_no_match();
int find_the_ace();

//Global variables
struct user player; //Player struct

int main(){
  int choice, last_game;
  srand(time(0)); //seed the randomizer with current time

  if(get_player_data() == -1){
    register_new_player(); //if there is no data for current player register new
  }

  while(choice != 7){
    printf("-=[Game of Chance Menu ]=-\n");
    printf("1 - Play the pick a Number game\n");
    printf("2 - Play the No Match Dealer game\n");
    printf("3 - Play the Find the Ace game\n");
    printf("4 - View current high score\n");
    printf("5 - Change your user name\n");
    printf("6 - Reset your account at 100 credits\n");
    printf("7 - Quit\n");
    printf("[Name: %s]\n", player.name);
    printf("[You have %u credits] -> ", player.credits);
    scanf("%d", &choice);
  }

  if((choice < 1) || (choice > 7)){
    printf("\n[!!] The %d is an invalid selection.\n\n", choice);
  }
  else if(choice < 4){
    if(choice != last_game){
      if(choice == 1)
        player.current_game = pick_a_number;
      else if(choice == 2)
        player.current_game = dealer_no_match;
      else
        player.current_game = find_the_ace;
      last_game = choice; // and set last_game
    }
    play_the_game();
  }
  else if(choice == 4)
    show_highscore();
  else if(choice == 5)
    printf("\nChange user name\n");
    printf("Enter your new name: ");
    input_name():
    printf("Your name has been change.\n\n")

}
//end of file
