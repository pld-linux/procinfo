Summary:	proc filesystem information
Summary(de):	Informationen zum proc-Dateisystem 
Summary(fr):	informations sur le syst�me de fichiers proc
Summary(pl):	Informacje z filesystemu proc 
Summary(tr):	proc dosya sistemi bilgileri
Name:		procinfo
Version:	17
Release:	2
Copyright:	GPL
Group:		Utilities/System
Group(pl):	Narz�dzia/System
Source:		ftp://ftp.cistron.nl/pub/people/svm/%{name}-%{version}.tar.gz
Patch:		procinfo-DESTDIR.patch
BuildRequires:	ncurses-devel >= 5.0
Buildroot:	/tmp/%{name}-%{version}-root

%description
procinfo is a package to allow you to get useful information
from /proc.  /proc is the kernel filesystem.  This is a place
you can go to acquire information from your running kernel.

%description -l de
Mit dem Paket procinfo k�nnen Sie n�tzliche Informationen aus
/proc abrufen. /proc ist das Kernel-Dateisystem, das Informationen
�ber den laufenden Kernel enth�lt.

%description -l fr
procinfo est un paquetage permettant d'obtenir des informations
utiles � partir de /proc. /proc est le syst�me de fichiers du noyau.
C'est l'endroit o� vous pouvez allez pour obtenir des informations
sur le noyau qui s'ex�cute.

%description -l pl
Procinfo jest programem, kt�ry przekazuje informacje wyczytane z systemu 
plik�w j�dra - /proc.

%description -l tr
procinfo, /proc dosya sisteminden bilgi alman�za izin veren bir pakettir.
/proc �ekirdek dosya sistemini tutar ve ko�an �ekirde�inizden bilgi
edinebilece�iniz bir dizin yap�s� sunar.

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
