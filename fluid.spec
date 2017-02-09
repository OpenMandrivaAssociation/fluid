%define major 0
%define libname	%mklibname Fluid %{major}
%define devname	%mklibname -d Fluid

Summary:	Fluid modules for QtQuick applications
Name:		fluid
Version:	0.9.0
Release:	1
License:	LGPLv2+
Group:		Graphical desktop/Other
URL:		https://github.com/lirios
Source0:	https://github.com/lirios/fluid/releases/download/v%{version}/%{name}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	git
BuildRequires:	extra-cmake-modules
BuildRequires:	qt5-devel
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5QuickTest)
BuildRequires:	cmake(Qt5QuickControls2)

%description
Components for Qt Quick applications with Material Design and Universal

%package -n	%{libname}
Summary:	Library for accessing USB devices
Group:		System/Libraries

%description -n	%{libname}
Components for Qt Quick applications with Material Design and Universal

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n	%{devname}
Components for Qt Quick applications with Material Design and Universal
development files

%prep
%setup -q
./scripts/fetch_icons.sh

%build
%cmake_qt5
%make

%install
%makeinstall_std -C build

%files
%{_libdir}/qml/Fluid/*

%files -n %{libname}
%{_libdir}/libFluid.so.%{major}*

%files -n %{devname}
%{_bindir}/fluid-demo
%{_libdir}/libFluid.so
%{_libdir}/cmake/Fluid/
%{_includedir}/Fluid/fluid/*
%{_includedir}/Fluid/Fluid/DateUtils
