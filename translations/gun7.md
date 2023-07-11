Giriş:
Cross-Site Script Inclusion (XSSI) saldırılarına karşı korunma konusunda red team yaklaşımını ele alacağız. XSSI saldırıları, hedef web uygulamasının güvenlik zayıflıklarından yararlanarak kullanıcıların bilgilerini çalmak veya web uygulamasını etkilemek için yapılan saldırılardır. Bu eğitim, red team üyelerine XSSI saldırılarından korunma becerilerini geliştirmeleri için ayrıntılı adımlar sunacaktır.

## Bölüm 1: XSSI Saldırılarına Genel Bakış

XSSI saldırıları, Cross-Site Script Inclusion (Çapraz Site Komut İçermesi) saldırılarının bir türüdür. Bu saldırılar, saldırganların hedef web uygulamasının güvenlik zayıflıklarından yararlanarak kullanıcıların tarayıcılarında kötü niyetli kodların çalıştırılmasına izin verir.

Web uygulamalarının güvenliği, günümüzde büyük bir öneme sahiptir. Saldırganlar, kullanıcıların tarayıcılarında kötü niyetli betiklerin çalıştırılmasını sağlayarak, hassas verilere erişebilir veya kullanıcıların oturum bilgilerini ele geçirebilir. Bu tür saldırılardan biri de Cross-Site Script Inclusion (XSSI) saldırılarıdır.
XSSI saldırıları, bir web uygulamasında güvenlik açığına neden olan ve saldırganın dışarıdan bir betik ekleyerek kullanıcıların tarayıcılarında bu betiği çalıştırmasını sağlayan bir saldırı türüdür. Bu saldırı, web uygulamasının güvenlik kontrollerinin eksik veya zayıf olduğu durumlarda gerçekleşebilir.
XSSI saldırılarının potansiyel sonuçları oldukça ciddi olabilir. Saldırganlar, kullanıcıların oturum bilgilerini çalabilir, kötü niyetli betiklerin çalıştırılmasını sağlayabilir ve kullanıcıların hassas verilerini ele geçirebilir. Bu nedenle, web uygulamalarının XSSI saldırılarına karşı korunması büyük önem taşır.
XSSI saldırılarına karşı korunma yöntemleri arasında giriş parametrelerinin doğrulanması ve filtrelenmesi, güvenlik kontrollerinin güncel ve eksiksiz olması, kullanıcı girişlerinin doğru şekilde kodlanması ve güvenlik duvarı (firewall) kullanımı bulunur. Bu önlemler, saldırganların web uygulamasına dışarıdan kötü niyetli betikler eklemesini engelleyerek, kullanıcıların güvenliğini sağlar.

- XSSI saldırılarının potansiyel etkileri oldukça ciddi olabilir. İşte bazı örnekler:
- Kullanıcı Bilgilerinin Çalınması: XSSI saldırıları, saldırganların kullanıcıların oturum bilgilerini ele geçirmesine olanak tanır. Saldırgan, kötü niyetli bir betik ekleyerek kullanıcının tarayıcısında çalıştırır ve bu sayede kullanıcının oturum bilgilerini çalar. Bu bilgiler, saldırganın yetkisiz erişim sağlamasına ve kullanıcının hesabını ele geçirmesine yol açabilir.
- Kötü Niyetli Betiklerin Çalıştırılması: XSSI saldırıları, saldırganların web uygulamasında kötü niyetli betiklerin çalıştırılmasını sağlamasına olanak tanır. Bu betikler, kullanıcının tarayıcısında zararlı işlemler gerçekleştirebilir, kullanıcının bilgilerini çalabilir veya kullanıcının tarayıcısını kontrol altına alabilir. Bu durum, kullanıcıların güvenliğini ve gizliliğini tehlikeye atar.
- Web Uygulamasının Bütünlüğünün Tehlikeye Girmesi: XSSI saldırıları, saldırganların web uygulamasının bütünlüğünü tehlikeye atmasına neden olabilir. Saldırgan, dışarıdan eklediği betikler aracılığıyla web uygulamasının işlevselliğini bozabilir, veritabanına zarar verebilir veya hizmeti tamamen devre dışı bırakabilir. Bu durum, web uygulamasının kullanılabilirliğini etkiler ve ciddi maddi ve itibari zararlara yol açabilir.
- Bu potansiyel etkiler, XSSI saldırılarının ciddiyetini ve önemini vurgular. Web uygulamalarının XSSI saldırılarına karşı korunması, güvenlik kontrollerinin güncel ve eksiksiz olması, giriş parametrelerinin doğrulanması ve filtrelenmesi gibi önlemler alınmalıdır. Ayrıca, düzenli güvenlik testleri ve izleme süreçleri uygulanmalıdır.

## Bölüm 2: XSSI Saldırılarının Yapılandırma Zayıflıkları

CORS politikalarının doğru şekilde yapılandırılmaması, XSSI saldırılarına zemin hazırlar çünkü bu saldırılar, tarayıcının aynı kök etki alanı dışındaki kaynaklara erişmesine izin veren CORS politikalarını sömürür. Bu politikalar, tarayıcının bir web sitesinden diğerine veri göndermesini veya almasını sınırlar. Ancak, yanlış yapılandırılmış bir CORS politikası, tarayıcının kötü niyetli bir saldırganın kontrolündeki bir web sitesine veri göndermesine veya almasına izin verebilir.
Hedef web uygulamalarında yaygın olarak yapılan yapılandırma hataları şunları içerebilir:
- Yanlış yapılandırılmış CORS başlıkları: Web uygulaması, CORS başlıklarını yanlış şekilde yapılandırırsa, tarayıcılar bu başlıkları yanlış yorumlayabilir ve kötü niyetli bir saldırganın web uygulamasına erişmesine izin verebilir. Örneğin, Access-Control-Allow-Origin başlığı, tarayıcının hangi kaynaklara erişebileceğini belirler. Yanlış yapılandırılmış bir başlık, tarayıcının herhangi bir kaynağa erişmesine izin verebilir.
- Yanlış yapılandırılmış CSRF (Cross-Site Request Forgery) koruması: CSRF koruması, tarayıcının yalnızca belirli bir kaynaktan gelen istekleri kabul etmesini sağlar. Ancak, yanlış yapılandırılmış bir CSRF koruması, tarayıcının kötü niyetli bir saldırganın isteklerini kabul etmesine izin verebilir. Bu durumda, saldırgan, tarayıcının güvenilir bir kullanıcının kimliğiyle kötü niyetli istekler göndermesini sağlayabilir.
Bu hatalı yapılandırmaların sonuçları şunlar olabilir:
- Kullanıcı verilerinin tehlikeye girmesi: XSSI saldırıları, tarayıcının kullanıcıya ait verileri kötü niyetli bir saldırganın kontrolündeki bir web sitesine göndermesine veya almasına izin verebilir. Bu, kullanıcının gizli bilgilerinin (örneğin oturum açma bilgileri, kişisel bilgiler) saldırgan tarafından ele geçirilmesine yol açabilir.
- Kimlik avı saldırıları: Yanlış yapılandırılmış bir web uygulaması, saldırganın kullanıcılardan hassas bilgileri çalmak için kimlik avı saldırıları düzenlemesine olanak tanır. Saldırgan, kullanıcıları güvenilir bir web sitesine yönlendiren sahte bir web sitesi oluşturabilir ve kullanıcıların kimlik bilgilerini bu sahte siteye girmelerini sağlayabilir.

## Bölüm 3: XSSI Saldırı Türleri

1. ### Regular XSSI
Bir web uygulamasının sunucu tarafında yer alan JavaScript dosyasının, başka bir web sitesinden veya kaynaktan istemci tarafında yürütülmesine izin veren bir güvenlik açığıdır. Bu açık, sunucu tarafında yer alan JavaScript dosyasının, istemci tarafında doğrudan çağrılabilir ve içerdiği hassas bilgiler kötü niyetli kişiler tarafından ele geçirilebilir.

Aşağıda, bir örnek vererek Regular XSSI'nın nasıl çalıştığını açıklayalım:

1. Hedef web uygulaması, sunucu tarafında yer alan bir JavaScript dosyasında hassas bilgileri içeren bir değişkeni tanımlar. Örneğin, confidential_keys adında bir dizi.
2. Bu JavaScript dosyası, istemci tarafında erişilebilir bir konumda bulunur ve herhangi bir kullanıcı tarafından doğrudan çağrılabilir.
3. Saldırgan, kötü niyetli bir web sitesi veya içerik oluşturur.
4. Saldırgan, kötü niyetli içeriğe hedef web uygulamasının JavaScript dosyasını çağıran bir kod ekler. Örneğin:
```
<script src="https://www.vulnerable-domain.tld/script.js"></script>
<script> alert(JSON.stringify(confidential_keys[0])); </script>
```

5. Kullanıcı, saldırganın kötü niyetli web sitesini ziyaret eder.
6. Kötü niyetli web sitesi, hedef web uygulamasının JavaScript dosyasını çağırır.
7. JavaScript dosyası, istemci tarafında çalıştırılır ve confidential_keys[0] değişkenini içeren bir uyarı mesajı görüntüler.
8. Kullanıcı, uyarı mesajını görür ve saldırganın kötü niyetli web sitesi tarafından elde edilen hassas bilgilere maruz kalır.

Bu senaryoda, saldırgan, hedef web uygulamasının JavaScript dosyasını kötü niyetli bir web sitesi üzerinden çağırarak, kullanıcının hassas bilgilere erişmesini sağlamaktadır. Bu tür bir saldırı, güvenlik açıklarının olduğu web uygulamalarında gerçekleştirilebilir ve kullanıcıların bilgilerini tehlikeye atabilir. Bu nedenle, web uygulamalarının güvenliği için önlemler alınması önemlidir.

## Dynamic JavaScript-based XSSI ve Bilgi Sızdırma

Dynamic JavaScript-based XSSI, bir web uygulamasında kullanılan dinamik JavaScript betiklerinin güvenli bir şekilde yüklenmemesi sonucu ortaya çıkan bir güvenlik açığıdır. Bu açık, saldırganların web uygulamasının güvenlik kontrollerini atlayarak hassas bilgilere erişmesini sağlar. Bu eğitimde, Dynamic JavaScript-based XSSI güvenlik açığı ve bilgi sızdırma senaryolarını inceleyeceğiz.

**1. kısım: JSONP ile Bilgi Sızdırma**

JSONP (JSON with Padding), web uygulamalarında yaygın olarak kullanılan bir tekniktir. Ancak, güvenlik kontrolleri yapılmadan kullanıldığında XSSI açığına yol açabilir. İşte bu senaryonun örneği:

```javascript
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

Bu örnekte, JSONP yanıtı içindeki `angular.callbacks._7` geri çağırma işlevi, gizli bilgileri içeren `confidentialData` nesnesini alır ve bir uyarı mesajı olarak görüntüler. Gerçek senaryoda, `confidentialData` nesnesi gerçek kullanıcı bilgileriyle doldurulacaktır.

**Senaryo 2: JSONP ile Özel İşlev Kullanma**

Bu senaryoda, JSONP yanıtının özel bir işlev üzerinden işlenmesiyle bilgi sızdırma gerçekleştirilir. İşte örneği:

```javascript
<script>
  function leak(leaked) {
    alert(JSON.stringify(leaked));
  }
</script>
<script src="https://site.tld/p?jsonp=leak" type="text/javascript"></script>
```

Bu kodda, `leak` adında bir işlev tanımlanır ve JSONP yanıtı bu işlevi tetikleyerek gizli bilgileri içeren bir nesne geçirir. Gerçek senaryoda, `leak` işlevi, gizli bilgileri ele geçirerek uygun bir şekilde işleyecektir.

**Senaryo 3: Prototype Manipülasyonu ile Bilgi Sızdırma**

Bu senaryoda, JavaScript'in prototip zinciri üzerindeki bir manipülasyonla bilgi sızdırma gerçekleştirilir. İşte örneği:

```javascript
(function(){
  var arr = ["secret1", "secret2", "secret3"];
  var x = arr.slice(1);
})();
```

Tabii, Non-Script-XSSI açığına gerçeğe yakın bir senaryo ile tekrar anlatmaya çalışayım:

Bir web uygulaması, dinamik olarak dahil edilen Non-Script dosyalarında güvenlik kontrolleri yapmadan verileri işliyor. Bu durum, saldırganların Non-Script dosyaları aracılığıyla cross-origin olarak hassas bilgilere erişmelerini sağlayabilir. İşte bu açığı temsil eden bir senaryo:

1. Adım: Non-Script Dosyasının Tespiti
Saldırganlar, web sitesindeki Non-Script dosyalarını keşfetmek için otomatik araçlar kullanır. Bu araçlar, web sitesindeki kaynak kodunu analiz ederken, dinamik olarak dahil edilen dosyalara odaklanır. Bu aşamada saldırganlar, CSV dosyalarının dahil edildiği bir senaryoyu hedef olarak belirler.

2. Non-Script Dosyasının Sömürülmesi
Saldırganlar, keşfedilen Non-Script dosyasının sömürülmesi için aşağıdaki senaryoyu kullanır:

```html
<script src="http://site.tld/non-script-file.csv" type="text/csv" charset="UTF-8"></script>
<script>
  // Saldırganın kontrolündeki bir sunucuya verileri gönderme
  sendDataToAttackerServer(dataFromNonScriptFile);
</script>
```

Bu kodda, CSV dosyası `script` etiketi içinde dahil edilir ve ardından `dataFromNonScriptFile` değişkeni üzerinden saldırganın kontrolündeki bir sunucuya veriler gönderilir.

3. Hassas Bilgilerin Sızdırılması
Non-Script dosyasının sömürülmesi sonucunda, saldırganlar cross-origin olarak hassas bilgilere erişebilir. Örneğin, CSV dosyası içindeki verilerin içeriği kullanıcıların kişisel bilgilerini veya diğer hassas verileri içeriyorsa, saldırganlar bu bilgilere erişebilir ve saldırganın kontrolündeki sunucuya gönderebilir.


Sonuç:
XSSI saldırılarının nasıl gerçekleştirileceğini ve nasıl önlenmesi gerektiğini detaylı bir şekilde öğrendiniz. Red team yaklaşımıyla, hedef web uygulamalarında XSSI saldırılarının tespit edilmesi ve önlenmesi için etkili bir şekilde çalışabilirsiniz. Unutmayın, güvenlik önlemlerinin sürekli güncellenmesi ve saldırı senaryolarının sürekli olarak test edilmesi önemlidir.