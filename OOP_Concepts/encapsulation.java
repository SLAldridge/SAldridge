// Encapsulation is a means of hiding the implementation details of a class from the user
// and I am not about to try to demonstrate encapsulation in Python
// The easiest way to demonstrate this is through getters and setters that operate on private methods/attributes

public Class Person {
    // These cannot be directly accessed outside of this class.
    private String firstName;
    private String lastName;
    
    // but these methods are public
    public void SetFirstname(String firstName) {
        firstName = firstName;
    }

    public void SetLastname(String lastName) {
        lastName = lastName;
    }

    public String GetName() {
        return firstName + ' ' + lastName;
    }

}
