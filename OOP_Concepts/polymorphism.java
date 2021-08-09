// This is a snippet from one of my school projects. The override is an example of polymorphism. 
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;


public class Appointment {

    private int apptID;
    private int custID;
    private int usrID = UserHomeController.getSession().getLoggedInUserID();
    private String title;
    private String description;
    private String location;
    private String type;
    private LocalDate date;
    private LocalTime start;
    private LocalTime end;
    private String userName;
    
    //getters & setters
    public int getApptID() {
        return apptID;
    }

    public void setApptID(int apptID) {
        this.apptID = apptID;
    }

    public int getCustID() {
        return custID;
    }

    public void setCustID(int custID) {
        this.custID = custID;
    }

    public int getUsrID() {
        return usrID;
    }

    public void setUsrID(int usrID) {
        this.usrID = usrID;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }

    public LocalTime getStart() {
        return start;
    }

    public void setStart(LocalTime start) {
        this.start = start;
    }

    public LocalTime getEnd() {
        return end;
    }

    public void setEnd(LocalTime end) {
        this.end = end;
    }

    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }
    
    // This is an example of polymorphism. I'm overriding Object.toString()
    @Override
    public String toString() {
        return title;
    }
        
    //constructors
    public Appointment() {

    }

    public Appointment(int customerID, int userID, String title, String description, String location, String type, LocalDateTime startTime, LocalDateTime endTime) {

    }

}
