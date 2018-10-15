#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : bluez-qt
Version  : 5.51.0
Release  : 5
URL      : https://download.kde.org/stable/frameworks/5.51/bluez-qt-5.51.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.51/bluez-qt-5.51.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.51/bluez-qt-5.51.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: bluez-qt-data = %{version}-%{release}
Requires: bluez-qt-lib = %{version}-%{release}
Requires: bluez-qt-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : qtbase-dev mesa-dev

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
%setup -q -n bluez-qt-5.51.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539610736
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1539610736
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/bluez-qt
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/bluez-qt/COPYING.LIB
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/lib/udev/rules.d/61-kde-bluetooth-rfkill.rules

%files data
%defattr(-,root,root,-)
/usr/share/xdg/bluez.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/BluezQt/BluezQt/Adapter
/usr/include/KF5/BluezQt/BluezQt/Agent
/usr/include/KF5/BluezQt/BluezQt/Device
/usr/include/KF5/BluezQt/BluezQt/DevicesModel
/usr/include/KF5/BluezQt/BluezQt/InitManagerJob
/usr/include/KF5/BluezQt/BluezQt/InitObexManagerJob
/usr/include/KF5/BluezQt/BluezQt/Input
/usr/include/KF5/BluezQt/BluezQt/Job
/usr/include/KF5/BluezQt/BluezQt/Manager
/usr/include/KF5/BluezQt/BluezQt/MediaPlayer
/usr/include/KF5/BluezQt/BluezQt/MediaPlayerTrack
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
/usr/include/KF5/BluezQt/BluezQt/Services
/usr/include/KF5/BluezQt/BluezQt/Types
/usr/include/KF5/BluezQt/bluezqt/adapter.h
/usr/include/KF5/BluezQt/bluezqt/agent.h
/usr/include/KF5/BluezQt/bluezqt/bluezqt_export.h
/usr/include/KF5/BluezQt/bluezqt/device.h
/usr/include/KF5/BluezQt/bluezqt/devicesmodel.h
/usr/include/KF5/BluezQt/bluezqt/initmanagerjob.h
/usr/include/KF5/BluezQt/bluezqt/initobexmanagerjob.h
/usr/include/KF5/BluezQt/bluezqt/input.h
/usr/include/KF5/BluezQt/bluezqt/job.h
/usr/include/KF5/BluezQt/bluezqt/manager.h
/usr/include/KF5/BluezQt/bluezqt/mediaplayer.h
/usr/include/KF5/BluezQt/bluezqt/mediaplayertrack.h
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
/usr/include/KF5/BluezQt/bluezqt/services.h
/usr/include/KF5/BluezQt/bluezqt/types.h
/usr/include/KF5/bluezqt_version.h
/usr/lib64/cmake/KF5BluezQt/KF5BluezQtConfig.cmake
/usr/lib64/cmake/KF5BluezQt/KF5BluezQtConfigVersion.cmake
/usr/lib64/cmake/KF5BluezQt/KF5BluezQtTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5BluezQt/KF5BluezQtTargets.cmake
/usr/lib64/libKF5BluezQt.so
/usr/lib64/qt5/mkspecs/modules/qt_BluezQt.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5BluezQt.so.5.51.0
/usr/lib64/libKF5BluezQt.so.6
/usr/lib64/qt5/qml/org/kde/bluezqt/DevicesModel.qml
/usr/lib64/qt5/qml/org/kde/bluezqt/libbluezqtextensionplugin.so
/usr/lib64/qt5/qml/org/kde/bluezqt/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bluez-qt/COPYING.LIB
