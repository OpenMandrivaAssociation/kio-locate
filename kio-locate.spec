Summary: 	kio-locate
Name: 		kio-locate
Version: 	0.5.3
Release: 	1
Source0:		http://kde-apps.org/CONTENT/content-files/120965-kio-locate-%{version}.tar.gz
License: 	GPLv2+
Group: 		Graphical desktop/KDE
URL: 		http://kde-apps.org/content/show.php/kio-locate?content=120965
BuildRequires:  kdelibs4-devel

%description
This is kio-locate for KDE4.

%files -f kio_locate.lang
%defattr(-,root,root)
%{_kde_libdir}/kde4/*.so
%{_kde_docdir}/HTML/en/kioslave/locate/*
%{_kde_services}/*.protocol
%{_kde_services}/searchproviders/*.desktop
#--------------------------------------------------------------------

%prep
%setup -qn kio-locate-%{version}

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang kio_locate
