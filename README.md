# Brute-force Login Simulator - Educational Repo

این مخزن برای اهداف آموزشی ساخته شده و شامل یک سرور تستی ساده (Flask) است که نمایش‌دهنده مفاهیم لاگین و محدودیت‌های ساده است. هرگونه استفاده از ابزارهای حمله‌محور بدون اجازه‌ی صریح مالک هدف، غیرقانونی است.

## فایل‌های داخل مخزن
- `vuln_app.py` : سرور Flask که endpoint `/login` و `/status` دارد.
- `tester_client.py` : یک کلاینت نمونه که یک درخواست لاگین ارسال می‌کند (فقط یک تلاش).
- `bruteforce_stub.md` : توضیح و pseudo-code برای اسکریپت Brute-force (فقط مستندات، بدون کد اجرایی).
- `requirements.txt` : وابستگی‌ها.
- `Dockerfile` : برای اجرای ایزوله شده در کانتینر (تنظیم برای bind روی localhost).
- `.gitignore` : فایل‌هایی که نباید به گیت منتقل شوند.

## هشدارهای مهم
- این پروژه فقط برای اجرا در محیط محلی یا محیط ایزوله‌شده (VM/Docker) طراحی شده است.
- انتشار اسکریپت‌های حمله‌ای یا اجرای آن‌ها علیه سیستم‌های واقعی که مالک آن نیستید غیرقانونی است.
- **این مخزن شامل کد اجرایی برای حمله خودکار یا brute-force نیست.**

## اجرا لوکال
1. ساخت virtualenv و نصب پکیج‌ها:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. اجرای سرور:
   ```bash
   python vuln_app.py
   ```
3. تست با `tester_client.py`:
   ```bash
   python tester_client.py --username alice --password alice123
   ```

## License
پیشنهادی: MIT
