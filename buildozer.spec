[app]

# (str) Title of your application
title = UBTech Robot Control

# (str) Package name
package.name = ubtechrobot

# (str) Package domain (needed for android/ios packaging)
package.domain = org.ubtech

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_exts = spec,pyc,pyo

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/.jpg

# (str) Application versioning (method 1)
version = 1.0.0

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,pyserial,speechrecognition,requests,pyjnius

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# OSX Specific
#

#
# author = © Copyright Info

# OSX icon and splashscreen
#icon.filename = %(source.dir)s/data/icon.icns
#presplash.filename = %(source.dir)s/data/presplash.png

#
# Android Specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,BLUETOOTH,BLUETOOTH_ADMIN,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,RECORD_AUDIO

# (int) Android API to use
android.api = 30

# (int) Minimum API required
android.minapi = 21

# (int) Android SDK version
android.sdk = 30

# (str) Android NDK version
android.ndk = 25b

# (list) Android architectures to build (default: armeabi-v7a, arm64-v8a, x86, x86_64)
android.arch = arm64-v8a, armeabi-v7a

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path =

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or to save time
# when the SDK is already up to date.
#android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only. If set to False,
# the default, you will be shown the license when first running buildozer.
android.accept_sdk_license = True

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (list) Android AAR archives to add (leave empty to not add any)
#android.add_aars =

# (list) Gradle dependencies to add (leave empty to not add any)
#android.gradle_dependencies =

# (list) Java classes to add
#android.add_src =

# (str) python-for-android branch to use, defaults to stable
#p4a.branch = stable

# (list) OUYA Console framework to add
#android.ouya.category = GAME
#android.ouya.filename = ouya_icon.png

# (str) Bootstrap mode for android (sdl2, pygame, webview, service_only)
android.bootstrap = sdl2

# (bool) If True, the graphics backend of the bootstrap (sdl2, pygame, webview) will be optimized (compiled with NEON etc.)
android.graphics_opts = True

# (bool) If True, the debug version of the bootstrap (sdl2, pygame, webview) will be used
#android.bootstrap.debug = False

# (str) If set, will be used as a version name in the Android Manifest
#android.version_name =

# (bool) If True, hides the status bar (Android)
#android.statusbar_hide = False

# (bool) If True, force the default permission to be added
#android.default_permissions = True

# (bool) Adds the permission to request the Android Activity to be hardware accelerated.
android.hardware_accelerated = True

# (list) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Copy libs instead of compiling (if possible)
#android.copy_libs = True

# (str) The Android arch to build for, the default is automatically chosen.
#android.arch = armeabi-v7a

# (bool) Turn on/off the android archeological tools (deprecated)
#android.archeological = False

#
# iOS Specific
#

# (str) Path to a custom kivy-ios folder
#ios.kivy_ios_dir = ../kivy-ios
# Alternately, specify the URL to clone kivy-ios from:
#ios.kivy_ios_url = https://github.com/kivy/kivy-ios

# (str) Path to ios SDK
#ios.sdk_path =

# (str) Version of the iOS SDK to use
#ios.sdk_version = 13.0

# (str) iOS deployment target
#ios.deployment_target = 13.0

# (str) Xcode project file to use, if using custom xcode project
#ios.xcode_project =

# (str) Xcode project configuration to use, if using custom xcode project
#ios.xcode_config = Debug

# (list) iOS frameworks to add
#ios.frameworks = libXYZ

# (bool) Delete the build directory before building (clean build)
#ios.clean_build = False

# (bool) Use the bitcode when building
#ios.bitcode = False

# (str) Method to use to sign the app (available: certificate, ad-hoc)
#ios.codesign.method = certificate

# (str) Certificate to use to sign the app (when codesign.method == certificate)
#ios.codesign.certificate = iPhone Developer: Me (XXXXXXXXXX)

# (str) Provisioning profile to use when signing the app (when codesign.method == certificate)
#ios.codesign.profile =

# (str) When using ad-hoc signing, the name of the app
#ios.codesign.appname =

# (bool) Whether to generate or not an debug iOS symbol file
#ios.symbols = False

#
# Windows Specific
#

# (list) Windows requirements (kivy, kivy-sdl2, etc.)
#p4a.window_requirements =

#
# General options
#

# (str) The directory where the project file lives
#build_dir = ./.buildozer

# (str) The directory where distributions will be stored
#dist_dir = ./bin

# (str) The name of the distribution to use
#target_name = ubtechrobot

# (str) The android logcat log level (default: 2)
#android.log_level = 2

# (bool) Turn on/off the debug mode of buildozer (default: False)
#buildozer.debug = False

# (str) The path to the android debug bridge (adb)
#android.adb = adb

# (str) The path to the android emulator
#android.emulator = emulator

# (str) The command to run the emulator (default: emulator)
#android.emulator_cmd = emulator

# (bool) Turn on/off the Android emulator
#android.emulator = False

# (str) The Android AVD to use (if android.emulator = True)
#android.avd =

# (bool) Whether to use the GPU with the Android emulator (if android.emulator = True)
#android.emulator_gpu = False

# (bool) Turn on/off the Android device
#android.device = False

# (str) The ADB device serial number to use (if android.device = True)
#android.device_serial =

# (bool) Whether to automatically accept the Android SDK license
#android.accept_sdk_license = True

# (list) The targets to build, choices: android, ios, windows
#targets = android

# (str) The log level for buildozer (default: 1)
log_level = 2

# (str) The folder to store the buildozer logs
#buildozer.log_dir = ./.buildozer/logs

# (bool) Whether to run the application on the device (if android.device = True)
#android.run = False

# (bool) Whether to run the application on the emulator (if android.emulator = True)
#android.run_emulator = False

# (bool) Whether to copy the application to the device (if android.device = True)
#android.copy_to_device = False

# (bool) Whether to install the application on the device (if android.device = True)
#android.install = False

# (str) The log level for the Android logcat (default: V)
#android.logcat_level = V

# (list) The Android logcat filters to use
#android.logcat_filters = *:S python:D

# (str) The path to the Android logcat output file (if empty, output to stdout)
#android.logcat_output =

# (str) The path to the Android logcat error output file (if empty, output to stderr)
#android.logcat_error_output =

# (bool) Whether to show the Android logcat output (default: True)
#android.logcat_show = True

# (bool) Whether to clear the Android logcat before starting (default: False)
#android.logcat_clear = False
