import java.io.*;
import static java.lang.System.*;
import java.util.Scanner;
import java.lang.Math;
import java.util.*;

class BankAccountTester{

public static void main (String str[]) throws IOException {

         
            Scanner scan = new Scanner(System.in);
              
            System.out.println("Welcome to the bank creator!");
            ArrayList <BankAccount> accounts = new ArrayList <BankAccount>(); //arraylist which holds the bankaccount objects
             
             int i=0; //variable that counts the number of accounts
             while(true){ //loop to create the accounts
               i++;
               System.out.print("New Account: Account " + i + " \nEnter name (q to quit): ");
               String n = scan.nextLine();
               if(n.equals("q")) break;
               System.out.print("\nEnter address: ");
               String a = scan.nextLine();
               System.out.print("\nEnter opening balance: ");
               double b = scan.nextDouble();
               scan.nextLine();
               accounts.add(new BankAccount(n,a,b));
               accounts.get(i-1).roundToPenny();
               System.out.println("Here is your account information " + accounts.get(i-1)); //returns intial information of each account
            }
             
             while(true){ //loops that changes the information of the account
               int position = -1;
               System.out.print("Would you like to make any changes to your account? (Enter yes or no)");
               String responseToContinue = scan.nextLine();
               if(responseToContinue.equals("no")) break;
                 System.out.print("\n Please enter your account number (this is the number given when your account was created) ");
                 int enteredAccount = scan.nextInt();
                 scan.nextLine();
                 int currentAccountNum = 0; //declaration of variable
                 while(true){ //loop that checks if the bankaccount number exists and then finds the correct bankaccount object
                 for(position = 0; position<accounts.size(); position++){ //loop that checks all the existing account numbers
                   currentAccountNum = accounts.get(position).getAccountNumber();
                   if(currentAccountNum==enteredAccount) break;
                }
                 if(currentAccountNum==enteredAccount) break; //breaks out of the loop if the position represents the position of the correct bankaccount object
                 else
                 System.out.println("The account number you entered does not belong to any accounts in existance, please try again"); 
                 enteredAccount = scan.nextInt();
                 scan.nextLine();
              }
               System.out.print("\nEnter A to change your address, N to change your name, W to withdraw, D to deposit and I to add interest");
               String responseToSelection = scan.nextLine();
               if(responseToSelection.equals("A")){ //statement to change the address
                 System.out.print("\nWhat would you like to change your address to? :");
                 String changeAddress = scan.nextLine();
                 accounts.get(position).setAddress(changeAddress);
               }
               if(responseToSelection.equals("N")){ //statement to change the name
                 System.out.print("\nWhat would you like to change your name to? :");
                 String changeName = scan.nextLine();
                 accounts.get(position).setName(changeName);
               }
               if(responseToSelection.equals("W")){ //statement to withdraw money from the account
                 System.out.print("\nHow much would you like to withdraw :");
                 double withdrawAmount = scan.nextDouble();
                 scan.nextLine();
                 double currentBalance = accounts.get(position).getBalance(); //gets the current balance of a specific account
                 while(withdrawAmount > currentBalance){ //loop to ensure withdrawl amount is not greater than balance
                   System.out.print("\nYou do not have enough in your account to make that withdrawl, please under a withdrawl amount less the your balance " + currentBalance);
                   withdrawAmount = scan.nextDouble();
                   scan.nextLine();
                 }
                 accounts.get(position).withdraw(withdrawAmount);
                 accounts.get(position).roundToPenny();
               }
               if(responseToSelection.equals("D")){ //statement to deposit money into an account
                 System.out.print("\nHow much would you like to deposit into your account? ");
                 double depositAmount = scan.nextDouble();
                 scan.nextLine();
                 accounts.get(position).deposit(depositAmount);
                 accounts.get(position).roundToPenny();
               }
               if(responseToSelection.equals("I")){ //statement to add interest to an account
                 System.out.print("\nPlease enter the amount of interest you want (enter a value betweeen .01 and .2) ");
                 double interestAmount = scan.nextDouble();
                 scan.nextLine();
                 accounts.get(position).interest(interestAmount);
                 accounts.get(position).roundToPenny();
               }
               }
           
       
            i=0; //resets counting variable
            for(BankAccount ba: accounts){ //loop to print out accounts
            i++;
            System.out.println("Account: " + i);
            System.out.println(ba);
            }
              
             
}
}