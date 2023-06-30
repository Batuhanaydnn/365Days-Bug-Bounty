# 2FA bypass teknikleri.

## Response Manipulation
Response Manipulation, bir API yanıtının içeriğini değiştirme işlemidir. İsteklerin yapıldığı API'ler genellikle JSON formatında yanıtlar döndürür. Response Manipulation, bu JSON yanıtlarındaki belirli bir öğeyi değiştirmeyi sağlar.

Örneğin, verilen senaryoda, yanıttaki "success" anahtarının değeri "false" olarak geliyorsa, bunu "true" olarak değiştirmek istiyoruz. Bu işlem, yanıtın içeriğini manipüle ederek gerçekleştirilebilir.

Response Manipulation işlemini gerçekleştirmek için aşağıdaki adımları izleyebilirsiniz:

- İsteği API'ye gönderin ve yanıtı alın.
- Yanıtı JSON formatında bir veri yapısına dönüştürün.
- Yanıtın içeriğini kontrol edin ve "success" anahtarının değerini kontrol edin.
- Eğer "success" değeri "false" ise, bu değeri "true" olarak değiştirin.
- JSON veri yapısını tekrar bir yanıt formatına dönüştürün.
- Değiştirilmiş yanıtı API isteği yapan koda veya kullanıcıya döndürün.

response_manipulation dosyasında örnek bir similasyon tasarlanmıştır.

## Status Code Manipulation
API yanıtındaki HTTP durum kodunu değiştirme işlemidir. HTTP durum kodları, bir isteğin veya yanıtın başarılı bir şekilde gerçekleşip gerçekleşmediğini belirten sayısal değerlerdir. Örneğin, 200 durum kodu "OK" durumunu temsil ederken, 4xx durum kodları genellikle isteğin hatalı olduğunu veya erişimin reddedildiğini gösterir.

Status Code Manipulation işlemi, yanıtın başarısız olduğunu belirten 4xx bir durum kodunu 200 OK olarak değiştirerek, kısıtlamaları atlayıp atlayamayacağımızı test etmeyi amaçlar.

- İsteği API'ye gönderin ve yanıtı alın.
- Yanıttaki HTTP durum kodunu kontrol edin.
- Eğer durum kodu 4xx (örneğin, 403 veya 404) ise, bu durum kodunu 200 OK olarak değiştirin.
- Değiştirilmiş yanıtı API isteği yapan koda veya kullanıcıya döndürün.

status_code_mannipulation dosyasında örnek bir simülasyon tasarlanmıştır.

