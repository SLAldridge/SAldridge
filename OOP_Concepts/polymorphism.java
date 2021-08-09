// a snippet from one of my school projects with a method overload
// in this case, I overloaded the constructors for the Customer class, so that a Customer object could be created with or without params. 

    Customer() {
        
    }
    
    Customer(int custID, String custName, int addressID) {
        this.custID = custID;
        this.custName = custName;
        this.addressID = addressID;
    }
