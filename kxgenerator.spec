Summary:	kX Generator - xorg.conf file generator
SUmmary(de):	kX Generator - ein xorg.conf Datei Generator
Summary(pl):	kX Generator - generator pliku xorg.conf
Name:		kxgenerator
Version:	0.2.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.kde-apps.org/content/files/39085-%{name}-%{version}.tar.bz2
# Source0-md5:	2fc78e92722408cccecfdcaf31ed1559
URL:		http://www.kde-apps.org/content/show.php?content=39085
BuildRequires:	autoconf
BuildRequires:	kdelibs-devel >= 9:3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kX Generator is a utilitty to configure the X server by modyfying xorg.conf file.

%description -l de
kX Generator ist ein Programm dass den X Server konfiguriert indem es die
xorg.conf Datei verändert.

%description -l pl
kX Generator to narzêdzie do konfiguracji X serwera poprzez modyfikacje
pliku xorg.conf.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/kxgenerator
%{_datadir}/applnk/Utilities/kxgenerator.desktop
%{_iconsdir}/hicolor/64x64/apps/kxgenerator.png
