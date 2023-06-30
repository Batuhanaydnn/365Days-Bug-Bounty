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

