Entrance:
We will consider the red team approach to protecting against Cross-Site Script Inclusion (XSSI) attacks. XSSI attacks are attacks to steal users' information or infect the web application by exploiting the security weaknesses of the target web application. This tutorial will provide red team members with detailed steps to improve their protection from XSSI attacks.

## Chapter 1: Overview of XSSI Attacks

XSSI attacks are a type of Cross-Site Script Inclusion attacks. These attacks allow attackers to run malicious code in users' browsers by exploiting the security weaknesses of the target web application.

The security of web applications is of great importance today. By having malicious scripts run on users' browsers, attackers can gain access to sensitive data or capture users' login information. One such attack is Cross-Site Script Inclusion (XSSI) attacks.
XSSI attacks are a type of attack that causes a security vulnerability in a web application and allows the attacker to insert an external script and run it in users' browsers. This attack can happen when the web application's security controls are missing or weak.
The potential consequences of XSSI attacks can be quite serious. Attackers can steal users' session information, run malicious scripts, and capture users' sensitive data. Therefore, protecting web applications against XSSI attacks is of paramount importance.
Methods of protection against XSSI attacks include validation and filtering of input parameters, up-to-date and complete security controls, correct encoding of user inputs, and use of firewalls. These measures keep users safe by preventing attackers from adding malicious scripts to the web application from outside.

- The potential effects of XSSI attacks can be quite serious. Here are some examples:
- Theft of User Information: XSSI attacks allow attackers to obtain login information of users. The attacker inserts a malicious script that runs it in the user's browser, thereby stealing the user's session information. This information could allow the attacker to gain unauthorized access and hijack the user's account.
- Execution of Malicious Scripts: XSSI attacks allow attackers to enable malicious scripts to be run in the web application. These scripts can perform malicious operations on the user's browser, steal the user's information or take control of the user's browser. This puts users' security and privacy at risk.
- Web Application Integrity Compromised: XSSI attacks can cause attackers to compromise the web application's integrity. The attacker can disrupt the functionality of the web application, damage the database, or completely disable the service through scripts he adds from the outside. This affects the usability of the web application and may cause serious material and reputational damage.
- These potential impacts highlight the severity and importance of XSSI attacks. Precautions such as protection of web applications against XSSI attacks, up-to-date and complete security controls, validation and filtering of input parameters should be taken. In addition, regular security testing and monitoring processes should be implemented.

## Chapter 2: Configuration Weaknesses of XSSI Attacks

Not configuring CORS policies correctly paves the way for XSSI attacks because these attacks exploit CORS policies that allow the browser to access resources outside of the same root domain. These policies limit the browser from sending or receiving data from one website to another. However, a misconfigured CORS policy could allow the browser to send or receive data to a website controlled by a malicious attacker.
Common configuration errors in target web applications can include:
- Misconfigured CORS headers: If the web application misconfigures the CORS headers, browsers can misinterpret these headers and allow a malicious attacker to access the web application. For example, the Access-Control-Allow-Origin header determines which resources the browser can access. A misconfigured header can allow the browser to access any resource.
- Misconfigured CSRF (Cross-Site Request Forgery) protection: CSRF protection ensures that the browser only accepts requests from a specific source. However, a misconfigured CSRF protection could allow the browser to accept requests from a malicious attacker. In this case, the attacker could have the browser send malicious requests under the identity of a trusted user.
The consequences of these misconfigurations can be:
- Compromise of user data: XSSI attacks can allow a browser to send or receive user data to a website controlled by a malicious attacker. This can lead to the attacker's capture of the user's confidential information (eg login information, personal information).
- Phishing attacks: A misconfigured web application allows an attacker to stage phishing attacks to steal sensitive information from users. An attacker could create a fake website that redirects users to a trusted website and have users enter their credentials on that fake site.

## Chapter 3: XSSI Attack Types

1. ### Regular XSSI
A security vulnerability that allows client-side execution of a web application's server-side JavaScript file from another website or resource. This vulnerability can be directly invoked on the client side of the server-side JavaScript file, and the sensitive information it contains can be compromised by malicious people.

Here's an example of how Regular XSSI works:

1. The target web application defines a variable containing sensitive information in a server-side JavaScript file. For example, an array named confidential_keys.
2. This JavaScript file is located in a client-side accessible location and can be called directly by any user.
3. The attacker creates a malicious website or content.
4. The attacker inserts code into the malicious content that calls the target web application's JavaScript file. For example:
```javascript
<script src="https://www.vulnerable-domain.tld/script.js"></script>
<script> alert(JSON.stringify(confidential_keys[0])); </script>
```

5. The user visits the malicious website of the attacker.
6. The malicious website calls the target web application's JavaScript file.
7. The JavaScript file is executed on the client side and displays a warning message containing the confidential_keys[0] variable.
8. The user sees the warning message and is exposed to sensitive information obtained by the attacker's malicious website.

In this scenario, the attacker invokes the target web application's JavaScript file through a malicious website, giving the user access to sensitive information. This type of attack can be carried out in web applications with vulnerabilities and can compromise users' information. Therefore, it is important to take precautions for the security of web applications.
## Dynamic JavaScript-based XSSI and Spoofing

Dynamic JavaScript-based XSSI is a vulnerability that results from the failure to securely load dynamic JavaScript scripts used in a web application. This vulnerability allows attackers to access sensitive information by bypassing the web application's security checks. In this tutorial, we will examine Dynamic JavaScript-based XSSI vulnerability and spoofing scenarios.

**one. part: Spoofing with JSONP**

JSONP (JSON with Padding) is a widely used technique in web applications. However, it can lead to XSSI vulnerability when used without security checks. Here is an example of this scenario:

``javascript
<script>
  var confidentialData = {
    "status": "STATUS",
    "body": {
      "demographics": {
        "email": "example@example.com",
      }
    }
  };
  
  var angular = function () { return 1; };
  angular.callbacks = function () { return 1; };
  angular.callbacks._7 = function (leaked) {
    alert(JSON.stringify(leaked));
  };
</script>
<script src="https://site.tld/p?jsonp=angular.callbacks._7" type="text/javascript"></script>
```

In this example, the `angular.callbacks._7` callback function in the JSONP response takes the `confidentialData` object containing the hidden information and displays it as a warning message. In real scenario, `confidentialData` object will be populated with real user information.

**Scenario 2: Using Custom Function with JSONP**

In this scenario, information spoofing is accomplished by processing the JSONP response through a custom function. Here is the example:

``javascript
<script>
  function leak(leaked) {
    alert(JSON.stringify(leaked));
  }
</script>
<script src="https://site.tld/p?jsonp=leak" type="text/javascript"></script>
```

In this code, a function named `leak` is defined and the JSONP response triggers this function, passing an object containing hidden information. In the real scenario, the 'leak' function will handle it appropriately by seizing confidential information.

**Scenario 3: Information Leaking with Prototype Manipulation**

In this scenario, spoofing is accomplished by a manipulation of the JavaScript's prototype chain. Here is the example:

``javascript
(function(){
  var arr = ["secret1", "secret2", "secret3"];
  var x = arr.slice(1);
})();
```

Of course, let me try to explain the Non-Script-XSSI vulnerability again with a realistic scenario:

A web application processes data without security checks on dynamically included Non-Script files. This could allow attackers to cross-origin access sensitive information via Non-Script files. Here is a scenario that represents this vulnerability:

Step 1: Detection of Non-Script File
Attackers use automated tools to discover Non-Script files on the website. These tools focus on dynamically included files while analyzing the source code on the website. At this stage, attackers target a scenario where CSV files are included.

2. Exploitation of Non-Script File
Attackers use the following scenario to exploit the discovered Non-Script file:

```html
<script src="http://site.tld/non-script-file.csv" type="text/csv" charset="UTF-8"></script>
<script>
  // Sending data to an attacker-controlled server
  sendDataToAttackerServer(dataFromNonScriptFile);
</script>
```

In this code, the CSV file is included within the `script` tag and then data is sent to an attacker-controlled server via the `dataFromNonScriptFile` variable.

3. Leaking Sensitive Information
As a result of non-Script file exploitation, attackers can cross-origin access sensitive information. For example, if the content of the data in the CSV file contains users' personal information or other sensitive data, attackers can access this information and send it to the attacker-controlled server.


Conclusion:
You have learned in detail how to perform XSSI attacks and how to prevent them. With the red team approach, you can work effectively to detect and prevent XSSI attacks in target web applications. Remember, it is important to constantly update security measures and constantly test attack scenarios.