Summary:	Fluid modules for QtQuick applications
Name:		fluid
Version:	0.7.0
Release:	1
License:	LGPLv2+
Group:		Graphical desktop/Other
URL:		https://github.com/hawaii-desktop/%{name}
Source0:	https://github.com/hawaii-desktop/%{name}/release/%{name}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	qt5-devel

%description
Fluid modules for QtQuick applications.

%prep
%setup -q

%build
%cmake_qt5
%make

%install
%makeinstall_std -C build

%files
%dir %{_libdir}/hawaii/qml/Fluid
%{_libdir}/hawaii/qml/Fluid/*

