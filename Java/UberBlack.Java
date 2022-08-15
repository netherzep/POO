import java.util.Arraylist;
import java.util.Map;

class UberBlack extends Car{

    Map<String, Map<String, Integer>> typeCarAccepted;
    ArrayList<String> SeatsMaterial;

    public UberBlack(String license, Account driver,
    Map<String, Map<String, Integer>> typeCarAccepted,
    ArrayList<String> SeatsMaterial){

        super(license, driver);
        this.typeCarAccepted = typeCarAccepted;
        this.SeatsMaterial = SeatsMaterial;
        

    }


}