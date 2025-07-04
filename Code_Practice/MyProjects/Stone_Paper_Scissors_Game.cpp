#include<iostream>
#include<ctime>
int main()
{
    int user_in = 0;
    int comp_in = 0;
    int rounds;
    bool gameOver = false;
    int user_score = 0;
    int comp_score = 0;

    std::cout<<"*********Welcome to Stone, Paper, Scissors Game *********"<<std::endl;

    while (!gameOver)
    {
        srand(time(NULL));

        std::cout<<"Enter number of rounds to occur in one game : ";
        std::cin>>rounds;

        for (int i = 0; i < rounds; i++)
        {
            std::cout<<"Choose One of the Following : \n1. Stone \n2. Paper \n3.Scissors\n";
            std::cin>>user_in;

            comp_in = 1 + (rand() % 2);
            if (user_in == 1 && comp_in == 3)
            {
                std::cout<<"User :  Stone \n Computer : Scissors\n User Wins Round " << (i+1) << "\n";
                user_score += 1;
            }
            if (user_in == 3 && comp_in == 1)
            {
                std::cout<<"User :  Scissors \n Computer : Stone\n Computer Wins Round " << (i+1) << "\n";
                comp_score += 1;
            }
            if (user_in == 2 && comp_in == 1)
            {
                std::cout<<"User :  Paper \n Computer : Stone\n User Wins Round " << (i+1) << "\n";
                user_score += 1;
            }
            if (user_in == 1 && comp_in == 2)
            {
                std::cout<<"User :  Stone \n Computer : Paper\n Computer Wins Round " << (i+1) << "\n";
                comp_score += 1;
            }
            if (user_in == 3 && comp_in == 2)
            {
                std::cout<<"User :  Scissors \n Computer : Paper\n User Wins Round " << (i+1) << "\n";
                user_score += 1;
            }
            if (user_in == 2 && comp_in == 3)
            {
                std::cout<<"User :  Paper \n Computer : Scissors\n Computer Wins Round " << (i+1) << "\n";
                comp_score += 1;
            }
            if (user_in == 2 && comp_in == 2)
            {
                std::cout<<"User : Paper\nComputer : Paper\n Round No. " << (i+1) << " is a Draw! \n";
            }
            if (user_in == 3 && comp_in == 3)
            {
                std::cout<<"User : Scissors\nComputer : Scissors\n Round No. " << (i+1) << " is a Draw! \n";
            }
            if (user_in == 1 && comp_in == 1)
            {
                std::cout<<"User : Stone\nComputer : Stone\n Round No. " << (i+1) << " is a Draw! \n";
            }


        }
        std::cout<<"Final Scores are :  User : " << user_score << "   Computer : " << comp_score<<std::endl;
        if (user_score > comp_score)
        {
            std::cout<<"You Win!\n";
        }
        if (comp_score > user_score)
        {
            std::cout<<"Computer Wins!\n";
        }
        if (comp_score == user_score)
        {
            std::cout<<"It's a Draw!\n";
        }
        std::cout<<"******************************************************"<<std::endl;
        bool temp_state = true;
        std::string val;
        std::cout<<"Do you want to play again(y/n) : ";
        std::cin >> val;

        while (temp_state)
        {
            if (val == "n")
            {
                gameOver = true;
                temp_state = false;
            }
            if (val != "n" && val != "y")
            {
                std::cout<<"Invalid Input.Please Try Again!\n";
            }
            if (val == "y")
            {
                temp_state = false;
            }
        }
    }
    return 0;
}

    
