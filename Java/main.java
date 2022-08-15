class Main{

    public static void main(String[] args) {
        
        Car car = new Car("AMQ123",new Account("Diego Llanos", "1022403530"));
        car.passenger = 4;
        car.printDataCar();

        Car car2 = new Car("AFC879", new Account("Karen Garcia", "1071304231"));
        car2.passenger = 4;
        car2.printDataCar();
    }



}