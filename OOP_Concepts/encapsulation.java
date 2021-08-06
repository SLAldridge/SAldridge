// Encapsulation is a means of hiding the implementation details of a class from the user, 
// so we determine what properties/methods a user can access, and how.
// The easiest way to demonstrate this is through getters and setters.

// I'm going with Java here because encapsulation in Python is more of a suggestion, 
// whereas encapsulation in Java is like: https://www.youtube.com/watch?v=_NNYI8VbFyY

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
