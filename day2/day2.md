## Understanding REDOS Vulnerabilities

Imagine you are a developer building a website (I still do it) and you want to test if a mail address is formatted according to the rules. The first thing that comes to mind is often to write a Regex to check the correctness of this expression and prevent incorrect or offensive input. What most developers miss is ReDos. ReDos is a vulnerability that aims to damage the server resources by overconsuming server resources with the malicious load created by guessing the Regex specified in the backend as a result of the tests. Since it is difficult to notice this as a software developer or a hacker and most of the time the framework used prevents it, you will not encounter many such vulnerabilities in the web application pentest part. But sometimes companies come and ask you for help to test their Blue suites. I just want to say that ReDos type payloads can be used for things that can make Blue teams very upset. I will not give examples of this. 

Now let's leave a little bit of the story and go to practice. 

```
/(a+)+$/
```

The regex given above defines the characters a used consecutively in an expression. Attackers can manipulate this type of regex by sending a large number of a's. For example, a text like "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab" would over-extend the execution of the expression and consume the application's resources.  

### Real Life applications
Real Life Applications:
Redos attacks can be performed in many applications and scenarios that use regular expressions. Here are some examples:

Email address validation: An application can use regular expressions to check the validity of the email address entered by the user. However, if the regular expression is not optimized, an attacker can attack with an email address that is too long or complex.

Data validity check: In places like web forms or database entries, regular expressions can be used to check the validity of the data entered by the user. However, attackers can attack with large or complex data, especially data that is not expected from the user.

Log analysis: When regular expressions are used to analyze system logs, attackers can slow down or block the log analysis process with specially constructed text.

### How to know if we have discovered a ReDos vulnerability
If you encounter outputs similar to the following statements when you discover a redos, you may have discovered a ReDos vulnerability.

- A significant decrease or slowdown in application speed: Redos attacks can cause a service to slow down or crash completely due to the processing of a complex input against a regular expression. If an application is unexpectedly slow or unresponsive, it is important to consider a Redos attack.

- Processing time anomalies: Redos attacks consume resources by increasing the processing time of a regular expression. If you notice anomalies in the processing time of regular expressions that take much longer than normal, it could be a potential Redos attack.

- Use of complex or repetitive regular expressions: Expressions that contain complex or repetitive structures (backtracking, iteration, etc.) in regular expressions may indicate potential Redos vulnerabilities. It is important to pay attention to performance and optimization issues, especially when using regular expressions.

## Let's prepare some applications and simulations.
In the files of the day I have implemented some simulations for the redos vulnerability, which will help you to recognize the redos vulnerability and better understand the mistakes made in the applications developed around it.

1. Redos vulnerability / Email Validation

The Flask application listens to POST requests via the `/validate` endpoint and retrieves the e-mail address entered by the user. Then it checks the validity of the e-mail address using the `validate_email()` function. If it is valid, it will probably continue with the register or login part, but in our application, it will return "The email address is valid" as a result of validity. If invalid, it will return "Invalid email address".

Here we used a regex to check the validity of the email address. `(r'^[\w\.-]+@[\w\.-]+\.\w+$')` . If you try it, you'll notice that it's a valid validation for many email addresses. However, this statement can lead to a Redos vulnerability.

A Redos vulnerability will ruin the performance of the regular expression in the input data because of a misspelled regex. The [\w\.-] character set, represented by `[\w\.-]+`, accepts a combination of alphanumeric characters, periods and dashes. This part, when repeated consecutively (by iteration), can lead to a Redos attack with a long or complex input sent by the attacker.

When an attacker sends, for example, an expression like 'aaaaaaaaaaaaaaaaaaaaaaaaaaaab@aaaaaaaaaaab.com', a situation arises where the `[\w\.-]+` part matches many consecutive 'a' characters. Regex spends much more time than usual to synchronize and progress, which degrades performance and may even crash the service.

2. Redos Vulnerability Detection / Fuzzing test method

Fuzzing is a testing method that aims to find bugs and weaknesses in applications by attacking random or specially generated inputs. Here we aim to find potential redos vulnerabilities by sending expressions of different lengths and complexities to our regex and measuring the response time of the regex.

3. Given an input / Regex generator
After making the first tool, something like this came to my mind. Can we give input expressions and create a regex expression suitable for these input expressions? Yes it's a weird idea but it is possible.

## Appendices and recommended documentation
I have learned and summarized many of the things I have written here from the internet like you. If you want to read more and the sources I have reviewed and do your own experiments, you can check the links below.

- https://rexegg.com
- https://regexone.com
- https://speakerdeck.com/harshbothra/having-fun-with-regex
- https://javascript.info/regexp-catastrophic-backtracking
- https://regular-expressions.info/redos.html 
- https://hackerone.com/reports/511381
- https://hackerone.com/reports/661722

