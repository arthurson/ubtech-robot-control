[app]

# 应用基本信息
title = 优必选小微机器人控制软件
package.name = ubtechrobot
package.domain = org.ubtech

# 应用版本
version.regex = __version__ = ['"](.*)['"]
version.filename = %(source.dir)s/main.py

# 应用图标（如果有图标文件可以取消注释）
# icon.filename = %(source.dir)s/icon.png
# icon.filename = %(source.dir)s/icon-android.png

# 支持的架构
android.arch = armeabi-v7a, arm64-v8a

# Android API级别
android.api = 30
android.minapi = 21
android.ndk = 25b
android.sdk = 30

# 核心依赖 - 优化版本，避免编译问题
requirements = python3==3.9.25,kivy==2.3.0,kivymd==1.1.1,pySerial==3.5,speechrecognition==3.10.1,requests==2.31.0,pyjnius==1.5.0,openssl

# 注意：pyaudio 和 matplotlib 在Android上容易编译失败，暂时移除
# 如果需要语音功能，建议使用Android原生API通过pyjnius实现
# 如果需要图表功能，考虑使用其他轻量级方案

# Android权限
android.permissions = INTERNET,BLUETOOTH,BLUETOOTH_ADMIN,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,RECORD_AUDIO,ACCESS_NETWORK_STATE,WAKE_LOCK,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# Android特性
android.features = android.hardware.bluetooth,android.hardware.bluetooth_le,android.hardware.microphone

# Gradle依赖
android.gradle_dependencies = 'com.android.support:appcompat-v7:28.0.0','com.android.support:support-v4:28.0.0'

# 添加Android支持库
android.add_src = yes
android.whitelist = yes

# 服务声明（如果需要后台服务）
# android.services = YourService:your.service.Class

# 应用启动器
android.entrypoint = org.kivy.android.PythonActivity
android.fullscreen = 0

# 应用方向（0=自动, 1=竖屏, 2=横屏）
android.orientation = 1

# 应用主题
android.window_background_color = #FFFFFF
android.bootstrap = sdl2

# 资源文件
android.extra_java_dirs = 
android.add_services = 
android.add_authorities = 

# 应用元数据
android.meta_data = 

# 应用图标（如果有）
# android.icon = %(source.dir)s/icon.png
# android.presplash = %(source.dir)s/splash.png

# 包含的文件和排除规则
source.include_exts = py,png,jpg,kv,atlas,json,ttf,txt,md,ini
source.exclude_exts = spec,pyc,pyo,pyd,db,db3,so,o,os,DS_Store,git,pyproject
source.include_patterns = 
source.exclude_patterns = .git,.buildozer,__pycache__,*.pyc,*.pyo,*.so,*.db,*.db3,*.o,*.os,*.DS_Store

# 版本文件
version = 1.0.0

# 应用名称（不同平台）
fullscreen = 0

# 应用标题
title = 优必选小微机器人控制软件

# 应用描述
description = 优必选小微机器人综合控制平台，支持运动控制、语音交互、编程教学和远程监控功能

# 作者信息
author = Arthur Son

# 应用类别
category = Education

# 应用网址
# url = https://your-website.com

# 应用图标（Windows）
# icon = %(source.dir)s/icon.ico

# 其他平台设置
# ios.codesign.debug = 
# ios.codesign.release = 
# ios.codesign.framework = 

# OS X设置
# osx.icon = 
# osx.kivy_ios = 
# osx.bundle_identifier = 

# 构建优化
# 跳过某些不必要的检查
p4a.branch = develop
p4a.local_recipes = 
p4a.hook = 

# 日志级别（设置为2以便调试）
log_level = 2

# 警告抑制
warn_on_root = 0

# 交叉编译设置
# 确保编译时不因缺少某些库而失败
ignore_setup_py = yes

# 调试符号
debug = 1

# 构建目录
build_dir = %(source.dir)s/.buildozer

# 分发目录
dist_dir = %(source.dir)s/bin

# 签名配置（生产环境需要配置）
# android.release_keystore = 
# android.release_keystore_alias = 
# android.release_keystore_password = 

[buildozer]

# 日志级别
log_level = 2

# 警告抑制
warn_on_root = 0

# 路径设置
buildozer_dir = %(user)s/.buildozer
bin_dir = %(source.dir)s/bin

# Android SDK/NDK路径（使用环境变量或自动检测）
android.accept_sdk_license = True
android.ndk_path = 
android.sdk_path = 
android.ant_path = 

# 使用缓存
cache = True

# 更新设置
update = False

# 调试模式
debug = 1

# 设备连接
# android.logcat_filters = *:S python:D
# android.adb = 

# iOS设置
# ios.skip_xcodebuild = 
# ios.xcode_version = 
# ios.codesign_identity = 
# ios.provisioning_profile = 

# 其他平台
# p4a.branch = 
# p4a.local_recipes = 
# p4a.hook = 
