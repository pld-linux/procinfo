Summary:	proc filesystem information
Summary(de):	Informationen zum proc-Dateisystem 
Summary(fr):	informations sur le système de fichiers proc
Summary(pl):	Informacje z filesystemu proc 
Summary(tr):	proc dosya sistemi bilgileri
Name:		procinfo
Version:	17
Release:	2
Copyright:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source:		ftp://ftp.cistron.nl/pub/people/svm/%{name}-%{version}.tar.gz
Patch:		procinfo-DESTDIR.patch
BuildRequires:	ncurses-devel >= 5.0
Buildroot:	/tmp/%{name}-%{version}-root

%description
procinfo is a package to allow you to get useful information
from /proc.  /proc is the kernel filesystem.  This is a place
you can go to acquire information from your running kernel.

%description -l de
Mit dem Paket procinfo können Sie nützliche Informationen aus
/proc abrufen. /proc ist das Kernel-Dateisystem, das Informationen
über den laufenden Kernel enthält.

%description -l fr
procinfo est un paquetage permettant d'obtenir des informations
utiles à partir de /proc. /proc est le système de fichiers du noyau.
C'est l'endroit où vous pouvez allez pour obtenir des informations
sur le noyau qui s'exécute.

%description -l pl
Procinfo jest programem, który przekazuje informacje wyczytane z systemu 
plików j±dra - /proc.

%description -l tr
procinfo, /proc dosya sisteminden bilgi almanýza izin veren bir pakettir.
/proc çekirdek dosya sistemini tutar ve koþan çekirdeðinizden bilgi
edinebileceðiniz bir dizin yapýsý sunar.

%prep
%setup -q
%patch -p1

%build
make	CFLAGS="$RPM_OPT_FLAGS -I/usr/include/ncurses" \
	LDLIBS="-lncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix},%{_bindir},%{_mandir}/man8}

make install \
	DESTDIR="$RPM_BUILD_ROOT" \
	prefix=%{_prefix} \
	bindir=%{_bindir} \
	mandir=%{_mandir}

gzip -9fn README $RPM_BUILD_ROOT%{_mandir}/man8/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/*
