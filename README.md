# BTC/USDT Monitor

Bu proje, Binance API'sini kullanarak BTC/USDT döviz kuru izleme uygulamasıdır. Uygulama, fiyat değişikliklerini 5 dakikalık aralıklarla kontrol eder ve sonuçları bir dosyaya yazar.

## Kurulum

1. Sanal ortam oluşturun:
   ```bash
   python -m venv myenv
   ```

2. Sanal ortamı aktifleştirin:
   - **Linux / MacOS**:
     ```bash
     source myenv/bin/activate
     ```
   - **Windows**:
     ```bash
     myenv\Scripts\activate
     ```

3. Gereksinimleri yükleyin:
   ```bash
   pip install -r src/requirements.txt
   ```

## Docker Kullanımı

1. Docker imajını oluşturun:
   ```bash
   docker build -t btc_usdt_monitor -f docker/Dockerfile .
   ```

2. Docker konteynerini başlatın:
   ```bash
   docker run -d --name btc_usdt_monitor btc_usdt_monitor
   ```

## Kubernetes Dağıtımı

1. Dağıtım ve servis oluşturun:
   ```bash
   kubectl apply -f k8s/deployment.yaml
   kubectl apply -f k8s/service.yaml
   ```

## Loglara Erişim

Log dosyaları `logs/btc_usdt_results.txt` içinde saklanmaktadır. Uygulama çalıştıkça fiyat değişiklikleri burada güncellenecektir.
