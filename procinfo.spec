Summary:	A tool for gathering and displaying system information
Summary(de):	Informationen zum proc-Dateisystem
Summary(fr):	informations sur le système de fichiers proc
Summary(pl):	Informacje z filesystemu proc
Summary(tr):	proc dosya sistemi bilgileri
Name:		procinfo
Version:	18
Release:	2
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://ftp.cistron.nl/pub/people/svm/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-uptime.patch
Patch2:		%{name}-lsdev.patch
BuildRequires:	ncurses-devel >= 5.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The procinfo command gets system data from the /proc directory (the
kernel filesystem), formats it and displays it on standard output. You
can use procinfo to acquire information about your system from the
kernel as it is running.

%description -l de
Mit dem Paket procinfo können Sie nützliche Informationen aus /proc
abrufen. /proc ist das Kernel-Dateisystem, das Informationen über den
laufenden Kernel enthält.

%description -l fr
procinfo est un paquetage permettant d'obtenir des informations utiles
à partir de /proc. /proc est le système de fichiers du noyau. C'est
l'endroit où vous pouvez allez pour obtenir des informations sur le
noyau qui s'exécute.

%description -l pl
Procinfo jest programem, który przekazuje informacje wyczytane z
systemu plików j±dra - /proc.

%description -l tr
procinfo, /proc dosya sisteminden bilgi almanýza izin veren bir
pakettir. /proc çekirdek dosya sistemini tutar ve koþan
çekirdeðinizden bilgi edinebileceðiniz bir dizin yapýsý sunar.

%package perl
Summary:	procinfo perl helper scripts
Summary(pl):	Pomocnicze skrypty perlowe do procinfo
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Requires:	%{name} = %{version}

%description perl
Procinfo perl helper scripts.

%description perl -l pl
Pomocnicze skrypty perlowe do procinfo.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} CFLAGS="%{rpmcflags} -I/usr/include/ncurses" \
	LDLIBS="-lncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8}

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT" \
	prefix=%{_prefix} \
	bindir=%{_bindir} \
	mandir=%{_mandir}

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/procinfo
%{_mandir}/man8/procinfo*

%files perl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lsdev
%attr(755,root,root) %{_bindir}/socklist
%{_mandir}/man8/lsdev*
%{_mandir}/man8/socklist*
