[app]
title = My Admin App
package.name = adminpanel
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
# Добавил hostpython3 и запепятые
requirements = python3,kivy,hostpython3
orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0
android.archs = arm64-v8a
android.api = 31
android.minapi = 21
android.ndk_api = 21
android.skip_update = False
android.accept_sdk_license = True
log_level = 2
