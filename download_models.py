# download_models.py
import argostranslate.package
import argostranslate.translate

available_packages = argostranslate.package.get_available_packages()

for package in available_packages:
    if (package.from_code, package.to_code) in [
        ("en", "hi"), ("hi", "en"),
        ("en", "gu"), ("gu", "en")
    ]:
        print(f"📥 Downloading {package.from_code} → {package.to_code}")
        download_path = package.download()
        argostranslate.package.install_from_path(download_path)

print("✅ All selected translation models installed.")
