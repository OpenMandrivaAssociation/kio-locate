Summary: 	kio-locate
Name: 		kio-locate
Version: 	0.5.1
Release: 	%mkrel 1
Source:		http://kde-apps.org/CONTENT/content-files/120965-kio-locate-%{version}.tar.gz
License: 	GPLv2+
Group: 		Graphical desktop/KDE
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: 		http://kde-apps.org/content/show.php/kio-locate?content=120965
BuildRequires:  kdelibs4-devel

%description
This is kio-locate for KDE4.

%files
%defattr(-,root,root)
%{_kde_libdir}/kde4/*.so
%{_kde_docdir}/HTML/en/kioslave/kio-locate/*
#%{_kde_appsdir}/kio_locate
%{_kde_services}/*

%{_usr}/share/locale/cs/LC_MESSAGES/kio_locate.mo
%{_usr}/share/locale/de/LC_MESSAGES/kio_locate.mo
%{_usr}/share/locale/el/LC_MESSAGES/kio_locate.mo
%{_usr}/share/locale/fr/LC_MESSAGES/kio_locate.mo
#--------------------------------------------------------------------

%prep
%setup -qn kio-locate-%{version}

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%clean
rm -rf $RPM_BUILD_ROOT


