# Selenium
[Ir](https://www.selenium.dev/)

Selenium is an umbrella project for a range of tools and libraries that enable and support the automation of web browsers.


![Selenium architecture](https://miro.medium.com/max/1400/1*hf65kALZSBnqFWmUlxUSxQ.png)

**Selenium WebDriver**

A collection of language specific bindings to drive a browser-the way it is meant to be drive.

**Selenium IDE**

Simple record-and-playback of interactions with the browser.

Generate language/binding specific  instructions.

**Selenium Grid**

Scale by distributing and running tests on several machines and manage multiple environments from a central point, making it easy to run the test agains a vast combination of browser/OS.

```java
package sigef;

import java.net.MalformedURLException;
import java.net.URL;
import java.time.Duration;
import java.util.*;
import org.openqa.selenium.Alert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;

// Generar  devengado anulado
// Reportar devengado
// This code is sort of auto-generated (but it need some tweeks)
public class Worker implements Runnable {

  private static final String MONTO = "1.00";

  @Override
  public void run() {
    WebDriver driver = new ChromeDriver();
    JavascriptExecutor js = (JavascriptExecutor) driver;
    
    driver.manage().window().maximize();

    // Login
    driver.get("http://localhost:8080/sigef/principal.jsp");
    driver.manage().window().setSize(new Dimension(1920, 1080));
    
    js.executeScript(
      "alert('Saludos')",
      ""
    );
   }
}
```

## Todo

- Look for a `terminal` tool to generate from the `Selenium IDE` scripts instructions in the differente langauge bindinds.

## Resources

[Cucumber](https://cucumber.io/)

[Watir](http://watir.com/)

No code ui  test automation

[Test Automation](https://ieeexplore.ieee.org/abstract/document/6401116)

[A Test Automation Framework Based on WEB](https://ieeexplore.ieee.org/abstract/document/6211171)

[Reflect.run - Blazing fast automated testing](https://reflect.run/)

[TestCafe](https://reflect.run/)

[Test Automation - Wiki](https://en.wikipedia.org/wiki/Test_automation)
