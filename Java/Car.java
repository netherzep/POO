public class Car {
    
    Account driver;
    Integer id;
    String license;
    Integer passenger;

    public Car(String license, Account driver){

        this.license = license;
        this.driver  = driver; 

    }
    
    void printDataCar(){

        System.out.println("License: " + license + " Driver Name " + driver.name);
        

    }


}
