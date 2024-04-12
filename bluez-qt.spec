#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v10
# autospec commit: 81e1eeb
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : bluez-qt
Version  : 6.1.0
Release  : 81
URL      : https://download.kde.org/stable/frameworks/6.1/bluez-qt-6.1.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.1/bluez-qt-6.1.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.1/bluez-qt-6.1.0.tar.xz.sig
Source2  : D7574483BB57B18D.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 LGPL-2.1 LGPL-3.0
Requires: bluez-qt-data = %{version}-%{release}
Requires: bluez-qt-lib = %{version}-%{release}
Requires: bluez-qt-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# BluezQt
Qt wrapper for BlueZ 5 DBus API
## Introduction
BluezQt is a library for communication with BlueZ system and session daemons.

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) D7574483BB57B18D' gpg.status
%setup -q -n bluez-qt-6.1.0
cd %{_builddir}/bluez-qt-6.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1712952373
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DUDEV_RULES_INSTALL_DIR=/usr/lib/udev/rules.d
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DUDEV_RULES_INSTALL_DIR=/usr/lib/udev/rules.d
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1712952373
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/bluez-qt
cp %{_builddir}/bluez-qt-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/bluez-qt/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/bluez-qt-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/bluez-qt/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/bluez-qt-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/bluez-qt/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/bluez-qt-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/bluez-qt/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/bluez-qt-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/bluez-qt/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/bluez-qt-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/bluez-qt/e458941548e0864907e654fa2e192844ae90fc32 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories6/bluezqt.categories
/usr/share/qlogging-categories6/bluezqt.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/BluezQt/BluezQt/Adapter
/usr/include/KF6/BluezQt/BluezQt/Agent
/usr/include/KF6/BluezQt/BluezQt/Device
/usr/include/KF6/BluezQt/BluezQt/DevicesModel
/usr/include/KF6/BluezQt/BluezQt/GattApplication
/usr/include/KF6/BluezQt/BluezQt/GattCharacteristic
/usr/include/KF6/BluezQt/BluezQt/GattCharacteristicRemote
/usr/include/KF6/BluezQt/BluezQt/GattDescriptor
/usr/include/KF6/BluezQt/BluezQt/GattDescriptorRemote
/usr/include/KF6/BluezQt/BluezQt/GattManager
/usr/include/KF6/BluezQt/BluezQt/GattService
/usr/include/KF6/BluezQt/BluezQt/GattServiceRemote
/usr/include/KF6/BluezQt/BluezQt/InitManagerJob
/usr/include/KF6/BluezQt/BluezQt/InitObexManagerJob
/usr/include/KF6/BluezQt/BluezQt/Input
/usr/include/KF6/BluezQt/BluezQt/Job
/usr/include/KF6/BluezQt/BluezQt/LEAdvertisement
/usr/include/KF6/BluezQt/BluezQt/LEAdvertisingManager
/usr/include/KF6/BluezQt/BluezQt/Manager
/usr/include/KF6/BluezQt/BluezQt/Media
/usr/include/KF6/BluezQt/BluezQt/MediaEndpoint
/usr/include/KF6/BluezQt/BluezQt/MediaPlayer
/usr/include/KF6/BluezQt/BluezQt/MediaPlayerTrack
/usr/include/KF6/BluezQt/BluezQt/MediaTransport
/usr/include/KF6/BluezQt/BluezQt/MediaTypes
/usr/include/KF6/BluezQt/BluezQt/ObexAgent
/usr/include/KF6/BluezQt/BluezQt/ObexFileTransfer
/usr/include/KF6/BluezQt/BluezQt/ObexFileTransferEntry
/usr/include/KF6/BluezQt/BluezQt/ObexManager
/usr/include/KF6/BluezQt/BluezQt/ObexObjectPush
/usr/include/KF6/BluezQt/BluezQt/ObexSession
/usr/include/KF6/BluezQt/BluezQt/ObexTransfer
/usr/include/KF6/BluezQt/BluezQt/PendingCall
/usr/include/KF6/BluezQt/BluezQt/Profile
/usr/include/KF6/BluezQt/BluezQt/Request
/usr/include/KF6/BluezQt/BluezQt/Rfkill
/usr/include/KF6/BluezQt/BluezQt/Services
/usr/include/KF6/BluezQt/BluezQt/TPendingCall
/usr/include/KF6/BluezQt/BluezQt/Types
/usr/include/KF6/BluezQt/bluezqt/adapter.h
/usr/include/KF6/BluezQt/bluezqt/agent.h
/usr/include/KF6/BluezQt/bluezqt/bluezqt_export.h
/usr/include/KF6/BluezQt/bluezqt/device.h
/usr/include/KF6/BluezQt/bluezqt/devicesmodel.h
/usr/include/KF6/BluezQt/bluezqt/gattapplication.h
/usr/include/KF6/BluezQt/bluezqt/gattcharacteristic.h
/usr/include/KF6/BluezQt/bluezqt/gattcharacteristicremote.h
/usr/include/KF6/BluezQt/bluezqt/gattdescriptor.h
/usr/include/KF6/BluezQt/bluezqt/gattdescriptorremote.h
/usr/include/KF6/BluezQt/bluezqt/gattmanager.h
/usr/include/KF6/BluezQt/bluezqt/gattservice.h
/usr/include/KF6/BluezQt/bluezqt/gattserviceremote.h
/usr/include/KF6/BluezQt/bluezqt/initmanagerjob.h
/usr/include/KF6/BluezQt/bluezqt/initobexmanagerjob.h
/usr/include/KF6/BluezQt/bluezqt/input.h
/usr/include/KF6/BluezQt/bluezqt/job.h
/usr/include/KF6/BluezQt/bluezqt/leadvertisement.h
/usr/include/KF6/BluezQt/bluezqt/leadvertisingmanager.h
/usr/include/KF6/BluezQt/bluezqt/manager.h
/usr/include/KF6/BluezQt/bluezqt/media.h
/usr/include/KF6/BluezQt/bluezqt/mediaendpoint.h
/usr/include/KF6/BluezQt/bluezqt/mediaplayer.h
/usr/include/KF6/BluezQt/bluezqt/mediaplayertrack.h
/usr/include/KF6/BluezQt/bluezqt/mediatransport.h
/usr/include/KF6/BluezQt/bluezqt/mediatypes.h
/usr/include/KF6/BluezQt/bluezqt/obexagent.h
/usr/include/KF6/BluezQt/bluezqt/obexfiletransfer.h
/usr/include/KF6/BluezQt/bluezqt/obexfiletransferentry.h
/usr/include/KF6/BluezQt/bluezqt/obexmanager.h
/usr/include/KF6/BluezQt/bluezqt/obexobjectpush.h
/usr/include/KF6/BluezQt/bluezqt/obexsession.h
/usr/include/KF6/BluezQt/bluezqt/obextransfer.h
/usr/include/KF6/BluezQt/bluezqt/pendingcall.h
/usr/include/KF6/BluezQt/bluezqt/profile.h
/usr/include/KF6/BluezQt/bluezqt/request.h
/usr/include/KF6/BluezQt/bluezqt/rfkill.h
/usr/include/KF6/BluezQt/bluezqt/services.h
/usr/include/KF6/BluezQt/bluezqt/tpendingcall.h
/usr/include/KF6/BluezQt/bluezqt/types.h
/usr/include/KF6/BluezQt/bluezqt_version.h
/usr/lib64/cmake/KF6BluezQt/KF6BluezQtConfig.cmake
/usr/lib64/cmake/KF6BluezQt/KF6BluezQtConfigVersion.cmake
/usr/lib64/cmake/KF6BluezQt/KF6BluezQtTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6BluezQt/KF6BluezQtTargets.cmake
/usr/lib64/libKF6BluezQt.so
/usr/lib64/pkgconfig/KF6BluezQt.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF6BluezQt.so.6.1.0
/V3/usr/lib64/qt6/qml/org/kde/bluezqt/libbluezqtextensionplugin.so
/usr/lib64/libKF6BluezQt.so.6
/usr/lib64/libKF6BluezQt.so.6.1.0
/usr/lib64/qt6/qml/org/kde/bluezqt/DevicesModel.qml
/usr/lib64/qt6/qml/org/kde/bluezqt/bluezqtextensionplugin.qmltypes
/usr/lib64/qt6/qml/org/kde/bluezqt/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/bluezqt/libbluezqtextensionplugin.so
/usr/lib64/qt6/qml/org/kde/bluezqt/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bluez-qt/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/bluez-qt/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/bluez-qt/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/bluez-qt/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/bluez-qt/e458941548e0864907e654fa2e192844ae90fc32
