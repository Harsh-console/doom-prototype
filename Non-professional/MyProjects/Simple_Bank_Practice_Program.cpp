#include<iostream>
int main()
{
    bool state;
    state = true;
    double bank_balance;
    bank_balance = 1000.00;
    while (state)
    {
        std::cout <<"Select on of the options. \n 1. Withdraw Money. \n 2. Deposit Money. \n 3. View Account Balance. \n 4. Exit!\n";
        char user_input;
        std::cin>>user_input;
        switch (user_input)
        {
        case '1': {
            double temp_num;
            std::cout<<"How much money would you like to withdraw? : ";
            std::cin>>temp_num;
            (bank_balance>=temp_num)? (std::cout<<temp_num << " have been withdrawn from your account. Thank you!\n"):(std::cout<<"You do not have sufficient Balance. Please Try Again Later. Thank You!\n");
            if (bank_balance>=temp_num)
            {
                bank_balance -= temp_num;
            }
            break;
        }
        case '2': {
            double temp_num;
            std::cout<<"How much money would you like to deposit? : ";
            std::cin>>temp_num;
            bank_balance += temp_num;
            std::cout<<temp_num << " have been deposited to your Bank Account. Thank you!\n";
            break;
        }
        case '3':{
            std::cout<<"Your Account Balance is " << bank_balance <<" .\n";
            break;
        }
        case '4': {
            std::cout<<"Thank You for Visiting! \n";
            state = false;
        }
        default:{
            break;
        }
        }
    }
}