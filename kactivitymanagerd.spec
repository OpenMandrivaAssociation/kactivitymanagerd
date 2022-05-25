%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kactivitymanagerd
Version:	5.24.5
Release: 2
Source0: http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/%{name}-%{version}.tar.xz
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
BuildRequires: cmake(KF5Crash)
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
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang kactivities5 || touch kactivities5.lang

%files -f kactivities5.lang
%dir %{_libdir}/qt5/plugins/%{name}
%dir %{_libdir}/qt5/plugins/%{name}/1
%{_datadir}/qlogging-categories5/%{name}.categories
%{_libdir}/lib%{name}_plugin.so
%{_libdir}/libexec/kactivitymanagerd
%{_libdir}/qt5/plugins/%{name}/1/%{name}_*.so
%{_datadir}/kservices5/%{name}.desktop
%{_datadir}/kservicetypes5/%{name}-plugin.desktop
%{_prefix}/lib/systemd/user/plasma-kactivitymanagerd.service
%{_datadir}/dbus-1/services/org.kde.ActivityManager.service
%{_datadir}/krunner/dbusplugins/plasma-runnners-activities.desktop
