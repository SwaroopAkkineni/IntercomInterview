import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

class Interview {
  double dublinOfficeLatitude;
  double dublinOfficeLongitude;

  public Interview() {
    this.dublinOfficeLatitude = 53.339428;
    this.dublinOfficeLongitude = -6.257664;
  }

  public static void main(String[] args) {
    //check if a file has been sent
    System.out.println(args[0]);
    try (BufferedReader br = new BufferedReader(new FileReader(args[0]))) {
      String line = br.readLine();
      while (line != null) {
        System.out.println(line);
        line = br.readLine();
      }
    } catch (IOException e) {
			e.printStackTrace();
		}
  }

  private static Double calculateDistance(double latitude, double longitude) {
    //formula used: https://en.wikipedia.org/wiki/Great-circle_distance
    return 0.0;
  }
}
