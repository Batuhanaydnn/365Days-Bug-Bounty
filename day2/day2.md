## REDOS Zafiyetlerini anlamak

Bir websitesi geliştiren bir developer olduğunuzu düşünün. (Ben Hala daha yapıyorum bunu) bir mail adresinin kurallara uygun bir şekilde biçimlendirilip biçimlendirimediğini test etmek istiyorsunuz. Aklımıza gelen ilk şey çoğu zaman bir Regex yazarak bu ifadenin doğruluğunu kontrol etmek ve hatalı yahut saldırgan girişleri engellemektir. Çoğu yazılımcının atladığı nokta iste ReDos'tur. ReDos backendde belirlenmiş Regex'in testler sonucunda tahmini olarak çıkartılması ve oluşturulan zararlı yükle sunucu kaynaklarının aşırı tüketilerek zarar vermeyi amaçlayan bir güvenlik açığıdır. Bunu bir yazılımcı olarakta hacker olarakta farketmek zor olduğundan ve çoğu zaman kullanılan framework bunu engellediğinden dolayı web applicaton pentest kısmında çok fazla bu tip açıkla karşılaşmazsınız. Fakat bazen şirketler gelip Blue takımlarını test etmek için sizden yardım ister. ReDos tipi yükler Blue takımları çok üzecek şeyler için kullanılabileceğini sadece söylemek istiyorum. Bunun örneklerini vermeyeceğim. 

Şimdi biraz hikayeyi bırakıp uygulamaya geçelim. 

```
/(a+)+$/
```

Yukarıda verilmiş olan regex bir ifade içerisinde ardışık olarak kullanılan a karakterlerini tanımlar. Saldırganlar bu çeşit bir regexi manipüle etmek için çok sayıda a harfini göndererek saldırı yapabilirler. Örneğin "aaaaaaaaaaaaaaaaaaaaaaab" gibi bir metin ifadenin çalışmasını aşırı uzatır ve uygulamanın kaynaklarını tüketir.  

### Gerçek Hayattan uygulamalar
Gerçek Hayatta Uygulamalar:
Redos saldırıları, düzenli ifadeleri kullanan birçok uygulama ve senaryoda gerçekleştirilebilir. İşte bazı örnekler:

E-posta adresi doğrulama: Bir uygulama, kullanıcının girdiği e-posta adresinin geçerliliğini kontrol etmek için düzenli ifadeler kullanabilir. Ancak, düzenli ifadenin optimize edilmemesi durumunda, bir saldırgan çok uzun veya karmaşık bir e-posta adresiyle saldırı yapabilir.

Veri geçerliliği kontrolü: Web formları veya veritabanı girişleri gibi yerlerde düzenli ifadeler, kullanıcının girdiği verilerin geçerliliğini kontrol etmek için kullanılabilir. Ancak, saldırganlar, özellikle kullanıcıdan beklenmeyen büyük veya karmaşık verilerle saldırı yapabilir.

Log analizi: Sistem loglarını analiz etmek için düzenli ifadeler kullanıldığında, saldırganlar, özel olarak oluşturulmuş bir metinle log analiz işlemini yavaşlatabilir veya engelleyebilir.

### Bir ReDos Zafiyeti Keşfettiğimizi nasıl anlarız
Bir redos keşfettiğinizde aşağıdaki ifadelere benzer çıktılarla karşılaşıyorsanız bir ReDos zafiyeti keşfetmiş olabilirsiniz.

- Uygulama hızında belirgin bir düşüş veya yavaşlama: Redos saldırıları, bir düzenli ifadeye karşı karmaşık bir girişin işlenmesi nedeniyle hizmetin yavaşlamasına veya tamamen çökmesine yol açabilir. Eğer bir uygulama beklenmedik bir şekilde yavaşlamışsa veya cevap vermiyorsa, Redos saldırısını düşünmek önemlidir.

- İşlem süresindeki anormallikler: Redos saldırıları, düzenli ifadenin işlem süresini artırarak kaynak tüketir. Eğer düzenli ifadelerin işlem süresinde normalden çok daha uzun süren işlemler fark ederseniz, potansiyel bir Redos saldırısı olabilir.

- Karmaşık veya tekrarlayan düzenli ifadelerin kullanımı: Düzenli ifadelerde karmaşık veya tekrarlayan yapılar (geriye dönüş, yineleme vb.) içeren ifadeler, potansiyel Redos zafiyetlerini işaret edebilir. Özellikle düzenli ifadeleri kullanırken performans ve optimize edilme konularına dikkat etmek önemlidir.

## Birkaç uygulama ve similasyon hazırlayalım.
Günün dosyalarında redos zafiyeti için bazı simülasyonlar gerçekletirdim. Bunlar redos zafiyetini tanımanıza ve bununla ilgili geliştirilen uygulamalarda yapılan hatalı daha iyi kavramanıza yardımcı olacaktır.

1. Redos zafiyeti / Email Validation

Flask uygulamasi, `/validate`endpoint'i üzerinden POST isteklerini dinleyerek kullanıcının girdiği e-posta adresini alır. Ardından `validate_email()`fonksiyonunu kullanrak e-posta adresinin geçerliliğini kotrol eder. Geçerli ise büyük ihtimalle register veya login kısmına devam eder fakat bizim uygulamamızda geçerlilik sonucunda "E-posta adresi geçerli" yanıtını döndürür. Geçersiz ise "Geçersiz e-posta adresi" yanıtını döndürecektir

Burada e-posta adresinin geçerliliğini kontorl etmek için bir regex kullandık. `(r'^[\w\.-]+@[\w\.-]+\.\w+$')` . Denerseniz pek çok e-posta adresi için geçerli bir doğrulama olduğunu farkedersiniz. Fakat bu ifade bir Redos açığına yol açabilir.

Redos açığı, giriş verisindeki düzenli ifadenin performansını hatalı yazılmış regex yüzünden mahfedecektir. `[\w\.-]+` tarafından temsil edilen [\w\.-] karakter kümesi, alfanümerik karakterler, nokta ve tirenin birleşimini kabul eder. Bu kısım, ardışık olarak tekrarlandığında (yineleme ile), saldırganın gönderdiği uzun veya karmaşık bir girişle Redos saldırısına yol açabilir.

Saldırgan, örneğin 'aaaaaaaaaaaaaaaaaaaaaaaaaaaab@aaaaaaaaaaab.com' gibi bir ifade gönderdiğinde `[\w\.-]+` kısmının ardışık olarak birçok 'a' karakteriyle eşleştiği bir durum ortaya çıkar. Regex bu durumu eşitleyip ilerlemek için normalde olduğundan çok daha fazla zaman harcar ve bu durum performansı düşürür hatta hizmetin çökmesine dahi sebep olabilir.

2. Redos Zafiyet Tespiti / Fuzzing test yöntemi

Fuzzing, uygulamalarda rastgele veya özel olarak oluşturulmuş girişlere saldırarak hata ve zayıflıkları bulmayı amaçlayan bi test yöntemidir. Burada farklı uzunluklarda ve karmaşıklıklarda regex'imize ifadeler göndererek regexin tepki süresini ölçerek potansiyel redos zafiyetlerini bulmayı amaçlamaktayız.

3. Bir input verildiğinde / Regex üretici
İlk toolu yaptıktan sonra aklıma şöyle bir şey geldi. Biz input ifadeleri vererek bu input ifadelerine uygun bir regex ifade oluşturabilir miyiz? Evet tuhaf bir fikir fakat mümkün.




