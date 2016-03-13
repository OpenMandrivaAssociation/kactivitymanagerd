%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kactivitymanagerd
Version: 5.5.95
Release: 1
Source0: http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: KDE Plasma 5 Activities
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Sql)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5GlobalAccel)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: boost-devel
Requires: kactivities >= 5.20.0

%description
KDE Plasma 5 Activities.

%prep
%setup -q
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang kactivities5

%files -f kactivities5.lang
%{_bindir}/%{name}5
