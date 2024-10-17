Summary:	Locate KIO slave for KDE4
Name:		kio-locate
Version:	0.5.3
Release:	3
License:	GPLv2+
Group:		Graphical desktop/KDE
URL:		https://kde-apps.org/content/show.php/kio-locate?content=120965
Source0:	http://kde-apps.org/CONTENT/content-files/120965-kio-locate-%{version}.tar.gz
Patch0:		kio-locate-0.5.3-gcc4.7.patch
BuildRequires:	kdelibs4-devel

%description
Locate KIO slave for KDE4.

%files -f kio_locate.lang
%{_kde_libdir}/kde4/*.so
%{_kde_docdir}/HTML/en/kioslave/locate/*
%{_kde_services}/*.protocol
%{_kde_services}/searchproviders/*.desktop
#--------------------------------------------------------------------

%prep
%setup -qn kio-locate-%{version}
%patch0 -p1

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang kio_locate

