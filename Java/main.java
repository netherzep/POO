


class Main{

    public static void main(String[] args) {
        
        UberX uberx = new UberX("AMQ123",
        new Account("Diego Llanos", "1022403530"),
        "Chevrolet", "2020");
        uberx.SetPassenger(4);
        uberx.printDataCar();

        UberVan ubervan = new UberVan("HTY257",new Account("Diego Llanos", "1022403530"));
        ubervan.SetPassenger(6);
        ubervan.printDataCar();


        /*Car car2 = new Car("AFC879", new Account(2, "Karen Garcia", "1071304231", "k@gmail.com", "125448621858"));
        car2.passenger = 4;
        car2.printDataCar();*/
    }



}