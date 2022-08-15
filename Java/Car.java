public class Car {
    
    private Account driver;
    private Integer id;
    private String license;
    private Integer passenger;

    public Car(String license, Account driver){
        this.license = license;
        this.driver  = driver;

    }
    
    void printDataCar(){

        if(passenger != null){

            System.out.println("License: " + license + " Driver Name " + driver.name + " Passengers: " + passenger);
        }else{

            System.out.println("Passenger should have a valid input");
        }

        
        

    }

    public Integer getPassenger(){

        return passenger;
    }

    public void SetPassenger(Integer passenger){
        if(passenger == 4){

            this.passenger = passenger;
        }else{

            System.out.println("Mínimo 4 pasajeros");
        }
        
    }

    public Account getDriver() {
        return driver;
    }

    public void setDriver(Account driver) {
        this.driver = driver;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getLicense() {
        return license;
    }

    public void setLicense(String license) {
        this.license = license;
    }


    


}
