Summary: 	kio-locate
Name: 		kio-locate
Version: 	0.5.2
Release: 	%mkrel 1
Source:		http://kde-apps.org/CONTENT/content-files/120965-kio-locate-%{version}.tar.gz
License: 	GPLv2+
Group: 		Graphical desktop/KDE
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: 		http://kde-apps.org/content/show.php/kio-locate?content=120965
BuildRequires:  kdelibs4-devel

%description
This is kio-locate for KDE4.

%files -f kio_locate.lang
%defattr(-,root,root)
%{_kde_libdir}/kde4/*.so
%{_kde_docdir}/HTML/en/kioslave/kio-locate/*
%{_kde_services}/*.protocol
%{_kde_services}/searchproviders/*.desktop
#--------------------------------------------------------------------

%prep
%setup -qn kio-locate-%{version}

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%find_lang kio_locate

%clean
rm -rf $RPM_BUILD_ROOT


