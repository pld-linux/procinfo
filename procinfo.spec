Summary:	A tool for gathering and displaying system information
Summary(de):	Informationen zum proc-Dateisystem
Summary(fr):	informations sur le syst�me de fichiers proc
Summary(pl):	Informacje z filesystemu proc
Summary(tr):	proc dosya sistemi bilgileri
Name:		procinfo
Version:	17
Release:	3
License:	GPL
Group:		Utilities/System
Group(pl):	Narz�dzia/System
Source:		ftp://ftp.cistron.nl/pub/people/svm/%{name}-%{version}.tar.gz
Patch0:		procinfo-DESTDIR.patch
Patch1:		procinfo-cpus.patch
Patch2:		procinfo-smpfix.patch
BuildRequires:	ncurses-devel >= 5.0
Buildroot:	/tmp/%{name}-%{version}-root

%description
The procinfo command gets system data from the /proc directory (the kernel
filesystem), formats it and displays it on standard output. You can use
procinfo to acquire information about your system from the kernel as it is
running.

%description -l de
Mit dem Paket procinfo k�nnen Sie n�tzliche Informationen aus /proc
abrufen. /proc ist das Kernel-Dateisystem, das Informationen �ber den
laufenden Kernel enth�lt.

%description -l fr
procinfo est un paquetage permettant d'obtenir des informations utiles �
partir de /proc. /proc est le syst�me de fichiers du noyau. C'est l'endroit
o� vous pouvez allez pour obtenir des informations sur le noyau qui
s'ex�cute.

%description -l pl
Procinfo jest programem, kt�ry przekazuje informacje wyczytane z systemu
plik�w j�dra - /proc.

%description -l tr
procinfo, /proc dosya sisteminden bilgi alman�za izin veren bir pakettir.
/proc �ekirdek dosya sistemini tutar ve ko�an �ekirde�inizden bilgi
edinebilece�iniz bir dizin yap�s� sunar.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

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

gzip -9nf README $RPM_BUILD_ROOT%{_mandir}/man8/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/*
