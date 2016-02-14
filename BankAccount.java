public class BankAccount{
  
  private String name;
  private String address;
  private double balance;
  private int accountNum;
  
  public BankAccount(String n, String a, double b){
    name=n;
    address=a;
    balance=b;
    generateID();
  }
  
  public void roundToPenny(){ //rounds balance to the nearest penny
    balance = (int)(balance*100);
    balance = (double)(balance/100);
  }
  public void generateID(){ //generates a random 6 digit number
    accountNum =(int)(Math.random()*899999)+100000;       
  } 
  
  public void deposit(double d){ //adds deposit into balance
    balance += d;
  }
  
  public void withdraw(double w){ //withdraws money from balance
    balance -= w;
  }
  
  public void setName(String n){ //changes initial name of an account
    name = n;
  }
  
  public void setAddress(String a){ //chanegs intial address of an account
   address = a; 
  }
  public void interest(double i){ //adds interest to the balance
    balance += balance*i;
}
  public double getBalance(){ //gets the current balance
    return balance;
  } 
  
  public int getAccountNumber(){ //gets the account number
    return accountNum;
  }
  
  public String toString(){ //prints out the account information
    return "Name: " + name + ", Address: " + address + ", Account Number: " + accountNum + "\n Balance $" + balance ;
  }
    
}