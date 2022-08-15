import java.util.ArrayList;
import java.util.Map;

class UberVan extends Car{

    Map<String, Map<String, Integer>> typeCarAccepted;
    ArrayList<String> SeatsMaterial;
    private Integer passenger;

    public UberVan(String license, Account driver,
    Map<String, Map<String, Integer>> typeCarAccepted,
    ArrayList<String> SeatsMaterial){

        super(license, driver);
        this.typeCarAccepted = typeCarAccepted;
        this.SeatsMaterial = SeatsMaterial;
        

    }

    public UberVan(String license, Account driver){

        super(license, driver);        

    }

    @Override //polimorfismo
    public void SetPassenger(Integer passenger) {
        
        if(passenger == 6){

            this.passenger = passenger;
        }else{

            System.out.println("Mínimo 6 pasajeros");
        }
    }

   
}
