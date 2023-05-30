#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : bluez-qt
Version  : 5.106.0
Release  : 65
URL      : https://download.kde.org/stable/frameworks/5.106/bluez-qt-5.106.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.106/bluez-qt-5.106.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.106/bluez-qt-5.106.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 LGPL-2.1 LGPL-3.0
Requires: bluez-qt-config = %{version}-%{release}
Requires: bluez-qt-data = %{version}-%{release}
Requires: bluez-qt-lib = %{version}-%{release}
Requires: bluez-qt-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# BluezQt
Qt wrapper for BlueZ 5 DBus API
## Introduction
BluezQt is a library for communication with BlueZ system and session daemons.

%package config
Summary: config components for the bluez-qt package.
Group: Default

%description config
config components for the bluez-qt package.


%package data
Summary: data components for the bluez-qt package.
Group: Data

%description data
data components for the bluez-qt package.


%package dev
Summary: dev components for the bluez-qt package.
Group: Development
Requires: bluez-qt-lib = %{version}-%{release}
Requires: bluez-qt-data = %{version}-%{release}
Provides: bluez-qt-devel = %{version}-%{release}
Requires: bluez-qt = %{version}-%{release}

%description dev
dev components for the bluez-qt package.


%package lib
Summary: lib components for the bluez-qt package.
Group: Libraries
Requires: bluez-qt-data = %{version}-%{release}
Requires: bluez-qt-license = %{version}-%{release}

%description lib
lib components for the bluez-qt package.


%package license
Summary: license components for the bluez-qt package.
Group: Default

%description license
license components for the bluez-qt package.


%prep
%setup -q -n bluez-qt-5.106.0
cd %{_builddir}/bluez-qt-5.106.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685485149
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake .. -DUDEV_RULES_INSTALL_DIR=/usr/lib/udev/rules.d
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake .. -DUDEV_RULES_INSTALL_DIR=/usr/lib/udev/rules.d
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1685485149
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/bluez-qt
cp %{_builddir}/bluez-qt-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/bluez-qt/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/bluez-qt-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/bluez-qt/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/bluez-qt-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/bluez-qt/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/bluez-qt-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/bluez-qt/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/bluez-qt-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/bluez-qt/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/bluez-qt-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/bluez-qt/e458941548e0864907e654fa2e192844ae90fc32 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/61-kde-bluetooth-rfkill.rules

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/bluezqt.categories
/usr/share/qlogging-categories5/bluezqt.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/BluezQt/BluezQt/Adapter
/usr/include/KF5/BluezQt/BluezQt/Agent
/usr/include/KF5/BluezQt/BluezQt/Device
/usr/include/KF5/BluezQt/BluezQt/DevicesModel
/usr/include/KF5/BluezQt/BluezQt/GattApplication
/usr/include/KF5/BluezQt/BluezQt/GattCharacteristic
/usr/include/KF5/BluezQt/BluezQt/GattCharacteristicRemote
/usr/include/KF5/BluezQt/BluezQt/GattDescriptorRemote
/usr/include/KF5/BluezQt/BluezQt/GattManager
/usr/include/KF5/BluezQt/BluezQt/GattService
/usr/include/KF5/BluezQt/BluezQt/GattServiceRemote
/usr/include/KF5/BluezQt/BluezQt/InitManagerJob
/usr/include/KF5/BluezQt/BluezQt/InitObexManagerJob
/usr/include/KF5/BluezQt/BluezQt/Input
/usr/include/KF5/BluezQt/BluezQt/Job
/usr/include/KF5/BluezQt/BluezQt/LEAdvertisement
/usr/include/KF5/BluezQt/BluezQt/LEAdvertisingManager
/usr/include/KF5/BluezQt/BluezQt/Manager
/usr/include/KF5/BluezQt/BluezQt/Media
/usr/include/KF5/BluezQt/BluezQt/MediaEndpoint
/usr/include/KF5/BluezQt/BluezQt/MediaPlayer
/usr/include/KF5/BluezQt/BluezQt/MediaPlayerTrack
/usr/include/KF5/BluezQt/BluezQt/MediaTransport
/usr/include/KF5/BluezQt/BluezQt/MediaTypes
/usr/include/KF5/BluezQt/BluezQt/ObexAgent
/usr/include/KF5/BluezQt/BluezQt/ObexFileTransfer
/usr/include/KF5/BluezQt/BluezQt/ObexFileTransferEntry
/usr/include/KF5/BluezQt/BluezQt/ObexManager
/usr/include/KF5/BluezQt/BluezQt/ObexObjectPush
/usr/include/KF5/BluezQt/BluezQt/ObexSession
/usr/include/KF5/BluezQt/BluezQt/ObexTransfer
/usr/include/KF5/BluezQt/BluezQt/PendingCall
/usr/include/KF5/BluezQt/BluezQt/Profile
/usr/include/KF5/BluezQt/BluezQt/Request
/usr/include/KF5/BluezQt/BluezQt/Rfkill
/usr/include/KF5/BluezQt/BluezQt/Services
/usr/include/KF5/BluezQt/BluezQt/TPendingCall
/usr/include/KF5/BluezQt/BluezQt/Types
/usr/include/KF5/BluezQt/bluezqt/adapter.h
/usr/include/KF5/BluezQt/bluezqt/agent.h
/usr/include/KF5/BluezQt/bluezqt/bluezqt_export.h
/usr/include/KF5/BluezQt/bluezqt/device.h
/usr/include/KF5/BluezQt/bluezqt/devicesmodel.h
/usr/include/KF5/BluezQt/bluezqt/gattapplication.h
/usr/include/KF5/BluezQt/bluezqt/gattcharacteristic.h
/usr/include/KF5/BluezQt/bluezqt/gattcharacteristicremote.h
/usr/include/KF5/BluezQt/bluezqt/gattdescriptorremote.h
/usr/include/KF5/BluezQt/bluezqt/gattmanager.h
/usr/include/KF5/BluezQt/bluezqt/gattservice.h
/usr/include/KF5/BluezQt/bluezqt/gattserviceremote.h
/usr/include/KF5/BluezQt/bluezqt/initmanagerjob.h
/usr/include/KF5/BluezQt/bluezqt/initobexmanagerjob.h
/usr/include/KF5/BluezQt/bluezqt/input.h
/usr/include/KF5/BluezQt/bluezqt/job.h
/usr/include/KF5/BluezQt/bluezqt/leadvertisement.h
/usr/include/KF5/BluezQt/bluezqt/leadvertisingmanager.h
/usr/include/KF5/BluezQt/bluezqt/manager.h
/usr/include/KF5/BluezQt/bluezqt/media.h
/usr/include/KF5/BluezQt/bluezqt/mediaendpoint.h
/usr/include/KF5/BluezQt/bluezqt/mediaplayer.h
/usr/include/KF5/BluezQt/bluezqt/mediaplayertrack.h
/usr/include/KF5/BluezQt/bluezqt/mediatransport.h
/usr/include/KF5/BluezQt/bluezqt/mediatypes.h
/usr/include/KF5/BluezQt/bluezqt/obexagent.h
/usr/include/KF5/BluezQt/bluezqt/obexfiletransfer.h
/usr/include/KF5/BluezQt/bluezqt/obexfiletransferentry.h
/usr/include/KF5/BluezQt/bluezqt/obexmanager.h
/usr/include/KF5/BluezQt/bluezqt/obexobjectpush.h
/usr/include/KF5/BluezQt/bluezqt/obexsession.h
/usr/include/KF5/BluezQt/bluezqt/obextransfer.h
/usr/include/KF5/BluezQt/bluezqt/pendingcall.h
/usr/include/KF5/BluezQt/bluezqt/profile.h
/usr/include/KF5/BluezQt/bluezqt/request.h
/usr/include/KF5/BluezQt/bluezqt/rfkill.h
/usr/include/KF5/BluezQt/bluezqt/services.h
/usr/include/KF5/BluezQt/bluezqt/tpendingcall.h
/usr/include/KF5/BluezQt/bluezqt/types.h
/usr/include/KF5/BluezQt/bluezqt_version.h
/usr/lib64/cmake/KF5BluezQt/KF5BluezQtConfig.cmake
/usr/lib64/cmake/KF5BluezQt/KF5BluezQtConfigVersion.cmake
/usr/lib64/cmake/KF5BluezQt/KF5BluezQtTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5BluezQt/KF5BluezQtTargets.cmake
/usr/lib64/libKF5BluezQt.so
/usr/lib64/pkgconfig/KF5BluezQt.pc
/usr/lib64/qt5/mkspecs/modules/qt_BluezQt.pri

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF5BluezQt.so.5.106.0
/V3/usr/lib64/qt5/qml/org/kde/bluezqt/libbluezqtextensionplugin.so
/usr/lib64/libKF5BluezQt.so.5.106.0
/usr/lib64/libKF5BluezQt.so.6
/usr/lib64/qt5/qml/org/kde/bluezqt/DevicesModel.qml
/usr/lib64/qt5/qml/org/kde/bluezqt/libbluezqtextensionplugin.so
/usr/lib64/qt5/qml/org/kde/bluezqt/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bluez-qt/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/bluez-qt/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/bluez-qt/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/bluez-qt/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/bluez-qt/e458941548e0864907e654fa2e192844ae90fc32
