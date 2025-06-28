class Box {
    double width;
    double height;
    double length;
    
    Box() {
        length = width = height = 0;
    }

    Box(double l, double w, double h) {
        length = l;
        width = w;
        height = h;
    }

    Box(double len) {
        length = width = height = len;
    }

    double volume() {
        return length * width * height;
    }

    double volume(double x) {
        return x * x * x;
    }
}

public class Overloading {
    public static void main(String[] args) {
        Box b1 = new Box();
        Box b2 = new Box(10);
        Box b3 = new Box(10, 20, 30);
        System.out.println("volume=" + b1.volume());
        System.out.println("volume=" + b2.volume());
        System.out.println("volume=" + b3.volume());
        System.out.println("volume=" + b3.volume(30));
    }
}
