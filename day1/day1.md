# 2FA bypass techniques.

## Response Manipulation
Response Manipulation is the process of changing the content of an API response. APIs from which requests are made typically return responses in JSON format. Response Manipulation allows to change a specific element in these JSON responses.

For example, in the given scenario, if the value of the "success" key in the response is "false", we want to change it to "true". This can be accomplished by manipulating the content of the response.

You can follow the steps below to perform Response Manipulation:

- Send the request to the API and get the response.
- Convert the response into a data structure in JSON format.
- Check the content of the response and check the value of the "success" key.
- If the value of "success" is "false", change it to "true".
- Convert the JSON data structure back into a response format.
- Return the modified response to the code or user making the API request.

A sample simulation is designed in the response_manipulation file.

## Status Code Manipulation
The process of changing the HTTP status code in the API response. HTTP status codes are numeric values that indicate whether a request or response was successful or not. For example, a status code of 200 represents an "OK" status, whereas 4xx status codes usually indicate that the request failed or access was denied.

Status Code Manipulation aims to test whether we can bypass restrictions by changing a 4xx status code to 200 OK, indicating that the response failed.

- Send the request to the API and receive the response.
- Check the HTTP status code in the response.
- If the status code is 4xx (for example, 403 or 404), change it to 200 OK.
- Return the modified response to the code or user making the API request.

An example simulation is designed in the status_code_mannipulation file.

## 2FA Code Leakage in Response

In Turkish, it can be expressed as "2FA Code Exfiltration in Response". This vulnerability refers to the disclosure of the 2FA code entered during the user's authentication process in the response.

This vulnerability usually occurs in cases where security controls are incorrectly implemented or missing. Below is a simple scenario to explain how this vulnerability occurs and what it is:

- The user sends a request to enter the 2FA code during the authentication process.
- The server verifies the 2FA code and authenticates the user.
- After the authentication process is complete, the server returns a response.
- However, the server discloses a message or data containing the 2FA code in the response.
- In this case, any attacker or malicious user who sees the response can obtain the 2FA code and access the account bypassing security measures.

This vulnerability poses a serious risk as the 2FA code is information that must remain confidential. Since the 2FA code is used as a second authentication factor, it is important to secure the user's identity. If the 2FA code is leaked in the response, the likelihood of an attacker gaining unauthorized access to the account increases.

An example simulation is designed in the twofa_code_leakage_in_response file.

## JS File Analysis


JS file analysis is a method used to identify potential vulnerabilities in web applications. During this analysis, the JavaScript files used by the web application are examined to see if they contain sensitive information such as 2FA codes. Here are some clues to the possibility of this vulnerability:

1. JS files are not properly protected: When developers do not secure JS files with protection mechanisms, these files become easily accessible, allowing malicious actors to inspect their contents. By learning the path where the JS file is stored on the server, or the full path to the file, they can access it and retrieve sensitive information.
    
2. Security vulnerabilities: Developers writing buggy or insecure code can lead to security vulnerabilities in JS files. For example, pieces of code that do not validate properly or do not process information received from the user securely enough can lead to sensitive information, such as 2FA codes, falling into the hands of malicious actors.
    
3. Malware plugins or attacks: In some cases, malware plugins or attacks may be included in JS files. These plugins or attacks may be designed to steal user information or intercept 2FA codes.
    

Therefore, it is important to follow the steps below during JS file analysis:

- Taking the necessary measures to ensure the protection of JS files, i.e. making the files inaccessible or securing the code.
- Carefully examine the code of JS files to identify vulnerabilities and points where sensitive information is handled.
- Use tools to verify the sources and content of JS files.
- Keep third-party JS libraries used in the web application up to date and obtain them from reliable sources.

An example simulation is given in the js_file_analysis file

## 2FA Code Reusability

**Description:**

This vulnerability occurs in the Two-Factor Authentication (2FA) mechanism used in a web application or system. 2FA is an authentication method with an additional step to authenticate users. Usually, in addition to a username and password combination, users are asked to enter a randomly generated verification code.

However, in this vulnerability, the 2FA code provided by the server is left without being revoked after successful authentication. As a result, the same 2FA code can be used repeatedly, creating a potential vulnerability that can be used to hijack accounts if an attacker obtains a valid 2FA code.

**Vulnerability Causes and Tricks:**

1. **Missing Expiration:** If the server does not invalidate or expire the 2FA code after successful authentication, attackers can use the same code multiple times.
    
2. **Reusable Verification Codes:** This vulnerability can occur if the server, instead of setting 2FA codes to be single-use, designs each code to be used multiple times instead of once.
    
3. **Lack of Code Tracking:** If the server does not track or log the 2FA codes being used, multiple-use codes will not be detected and attackers can exploit the vulnerability.
    
4. **Weak Code Generation:** If the server generates 2FA codes in a predictable or repetitive manner, attackers can anticipate and use the codes.
    

**Potential Attack Scenario:**

1. Attacker intercepts or guesses the target user's 2FA code.
    
2. The target user uses this 2FA code to authenticate and successfully logs in.
    
3. Since the server does not invalidate or track the used 2FA code, the attacker can reuse the same code.
    
4. The attacker can access the account or perform unauthorized actions using the reused 2FA code.
    
An example simulation is given in the two_fa_code_reusability file

## Lack of Brute-Force Protection

The "Lack of Brute-Force Protection" vulnerability is one of the weak points in a 2FA (Two-Factor Authentication) system. This vulnerability means that attackers can use a brute-force attack to guess authentication codes. Here are some details explaining what this vulnerability is and the tricks involved:

1. What Does the Vulnerability Mean? No brute-force protection means that a user can make an unlimited number of attempts to guess the verification code. The system does not implement any limitation or security measure to check if the verification code is correct. In this case, an attacker has a chance to guess the correct code by trying all possible combinations.
    
2. How is a Brute-Force Attack Performed? Attackers can use specialized software or tools for a brute-force attack. This software systematically generates verification codes and sends them to the system until it finds the correct code. Attackers can determine the number of attempts by taking into account the verification code length, complexity and other parameters in the system.
    
3. Tricks and Tips:
    

- You can make brute-force attacks harder by increasing the length and complexity of validation codes. Longer and more complex codes make it less likely that attackers will guess the correct code.
- You can prevent brute-force attacks by implementing an attempt limit or limitation mechanism in the system. For example, a certain number of failed attempts within a certain period of time can result in account lockout or delayed response.
- You can use CAPTCHA or similar mechanisms to block content-based attacks. Such mechanisms prevent automated attack software from automatically guessing verification codes.

## Missing 2FA Code Integrity Validation


The "Missing 2FA Code Integrity Validation" vulnerability refers to a vulnerability where the integrity of validation codes is not validated when using 2FA (Two-Factor Authentication) in a web application. The problem caused by this vulnerability is that a user can receive a 2FA authentication code once and then bypass 2FA by using that code on another user's account.

Below is a scenario describing this vulnerability and related tricks:

**Scenario**:

1. Two users, Alice and Bob, log into their accounts with 2FA in a web application.
2. Alice receives the 2FA code and completes the verification process.
3. The app does not save Alice's verification code and does not verify that the code has been used before.
4. Bob also receives the verification code and enters the same code into the app as Alice did before.
5. Since the app does not check that his code has been used before, Bob can access his account without the 2FA verification code.

In this case, the app does not check that 2FA verification codes must be single-use and unique and allows the same code to be used more than once.

**Trickler**:

1. Using the same code more than once: The app does not check for previously used codes before validating verification codes. This allows the same code to be used more than once.
    
2. Failure to save codes: The app does not save verification codes after they have been used or verify the validity of verified codes. Therefore, it cannot track whether the code has been used before and allows reuse.
    

This vulnerability could allow attackers to gain unauthorized access to the system by applying a successfully obtained 2FA verification code to the accounts of different targeted users.

## Disabling CSRF on 2FA

This vulnerability, called "CSRF on 2FA Disabling", occurs in the absence of CSRF (Cross-Site Request Forgery) protection and authorization confirmation when disabling 2FA.

The working logic of this vulnerability is as follows:

- An attacker targets a website or application that the user is logged into.
- This target website or application has a function or form for the user to disable 2FA.
- The attacker creates a malicious website or generates an attack link and sends it to the user.
- The user visits the website created by the attacker or clicks on the attack link.
- The attacker's website automatically makes a request to the target website or application that the user is logged into.
- This request uses the user's authentication credentials to disable 2FA. As a result, 2FA protection is removed and the attacker gains unauthorized access to the user's account.

This vulnerability allows attackers to unauthorizedly disable 2FA while users are logged in. Users' accounts may be at risk, especially if the target website or application performs this operation without an additional authentication or confirmation step to disable CSRF protection and 2FA.

## Password Reset Disable 2FA

The "Password Reset Disable 2FA" vulnerability occurs when 2FA is disabled when users change their password or email address. In this vulnerability, attackers can reset the password or change the email address to gain access to the user's account, thus disabling 2FA protection.

A scenario describing how the vulnerability works could be as follows:

- An attacker gains access to a target user's account information or email address.
- The attacker logs into the target user's account and starts the password reset or email change process.
- On the password reset or email change form, the attacker makes a change that affects the target user's 2FA settings.
- Once the process is complete, the user's password is reset or email address is changed, but 2FA is disabled.
- Now the attacker can access the target user's account without a password and 2FA code.

This vulnerability removes the security advantage of 2FA and makes accounts vulnerable to attackers. 2FA should not be automatically disabled when users change their password or email address.

## Backup Code Abuse

"Backup Code Abuse" is a vulnerability that exploits the backup code feature to bypass 2FA (Two-Factor Authentication) and remove 2FA restrictions. Let me explain how this vulnerability works:

- Backup Codes: In a 2FA system, users are provided with backup codes that they can use if they lose access to the primary authentication method. The backup codes are usually provided in the form of a list and each code can only be used once.

- Code Reuse: This vulnerability occurs when backup codes are not invalidated or tracked after use. If a system does not mark the use of a backup code or associate it with a specific user account, an attacker can bypass authentication by using it multiple times once they obtain a valid backup code.

- Bypassing 2FA: To exploit this vulnerability, an attacker must obtain a valid backup code associated with the target user's account. This can be accomplished through a variety of methods, including social engineering, phishing attacks, or compromising the user's device or account.

- Exploitation of the Backup Code: An attacker can substitute a valid backup code for a regular 2FA code in the 2FA authentication process. Since the validity or use of the backup code is not tracked, the system grants access to the attacker and thus bypasses 2FA protection.

- Removing / Resetting 2FA: After successfully bypassing 2FA using the backup code, the attacker gains unauthorized access to the user's account without the need for a legitimate 2FA device. They can then remove or reset the 2FA restrictions, leaving the account open to further attacks or unauthorized access.

To prevent the "Backup Code Abuse" vulnerability, it is important that backup codes are properly tracked and invalidated after use. Each backup code must be associated with a specific user account and can only be used once. Furthermore, backup codes must be protected by strong security measures against unauthorized access or interception.

## Clickjacking on 2FA Disabling Page

The "Clickjacking on 2FA Disabling Page" vulnerability allows an attacker to disable 2FA by framing the 2FA (Two-Factor Authentication) disabling page with an iframe and convincing the victim through social engineering methods.

Below are the steps that explain how this vulnerability works:

1. The attacker creates a malicious website or page that frames the target user's 2FA opt-out page with an iframe.
    
2. The malicious website may present a legitimate appearance to gain the victim's trust. For example, it may mimic the interface of a legitimate service or distract the victim by presenting compelling content.
    
3. The attacker designs the malicious website in a way that convinces the victim. For example, he may attract the victim's attention with a message such as "You need to temporarily disable 2FA to win a reward".
    
4. The victim visits the malicious website and does not realize they are on the real page because the content is presented via iframe.
    
5. The victim follows the instructions on the malicious website and enters the necessary information to disable 2FA.
    
6. Since iframes are used, the information entered by the victim is transmitted to the malicious website and the attacker intercepts it.
    
7. The attacker misleads or misdirects the victim by stating that 2FA has been successfully disabled.
    
8. The victim comes under the control of the attacker, believing that 2FA has actually been disabled. This can pose a serious risk to account security and allows an attacker to gain unauthorized access or take malicious actions.
    

To prevent this vulnerability, it is important to implement Clickjacking protection for sensitive operations such as the 2FA opt-out page. For example, you can prevent the page from loading in an iframe using the X-Frame-Options header or use security policies such as Content Security Policy (CSP).

## Enabling 2FA doesn't expire Previously active Sessions

The "Enabling 2FA doesn't expire Previously active Sessions" vulnerability occurs when a user enables 2FA (Two-Factor Authentication) but previously active sessions do not expire. If this vulnerability is accompanied by a session timeout vulnerability, it may be possible for an attacker to maintain access to the account even after 2FA is enabled.

This vulnerability allows an attacker who has already compromised a user's session to maintain access to the account even after 2FA has been enabled. This means that the additional layer of security provided by 2FA cannot effectively protect the account because the existing session remains active.

An attacker looking to exploit this vulnerability will typically gain unauthorized access to the user's account. This can be accomplished by stealing session cookies or session IDs or using other session hijacking techniques. Once the attacker has compromised the user's session, they can perform various malicious actions on the account.

When the actual user decides to enable 2FA, the system should ideally invalidate all previously enabled sessions and force the attacker to re-authenticate. However, when this vulnerability exists, the previously compromised session remains valid even after 2FA is enabled, allowing the attacker to continue accessing the account unhindered.

## Bypass 2FA with null or 000000

This method, called "Bypass 2FA with null or 000000", allows the user to enter null or the code "000000" to bypass 2FA (Two-Factor Authentication) protection. This method overrides the layer of security required by 2FA and bypasses the verification process. This vulnerability can occur for the following reasons:

1. Invalid Codes: The system does not check or filter incoming values before validating the 2FA code. In this case, entering an empty code or an invalid value such as "000000" could allow the system to log in without requiring a valid 2FA code.
    
2. Faulty Checks: The checks performed during the 2FA verification process may be insufficient or incorrect. For example, when the system uses an if condition to validate the verification code, it does not check that values such as blank or "000000" are valid. In this case, when the user enters these values, the system logs in without requiring a valid 2FA code.
    

**Tricks**

1. Blank or "000000" Code Entry: A malicious attacker may enter a blank value or the code "000000" on the 2FA verification screen. In this case, the system logs in without checking for a valid 2FA code, allowing the attacker to bypass the verification process and access the user's account.
    
2. Inadequate Code Checks: An attacker can target weak points of the code checking mechanism used to verify the 2FA code. For example, if the system is performing an incorrect code check or there is a situation where null values are valid, the attacker can exploit this to bypass 2FA protection.
    

This vulnerability could render the security layer provided by 2FA ineffective and allow an attacker to gain unauthorized access to accounts.