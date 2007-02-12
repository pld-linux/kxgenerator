Summary:	kX Generator - xorg.conf file generator
Summary(de.UTF-8):   kX Generator - ein xorg.conf Datei Generator
Summary(pl.UTF-8):   kX Generator - generator pliku xorg.conf
Name:		kxgenerator
Version:	0.3.7
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dp0154.debowypark.waw.pl/kxgenerator/data/download/%{name}-%{version}.tar.bz2
# Source0-md5:	dd539d7983597f050bf6bc67c790a939
Patch0:		%{name}-desktop.patch
URL:		http://kxgenerator.fe.pl/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kX Generator is a utilitty to configure the X server by modifying
xorg.conf file.

%description -l de.UTF-8
kX Generator ist ein Programm dass den X Server konfiguriert indem es
die xorg.conf Datei verändert.

%description -l pl.UTF-8
kX Generator to narzędzie do konfiguracji X serwera poprzez
modyfikowanie pliku xorg.conf.

%prep
%setup -q
%patch0 -p0

%build
cp -f /usr/share/automake/config.sub admin
%{__aclocal}
%{__autoconf}
%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}
install src/*.desktop $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

rm $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities/%{name}.desktop
rm $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities/kxgenerator-layout.desktop

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/*.desktop
#%{_pixmapsdir}/%{name}-logo.png
%{_iconsdir}/hicolor/*/apps/%{name}.png
