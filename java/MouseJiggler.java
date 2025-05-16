import java.awt.Robot;
import java.util.Random;

public class MouseJiggler {
    public static void main(String[] argsv) throws Exception {
        Robot robot = new Robot();
        Random random = new Random();
        
        while(true) {
            robot.mouseMove(random.nextInt(100), random.nextInt(100));
            Thread.sleep(60000);
        }
    }
}
