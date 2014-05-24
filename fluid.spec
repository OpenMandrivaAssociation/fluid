Summary:	Fluid modules for QtQuick applications
Name:		fluid
Version:	0.2.0
Release:	1
License:	LGPLv2+
Group:		Graphical desktop/Other
URL:		http://www.maui-project.org
Source0:	http://downloads.sourceforge.net/project/mauios/hawaii/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	pkgconfig(Qt5)

%track
prog %{name} = {
	url = http://downloads.sourceforge.net/project/mauios/hawaii/
	regex = "%{name}-(__VER__)\.tar\.gz"
	version = %{version}
}

%description
Fluid modules for QtQuick applications.

%prep
%setup -q

%build
%cmake
%make

%install
%makeinstall_std -C build

%files
